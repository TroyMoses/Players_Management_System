from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddMalePlayerForm, AddFemalePlayerForm
from .models import MalePlayer, FemalePlayer

def home(request):
	male_players = MalePlayer.objects.all()
	female_players = FemalePlayer.objects.all()

    # Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

        # Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, 'You have successfully logged in')
			return redirect('home')
		else:
			messages.success(request, 'Error logging in - please try again')
			return redirect('home')
	else:
		return render(request, 'home.html', {'players': male_players, 'female_players': female_players})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def male_player_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		male_player_record = MalePlayer.objects.get(id=pk)
		return render(request, 'male_player.html', {'male_player_record':male_player_record})
	else:
		messages.success(request, "You must be logged in to view that page...")
		return redirect('home')

def delete_player(request, pk):
	if request.user.is_authenticated:
		delete_it = Player.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Player deleted successfully...")
		return redirect('home')
	else:
		messages.success(request, "You must be logged in to delete a player...")
		return redirect('home')


def add_male_player(request):
	form = AddPlayerForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_male_player = form.save()
				messages.success(request, "Male Player added successfully")
				return redirect('home')
		return render(request, 'add_male_player.html', {'form':form})
	else:
		messages.success(request, "You must be logged in to add a player...")
		return redirect('home')


def update_male_player(request, pk):
	if request.user.is_authenticated:
		current_player_record = MalePlayer.objects.get(id=pk)
		form = AddMalePlayerForm(request.POST or None, instance=current_player_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Player updated successfully!")
			return redirect('home')
		return render(request, 'update_male_player.html', {'form':form})
	else:
		messages.success(request, "You must be logged in to update a player...")
		return redirect('home')

