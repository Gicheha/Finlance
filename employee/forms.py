from django import forms
from employee.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class SignUpForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        exclude = ['user', 'country', 'city', 'profile_pic', 'status', 'is_suspended']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'single-input'

        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['id_number'].widget.attrs['placeholder'] = 'National ID Number'
        self.fields['email'].widget.attrs['placeholder'] = 'email'

    password1 = forms.CharField(min_length=8, 
                                max_length=100,
                                widget=forms.PasswordInput(attrs={'class': '', 'placeholder': 'password'}))
    password2 = forms.CharField(min_length=8,
                                max_length=100,
                                widget=forms.PasswordInput(attrs={'class': '', 'placeholder': 'repeat password'}))

    def clean_password(self):
        pw1 = self.cleaned_data.get('password1')
        pw2 = self.cleaned_data.get('password2')
        if pw1 and pw2 and pw1 == pw2:
            return pw2
        else:
            pw2 = None
            return pw2


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        exclude = ['user', 'email', 'is_suspended']

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'single-input'
        self.fields['profile_pic'].widget.attrs['id'] = 'profile-pic'


class UpdateEducation(forms.ModelForm):
    class Meta:
        model = EmployeeEducation
        exclude = ['user']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(UpdateEducation, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'single-input'
            field.widget.attrs['type'] = 'date'


class UpdateExperience(forms.ModelForm):
    class Meta:
        model = EmployeeExperience
        exclude = ['user']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(UpdateExperience, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'single-input'

        self.fields['current_job'].widget.attrs['class'] = ''


class UpdateEmployeeProficiency(forms.ModelForm):
    class Meta:
        model = EmployeeProficiency
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(UpdateEmployeeProficiency, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'single-input'


class UpdateResume(forms.ModelForm):
    class Meta:
        model = EmployeeResume
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(UpdateResume, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'single-input'


class UpdateLanguage(forms.ModelForm):
    class Meta:
        model = EmployeeLanguage
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(UpdateLanguage, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'single-input'

