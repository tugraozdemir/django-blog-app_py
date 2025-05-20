
# 🏢 Django Blog Projesi

Bu proje, Django framework kullanılarak geliştirilmiş, kullanıcıların kayıt olabildiği, giriş yapabildiği ve yönetici paneli üzerinden blog içeriklerinin düzenlenebildiği bir blog uygulamasıdır.

## 🚀 Özellikler

- Kullanıcı kayıt / giriş / çıkış işlemleri
- Blog yazıları oluşturma, düzenleme ve silme
- Admin paneli üzerinden içerik yönetimi
- Bootstrap ile responsive (mobil uyumlu) tasarım
- SQLite veritabanı desteği
- Temiz ve modüler yapı

## 🔧 Kullanılan Teknolojiler ve Kütüphaneler

- **Backend:** Python 3, Django
- **Frontend:** HTML5, CSS3, Bootstrap 4/5
- **Veritabanı:** SQLite
- **Kütüphaneler:**
  - `django-crispy-forms` *(isteğe bağlı)*
  - `python-decouple` *(ortam değişkenleri için)*

## 🧩 Proje Yapısı

```
django-blog-app/
├── article/            # Blog yazıları için uygulama
├── user/               # Kullanıcı yönetimi (login, register)
├── static/             # CSS, JS, görseller
├── templates/          # HTML şablonları
├── django_blog_app/    # Ayarlar ve URL yönlendirmeleri
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## ⚙️ Kurulum

Aşağıdaki adımları izleyerek projeyi kendi bilgisayarınızda çalıştırabilirsiniz:

```bash
# 1. Repoyu klonla
git clone https://github.com/tugraozdemir/django-blog-app_py.git
cd django-blog-app_py

# 2. Sanal ortam oluştur ve etkinleştir
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)

# 3. Gereksinimleri yükle
pip install -r requirements.txt

# 4. Veritabanını oluştur ve migrasyonları uygula
python manage.py makemigrations
python manage.py migrate

# 5. Süper kullanıcı oluştur
python manage.py createsuperuser

# 6. Sunucuyu başlat
python manage.py runserver
```

## 🔐 Admin Panel Girişi

- **URL:** http://127.0.0.1:8000/admin
- **Kullanıcı Adı / Şifre:** Kurulum sırasında belirlenir.

## 🤝 Katkı

Proje açık kaynaklıdır. Her türlü katkı, öneri ve geri bildirim memnuniyetle karşılanır. PR (Pull Request) veya Issue açabilirsiniz.

---

© 2025 Tuğra Özdemir – [GitHub](https://github.com/tugraozdemir)
