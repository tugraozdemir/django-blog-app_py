from django import forms
from django.contrib.auth.models import User # Kullanıcı adı zaten var mı kontrolü için

class LoginForm(forms.Form):
    # Crispy Forms düzgün çalışıyorsa widget'lara 'form-control' eklemek zorunlu değil
    # Ancak manuel kontrol için eklenebilir.
    username = forms.CharField(
        label = "Kullanıcı Adı",
        widget=forms.TextInput(attrs={'class': 'form-control'}) # Form kontrol sınıfını ekle
    )
    password = forms.CharField(
        label = "Parola",
        widget = forms.PasswordInput(attrs={'class': 'form-control'}) # Form kontrol sınıfını ekle
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length = 50,
        label = "Kullanıcı Adı",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=20,
        label = "Parola",
        widget = forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm = forms.CharField(
        max_length=20,
        label ="Parolayı Doğrula",
        widget = forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
    def clean_username(self): # Sadece kullanıcı adı alanını kontrol etmek için
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Bu kullanıcı adı zaten alınmış.")
        return username

    def clean(self):
        cleaned_data = super().clean() # Üst sınıfın clean metodunu çağır
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            self.add_error('confirm', "Parolalar eşleşmiyor.") # Belirli alana hata ekle

        # clean metodu her zaman tüm temizlenmiş veriyi döndürmelidir.
        # Bu kısım zaten doğru yapılmış gibi görünüyor, ancak emin olmak için:
        return cleaned_data # tüm cleaned_data'yı döndür