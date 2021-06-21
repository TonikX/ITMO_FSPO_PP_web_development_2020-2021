# Формы

Указанные в формах поля аналогичны полям моделей базы данных. Все формы написаны по одному и тому же принципу, поэтому будет описаны лишь некоторые формы

    class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = [
            "district",
            "street"
        ]

Базовая форма

    class CreateInspectorForm(UserCreationForm):
    class Meta:
        username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
        password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        servNumb = forms.CharField(label='Service number', widget=forms.TextInput(attrs={'class': 'form-input'}))
        last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-input'}))
        first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'form-input'}))
        patronymic = forms.CharField(label='Patronymic', widget=forms.TextInput(attrs={'class': 'form-input'}))
        phone = forms.CharField(label='Phone number', widget=forms.TextInput(attrs={'class': 'form-input'}))
        model = Inspector
        fields = ('username', 'password1', 'password2', 'servNumb', 'last_name', 'first_name', 'patronymic', 'phone', 'is_staff', 'is_superuser')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
            'servNumb': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-input'})
        }

В первых 9 строчках описываются поля формы, указанные в `fields`. В `widgets` формируется вид полей формы


    class LoginInspectorForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'})),
    servNumb = forms.CharField(label='Service number', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


Данная форма является формой входа и наследуется от уже определённой в Django формы `AuthenticationForm`. В данной форме фигурируют базовые поля логина и пароля, а также поле `servNumb` из модели `Inspector`
