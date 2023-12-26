from django import forms
from .models import CustomUser

class RegistrationForm(forms.Form):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'phone_number', 'direction', 'event', 'password1', 'password2']

    
    full_name = forms.CharField(label='Полное имя', widget=forms.TextInput(attrs={'placeholder': 'Введите ваше полное имя', 'image_url': '/media/auth/user.svg'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'placeholder': 'Введите ваш e-mail', 'image_url': '/media/auth/email.svg'}))
    phone_number = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'placeholder': 'Введите ваш номер телефона', 'image_url': '/media/auth/phone.svg'}))
    
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'image_url': '/media/auth/password.svg'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль', 'image_url': '/media/auth/password.svg'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким e-mail уже зарегистрирован.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпадают.')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            print(f"Field name: {name}, Image URL: {field.widget.attrs.get('image_url')}")

