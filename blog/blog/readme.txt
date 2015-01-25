This code enables the user to see all the blogs after signing up. login option is also on the page.
Complete details are in settings.py 
Other important details are-
http://127.0.0.1:8000  is the opening link of the site.
url for signup-> /signup
the port numbers are-
mysql ->  3306
applicatn-> 8000
the user can only enter data by entering it in the database.
Database details-
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',
        'PORT' : '3306'
                
        

    }
}
Imp- you can only run my entering the name "myblog", otherwise change it before hand.