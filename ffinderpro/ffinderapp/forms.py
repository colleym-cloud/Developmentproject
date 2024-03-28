from profile import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PlayerProfile, TeamProfile, Listing, CustomUser


class SignUpForm(UserCreationForm):
    USER_CHOICES = (
        ('player', 'Player'),
        ('team', 'Team'),
    )
    registration_type = forms.ChoiceField(choices=USER_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class PlayerSignUpForm(UserCreationForm):
    date_of_birth = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        help_text='Enter your date of birth'
    )
    address = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=False)
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'date_of_birth', 'address', 'city', 'photo']


class TeamSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    location = forms.CharField(max_length=255)
    league = forms.CharField(max_length=100)
    league_division = forms.CharField(max_length=50)
    level_on_pyramid = forms.CharField(max_length=50)
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'name', 'location', 'league', 'league_division', 'level_on_pyramid', 'photo', ]


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'positions', 'location', 'photo']


class ProfileUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        help_text='Enter your date of birth'
    )
    class Meta:
        model = PlayerProfile
        fields = ['date_of_birth', 'address', 'city', 'photo']

class PlayerProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        help_text='Enter your date of birth'
    )
    class Meta:
        model = CustomUser
        fields = ['photo']
 
class TeamProfileForm(forms.ModelForm):
    class Meta:
        model = TeamProfile
        fields = ['name', 'location', 'league', 'league_division', 'level_on_pyramid', 'photo']