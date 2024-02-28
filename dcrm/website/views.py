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

def bu_player(request, pk):
    if request.user.is_authenticated:
        try:
            bu_player = MalePlayer.objects.get(id=pk)
            return render(request, 'bu_player.html', {'bu_player': bu_player})
        except Player.DoesNotExist:
            try:
                female_player = FemalePlayer.objects.get(id=pk)
                return render(request, 'bu_player.html', {'bu_player': female_player})
            except FemalePlayer.DoesNotExist:
                messages.error(request, "Player does not exist.")
    else:
        messages.success(request, "You Must Be Logged In To View The Player!")
    return redirect('home')


def delete_player(request, pk):
    if request.user.is_authenticated:
        try:
            delete_pl = MalePlayer.objects.get(id=pk)
            delete_pl.delete()
            messages.success(request, "Player Deleted Successfully!")
        except Player.DoesNotExist:
            try:
                delete_pl = FemalePlayer.objects.get(id=pk)
                delete_pl.delete()
                messages.success(request, "Player Deleted Successfully!")
            except FemalePlayer.DoesNotExist:
                messages.error(request, "Player does not exist.")
    else:
        messages.success(request, "You Must Be Logged In To Delete A Player.")
    return redirect('home')


def add_player(request):
    form1 = AddPlayerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                # Check the gender value from the form
                gender = form.cleaned_data['gender']
                if gender == 'Male':
                    player = form.save(commit=False)
                    player.save()
                    messages.success(request, "Male Player Added Successfully!")
                elif gender == 'Female':
                    female_player = form.save(commit=False)
                    female_player.save()
                    messages.success(request, "Female Player Added Successfully!")
                else:
                    messages.error(request, "Invalid gender value")
                return redirect('home')
        return render(request, 'add_player.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In To Add A Player.")
        return redirect('home')

def update_player(request, pk):
    if request.user.is_authenticated:
        try:
            current_player1 = MalePlayer.objects.get(id=pk)
			current_player2 = FemalePlayer.objects.get(id=pk)
            form = AddPlayerForm(request.POST or None, instance=current_player)
            if form.is_valid():
                gender = form.cleaned_data['gender']
                if gender == 'Male':
                    player = form.save(commit=False)
                    player.save()
                    messages.success(request, "Male Player Added Successfully!")
                elif gender == 'Female':
                    female_player = form.save(commit=False)
                    female_player.save()
                    messages.success(request, "Female Player Added Successfully!")
                else:
                    messages.error(request, "Invalid gender value")
                return redirect('home')
            return render(request, 'update_player.html', {'form': form})
        except Player.DoesNotExist:
            try:
                current_player = FemalePlayer.objects.get(id=pk)
                form = AddPlayerForm(request.POST or None, instance=current_player)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Player Updated Successfully!")
                    return redirect('home')
                return render(request, 'update_player.html', {'form': form})
            except FemalePlayer.DoesNotExist:
                messages.error(request, "Player does not exist.")
    else:
        messages.success(request, "You Must Be Logged In To Update A Player.")
    return redirect('home')


