from socket import fromshare
from django import forms
from django.forms.widgets import NumberInput,SelectDateWidget
class SampleForm(forms.Form):  
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982', '1983', '1984', '1985']  
    Choice_value = [('1', 'First'), ('2', 'Second'), ('3', 'Third')] 
    GENDER_CHOICES = [  
    ('male', 'Male'),  
    ('female', 'Female'),  
    ('other', 'Other'),  
]   
    first_name = forms.CharField(max_length=50)  
    last_name = forms.CharField(max_length=50)  
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))                         
    email = forms.EmailField()  
    date_of_birth = forms.DateField(widget = NumberInput(attrs={'type':'date'}))  
    #date_of_birth = forms.DateField(widget = SelectDateWidget(years=BIRTH_YEAR_CHOICES))  
    value = forms.DecimalField(required=True)  
    agree = forms.BooleanField() 
    rank = forms.ChoiceField(choices=Choice_value)
    rank = forms.ChoiceField(widget = forms.RadioSelect, choices=Choice_value)   
    gender = forms.ChoiceField(choices=GENDER_CHOICES)    