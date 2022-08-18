from django import forms


class AddNoteForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(max_length=1000, widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label='Username')
    password = forms.CharField(max_length=255, widget=forms.PasswordInput())
