Tworzenie wirtualnego środowiska uruchomieniowego pythona

python -m venv venv

Windows: .\venv\Scripts\activate
Ubuntu: source venv/bin/activate
Mac: pip install virtualenv 
     source venv/bin/activate

(venv) ścieżka
Albo: pip install django==4.2.0
Albo: Plik requirements.txt 
pip install -r requirements.txt

Sprawdzenie
python
import django
print(django.get_version())
4.2

Utworzenie projektu 
django-admin startproject myapp

Weryfikacja myapp z plikiem manage.py w srodku. 

cd myapp
python manage.py check

https://docs.djangoproject.com/en/4.2/