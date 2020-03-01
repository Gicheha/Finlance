from ckeditor.widgets import CKEditorWidget
from django import forms
from customer.models import *
from indexapp.constants import COMPANY_SIZES


class DateInput(forms.DateInput):
    input_type = 'date'


class RichEditor(forms.Form):
    content = forms.CharField(widget=CKEditorWidget(attrs={'class':'form-control'}))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['accept_policy'].widget.attrs['class'] = ''
        self.fields['business_name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['contact_person_name'].widget.attrs['placeholder'] = 'contact_person_name'
        self.fields['company_size'].widget.attrs['placeholder'] = 'Company Size'
        self.fields['country'].widget.attrs['placeholder'] = 'Country'

    password1 = forms.CharField(min_length=8, max_length=100,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'password'}))
    password2 = forms.CharField(min_length=8, max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'repeat password'}))
    accept_policy = forms.BooleanField(widget=forms.CheckboxInput())

    def clean_password(self):
        pw1 = self.cleaned_data.get('password1')
        pw2 = self.cleaned_data.get('password2')
        if pw1 and pw2 and pw1 == pw2:
            return pw2
        else:
            return True


class UpdateCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(UpdateCustomer, self).__iter__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['business_name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['contact_person_name'].widget.attrs['placeholder'] = 'contact_person_name'
        self.fields['company_size'].widget.attrs['placeholder'] = 'Company Size'
        self.fields['country'].widget.attrs['placeholder'] = 'Country'


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['hiring_organization', 
                    'title',
                    'job_location',
                    'job_level',
                    'date_posted',
                    'valid_through',
                    'employment_type',
                    'category',
                    'experience',
                    'education_level',
                    'max_salary',
                    'min_salary',
                    'description'
                ]

        widgets = {
            'date_posted' : DateInput(),
            'valid_through' : DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['hiring_organization'].widget.attrs['placeholder'] = 'hiring organization'
        self.fields['title'].widget.attrs['placeholder'] = 'e.g Finance Analyst'
        self.fields['job_location'].widget.attrs['placeholder'] = 'Job  Location'
        self.fields['job_level'].widget.attrs['placeholder'] = 'Job Level'
        self.fields['date_posted'].widget.attrs['placeholder'] = 'Date Posted'
        self.fields['valid_through'].widget.attrs['placeholder'] = 'Application Deadline'
        self.fields['employment_type'].widget.attrs['placeholder'] = 'Employment Type'
        self.fields['category'].widget.attrs['placeholder'] = 'Job Category'
        self.fields['experience'].widget.attrs['placeholder'] = 'Required Experience'
        self.fields['education_level'].widget.attrs['placeholder'] = 'Required Education'
