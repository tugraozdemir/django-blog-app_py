from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings # Ayarlardan LOGIN_REDIRECT_URL'i almak için

# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        # Kullanıcı adı zaten var mı kontrolü (forms.py'de de yapılmalıydı)
        # if User.objects.filter(username=username).exists(): # Artık forms.py'de de kontrol ediliyor
        #    messages.error(request, "Bu kullanıcı adı zaten alınmış.")
        #    return render(request, "register.html", {"form": form})

        newUser = User(username =username)
        newUser.set_password(password) # Şifreyi hashleyerek kaydeder
        newUser.save()

        # Kayıttan sonra otomatik giriş
        login(request, newUser) 
        messages.success(request, f"Hoş geldin {username}, başarıyla kayıt oldunuz!") # Daha bilgilendirici mesaj

        # LOGIN_REDIRECT_URL varsa oraya, yoksa 'index'e yönlendir
        return redirect(getattr(settings, 'LOGIN_REDIRECT_URL', 'index'))
    
    # Form geçerli değilse veya GET isteği ise
    # Crispy Forms hataları formun yanında gösterecektir, ancak genel bir hata mesajı da eklenebilir
    elif request.method == 'POST': # Eğer POST isteği ama form geçerli değilse
        messages.error(request, "Kayıt olurken bir hata oluştu. Lütfen bilgilerinizi kontrol edin.")

    context = {
        "form" : form
    }
    return render(request, "register.html", context)

   
def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }

    if request.method == 'POST': # Sadece POST isteklerini işle
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username = username, password = password) # request'i de authenticate'e geç

            if user is None:
                messages.error(request,"Kullanıcı Adı veya Parola Hatalı.") # Hata mesajı için messages.error
                return render(request,"login.html",context)

            messages.success(request,"Başarıyla Giriş Yaptınız.") # Başarılı giriş mesajı
            login(request,user)
            # LOGIN_REDIRECT_URL varsa oraya, yoksa 'index'e yönlendir
            return redirect(getattr(settings, 'LOGIN_REDIRECT_URL', 'index'))
        else: # Form geçerli değilse
            # Crispy forms hataları gösterecek, ancak genel bir hata mesajı da uygun olabilir
            messages.error(request, "Giriş bilgileriniz geçersiz. Lütfen tekrar deneyin.")

    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız.")
    # Çıkış sonrası nereye yönlendirileceği belirlenebilir, örn: ana sayfa
    return redirect(getattr(settings, 'LOGOUT_REDIRECT_URL', 'index'))