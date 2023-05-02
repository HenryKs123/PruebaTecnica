# PruebaTecnica
Prueba Tecnica para desarrollador en Python Cydenet
Henry Alejandro Roemro Mesa 
el framework es operado en django y el  motor de datos de  Bases de datos es postgres 
para realizar las migraciones se debe ejecutar los siguientes codigos 
pip install psycopg2
se modifican los siguienstes argumento  que se encuentran ubicados en la carpeta CidenetN/settings.py  en el apartado DATABASES 

acorde a la configuracion del posgret del usuario 

  'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Empleados',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'DATABASE': '5432',
    }
    
pytonh manage.py migrate
pytrhon manage.py makemigrations
python manage.py migrate 
