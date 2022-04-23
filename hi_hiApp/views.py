from logging import exception
from django.shortcuts import redirect,render
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
from django.contrib import messages
from importlib_metadata import requires
from django.contrib.auth.decorators import login_required
from .form import *
from .models import *

def index(request):
    return render(request, 'hi_hiApp/index.html', None)

def account_info(request):
    return render(request, 'hi_hiApp/account-info.html', None)

def activity(request):
    transaction_history = transaction.objects.all().filter(Sender=request.user)
    context = {
        'transaction_history':transaction_history,
    }
    return render(request, 'hi_hiApp/activity.html', context)

def add_to_pot(request):
    card_details = users_wallet.objects.all().filter(user=request.user)
    context = {
        'card_details':card_details,
    }
    return render(request, 'hi_hiApp/add-to-pot.html', context)

def card_added(request):
    return render(request, 'hi_hiApp/card-added.html', None)

def help(request):
    return render(request, 'hi_hiApp/help.html', None)

def transfer_status(request):
    return render(request, 'hi_hiApp/transfer-status.html', None)

@login_required(login_url='login')
def send_money(request):
    transaction_instance = transaction(Sender=request.user)
    if request.method == 'POST':
        transaction_form = sending_moneyForm(request.POST, instance=transaction_instance)
        if transaction_form.is_valid():
            transaction_item = transaction_form.save()
            transaction_item.user = request.user
            
            try:
                sent_amount = transaction_form.cleaned_data.get('amount') #Amount to be sent
                receiver = transaction_form.cleaned_data['user'] #Recipient
                receivers_currency = transaction_form.cleaned_data['Currency'] #Recipient currency
                                
                senders_current_ballance = users_wallet.objects.all().filter(user=request.user).values_list('credict_ballance')
                receivers_current_ballance = users_wallet.objects.all().filter(user=receiver).values_list('credict_ballance')
                
                #cheking if receiver exists in the database
                user_check = users_wallet.objects.all().filter(user=receiver).exists()
                
                Naira_rate = rate.objects.all().values_list('Naira')
                Cedes_rate = rate.objects.all().values_list('Cedes')
                
                # performing the user check
                if user_check:
                    for item in senders_current_ballance:
                        senders_available_amount = int(item[0])
                        
                        # checking if the sender's balance is sufficent for the transaction
                        if senders_available_amount >= int(sent_amount):
                        
                            senders_balance = int(senders_available_amount) - int(sent_amount) 
                            # Updating the Available balance in senders wallet
                            users_wallet.objects.all().filter(user=request.user).update(credict_ballance=senders_balance)
                                                
                            for item in  receivers_current_ballance:
                                receivers_available_amount = int(item[0])
                                
                                #making a currency conversion for transfer
                                if receivers_currency == NG:
                                    # Naira rate conversion
                                    receivers_balance = int(receivers_available_amount) + (int(sent_amount) * 450 )
                                    # Cedes rate conversion
                                elif receivers_currency ==  GH:
                                    receivers_balance = int(receivers_available_amount) + (int(sent_amount) * 150 )
                                else:
                                    receivers_balance = int(receivers_available_amount) + (int(sent_amount) * 1 )
                                                                        
                                # Updating the Available balance in receivers wallet
                                users_wallet.objects.all().filter(user=receiver).update(credict_ballance=receivers_balance)
                    
                        else:
                            messages.warning(request, "Your balance is too low for this transaction!!!")
                            return redirect('send_money')
                else:
                    messages.warning(request, "Please check the user name entered!!!")
                    return redirect('send_money')
            except:
                messages.warning(request, "did'nt work something went wrong")
                return redirect('send_money')
            else: 
                messages.info(request, "Successful!!!")
                return redirect('transfer_status')
            
            return redirect('transfer_status')
    else:
        transaction_form = sending_moneyForm
                
    context = {
        'transaction_form':transaction_form,
    }
    return render(request, 'hi_hiApp/send-money.html', context)

def wallet(request):
    return render(request, 'hi_hiApp/wallet.html', None)

def welcome(request):
    return render(request, 'hi_hiApp/welcome.html', None)

def dashboard(request):
    card_details = users_wallet.objects.all().filter(user=request.user)
    transaction_history = transaction.objects.all().filter(Sender=request.user)
    context = {
        'card_details':card_details,
        'transaction_history':transaction_history,
    }
    return render(request, 'hi_hiApp/dashboard.html', context)

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.phone_number = form.cleaned_data.get("phone_number")
            user.save()
            
            # creating required Authentication credentials
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('welcome')
    else:
        form = signupForm()
    return render(request, 'registration/sign-up.html', {'form':form})
    
def logoutUser(request):
    logout(request)
    return redirect("login")


