from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddMalePlayerForm, AddFemalePlayerForm
from .models import MalePlayer
from .models import FemalePlayer

def home(request):
	male_players = MalePlayer.objects.all()

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
		return render(request, 'home.html', {'male_players': male_players})

def jaguars(request):
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
		return render(request, 'jaguars.html', {'female_players': female_players})

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
		try:
			male_player_record = MalePlayer.objects.get(id=pk)
			image_path = 'images/client.jpg'
			return render(request, 'male_player_record.html', {'male_player_record': male_player_record})
		except MalePlayer.DoesNotExist:
			messages.error(request, "Male Player does not exist.")
	else:
		messages.success(request, "You Must Be Logged In To View The Player!")
	return redirect('home')

def female_player_record(request, pk):
	if request.user.is_authenticated:
		try:
			female_player_record = FemalePlayer.objects.get(id=pk)
			image_path = 'images/client.jpg'
			return render(request, 'female_player_record.html', {'female_player_record': female_player_record})
		except FemalePlayer.DoesNotExist:
			messages.error(request, "Female Player does not exist.")
	else:
		messages.success(request, "You Must Be Logged In To View The Player!")
	return redirect('home')


def delete_male_player(request, pk):
	if request.user.is_authenticated:
		try:
			delete_mpl = MalePlayer.objects.get(id=pk)
			if request.method == 'POST':
				delete_mpl.delete()
				messages.success(request, "Male Player Deleted Successfully!")
				return redirect('home')
			else:
				return render(request, 'confirm_delete.html', {'player': delete_mpl})
		except MalePlayer.DoesNotExist:
			messages.error(request, "Player does not exist.")
	else:
		messages.success(request, "You Must Be Logged In To Delete A Player.")
	return redirect('home')

def delete_female_player(request, pk):
    if request.user.is_authenticated:
        try:
            delete_fpl = FemalePlayer.objects.get(id=pk)
            if request.method == 'POST':
                delete_fpl.delete()
                messages.success(request, "Female Player Deleted Successfully!")
                return redirect('jaguars')
            else:
                return render(request, 'confirm_delete.html', {'player': delete_fpl})
        except FemalePlayer.DoesNotExist:
            messages.error(request, "Female Player does not exist.")
    else:
        messages.success(request, "You Must Be Logged In To Delete A Player.")
    return redirect('jaguars')


def add_male_player(request):
	form = AddMalePlayerForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
                # Check the gender value from the form
				gender = form.cleaned_data['gender']
				if gender == 'Male' or gender == "M":
					male_player = form.save(commit=False)
					male_player.save()
					messages.success(request, "Male Player Added Successfully!")
				else:
					messages.error(request, "Invalid gender value, must be Male or M")
					return redirect('home')
		else:
            # Set the default value for the gender field
			form.fields['gender'].initial = 'M'
		return render(request, 'add_male_player.html', {'form': form})
	else:
		messages.success(request, "You Must Be Logged In To Add A Male Player.")
		return redirect('home')

def add_female_player(request):
	form = AddFemalePlayerForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
                # Check the gender value from the form
				gender = form.cleaned_data['gender']
				if gender == 'Female' or gender == 'F':
					female_player = form.save(commit=False)
					female_player.save()
					messages.success(request, "Female Player Added Successfully!")
				else:
					messages.error(request, "Invalid gender value, must be Female or F")
					return redirect('home')
		else:
            # Set the default value for the gender field
			form.fields['gender'].initial = 'M'
		return render(request, 'add_female_player.html', {'form': form})
	else:
		messages.success(request, "You Must Be Logged In To Add A Female Player.")
		return redirect('home')

def update_male_player(request, pk):
	if request.user.is_authenticated:
		try:
			current_player = MalePlayer.objects.get(id=pk)
			form = AddMalePlayerForm(request.POST or None, instance=current_player)
			if form.is_valid():
				gender = form.cleaned_data['gender']
				if gender == 'Male' or gender == 'M':
					male_player = form.save(commit=False)
					male_player.save()
					messages.success(request, "Male Player Updated Successfully!")
				else:
					messages.error(request, "Invalid gender value, must be Male or M")
				return redirect('home')
			return render(request, 'update_male_player.html', {'form': form})
		except Player.DoesNotExist:
			messages.error(request, "Male Player does not exist.")
	else:
		messages.success(request, "You Must Be Logged In To Update A Male Player.")
	return redirect('home')

def update_female_player(request, pk):
	if request.user.is_authenticated:
		try:
			current_player = FemalePlayer.objects.get(id=pk)
			form = AddFemalePlayerForm(request.POST or None, instance=current_player)
			if form.is_valid():
				gender = form.cleaned_data['gender']
				if gender == 'Female' or gender == 'F':
					female_player = form.save(commit=False)
					female_player.save()
					messages.success(request, "Female Player Updated Successfully!")
				else:
					messages.error(request, "Invalid gender value, must be Female or F")
				return redirect('jaguars')
			return render(request, 'update_female_player.html', {'form': form})
		except FemalePlayer.DoesNotExist:
			messages.error(request, "Player does not exist.")
	else:
		messages.success(request, "You Must Be Logged In To Update A Female Player.")
	return redirect('home')

def search_male_player(request):
    # query = request.GET.get('query')
    # players = MalePlayer.objects.filter(name__icontains=query) if query else MalePlayer.objects.all()
    # # Rest of your code
	query = request.GET.get('query')
	if query:
        # Perform case-insensitive search on fields you want to search
		male_players = MalePlayer.objects.filter(
            # gender='Male',
            first_name__icontains=query
			# last_name__icontains=query
            # Add more fields as needed for the search
        )
		context = {'male_players': male_players, 'query': query}
		return render(request, 'home.html', context)
	else:
        # Handle the case where no search query is provided
		return render(request, 'home.html')

def search_female_player(request):
    # query = request.GET.get('query')
    # players = FemalePlayer.objects.filter(name__icontains=query) if query else FemalePlayer.objects.all()
    # # Rest of your code
	query = request.GET.get('query')
	if query:
        # Perform case-insensitive search on fields you want to search
		female_players = FemalePlayer.objects.filter(
            gender='Female',
            first_name__icontains=query,
			last_name__icontains=query
            # Add more fields as needed for the search
        )
		context = {'female_players': female_players, 'query': query}
		return render(request, 'jaguars.html', context)
	else:
        # Handle the case where no search query is provided
		return render(request, 'jaguars.html')
