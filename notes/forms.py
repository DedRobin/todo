from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )


class AddNoteForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(max_length=1000, widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label='Username')
    password = forms.CharField(max_length=255, widget=forms.PasswordInput())
