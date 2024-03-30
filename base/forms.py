from django import forms
from .models import CustomerModel, ReviewModel
class AddressForm(forms.ModelForm):
    class Meta:
        model=CustomerModel
        fields = ['fname', 'lname', 'areacode', 'phone', 'address', 'zipcode']
        exclude = ['username']
        labels = {'fname':'First Name',
                  'lname':'Last Name',
                  'areacode':'Area Code',
                  'phone':'Phone',
                  'address':'Address',
                  'zipcode':'Zipcode'}
        

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = [ 'name', 'title', 'review', 'rating']
        exclude = ['username', 'titleproduct', 'date']
        labels = {
            'name':'Name',
            'title': 'Title',
            'review':'Review',
            'rating':'Rating'
        }
        widgets = {
         'name':forms.TextInput(attrs={'autofocues':True, 'class':'form-control'}),
         'title':forms.TextInput(attrs={'autofocues':True, 'class':'form-control'}),
         'review':forms.TextInput(attrs={'autofocues':True, 'class':'form-control'}),
         'rating':forms.NumberInput(attrs={'autofocues':True, 'class':'form-control', 'placeholder':'rate from 0-5'}),
         }
