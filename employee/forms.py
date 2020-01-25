from django import forms
from employee.models import *


class SignUpForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        exclude = ['user', 'country', 'city', 'profile_pic', 'status','is_suspended']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args,**kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['id_number'].widget.attrs['placeholder'] = 'National ID Number'
        self.fields['email'].widget.attrs['placeholder'] = 'email'

    accept_policy = forms.BooleanField(widget=forms.CheckboxInput())
    password1 = forms.CharField(min_length=8, max_length=100,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(min_length=8, max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'repeat password'}))

    def clean_password(self):
        pw1 = self.cleaned_data.get('password1')
        pw2 = self.cleaned_data.get('password2')
        if pw1 and pw2 and pw1 == pw2:
            return pw2
        else:
            return True


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        exclude = ['user', 'email', 'is_suspended']

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['profile_pic'].widget.attrs['id'] = 'profile-pic'


class UpdateEducation(forms.ModelForm):
    class Meta:
        model = EmployeeEducation
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(UpdateEducation, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UpdateExperience(forms.ModelForm):
    class Meta:
        model = EmployeeExperience
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(UpdateExperience, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['current_job'].widget.attrs['class'] = ''


class UpdateEmployeeProficiency(forms.ModelForm):
    class Meta:
        model = EmployeeProficiency
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(UpdateEmployeeProficiency, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UpdateResume(forms.ModelForm):
    class Meta:
        model = EmployeeResume
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(UpdateResume, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UpdateLanguage(forms.ModelForm):
    class Meta:
        model = EmployeeLanguage
        exclude = ['user']

    def __init__(self,*args,**kwargs):
        super(UpdateLanguage, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

