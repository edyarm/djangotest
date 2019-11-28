# djangotest

Proyecto creado con django, djangorestframework

Esta proyecto contiene una app que ofrece un API REST para realizar el CRUD sobre las tablas Professor, Student y Score, también ofrece para un usuario interno con la 

![djangotest](../master/screenshot.PNG)

## Pre requisitos
1. Python 3.X
2. Postgres
3. Django==2.2.7 
4. django-filter==2.2.0
5. djangorestframework==3.10.3
6. psycopg2==2.8.4
 
## Instalación
1. Clonar el repositorio
2. Configurar los valores de DATABASES en el archivo djangotest\settings.py
    a. NAME: Nombre de la base de datos
    b. USER: Usuario de la base de datos
    c. PASSWORD: Contraseña de la base de datos
    d. HOST: Host de la base de datos
    e. PORT: Puerto de la base de datos
3. Ejecutar manage.py migrate

## Ejecutar aplicación
1. Ejecutar manage.py runserver