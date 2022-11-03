# mi-proyecto-final
Nuestro MVT Django

Entrega intermedia del Proyecto Final de Python de Coderhouse.

En esta entrega de MVT se podrá visualizar código de Python en Django de:

- Vistas
- Formularios
- Modelos 
    - Familiares
    - Configuracion: Para seteo de nombre_blog, titulo_principal, subtitulo_principal
- Templates
    - buscar.html: es nuestra página de inicio para buscar familiares.
    - alta_familiar.html: es nuestra página para la creación de familiares.
- Herencia
    - base.html: es nuestra extensión de página para estilos para todas nuestras páginas; donde utiliza el modelo Configuracion (para los datos básicos de información del blog); más la definición de CSS.


Importante: Este ejemplo fue probado con Python 3.10.6 y Django 4.1.2.

Checklist de Validación:
1. Para comenzar tienen que asegurarse que tienen instalado: Python.

En windows tiene que abrir una terminal cmd o powershell.

`
PS C:\> python --version
Python 3.X.X 
En Linux/Mac tiene que abrir una terminal bash

$ python --version
Python 3.X.X 
`

Si les aparece la versión todo OK pueden continuar. Caso contrario descarguen python desde este link.

2. Instalar django
En una terminal cmd o powershell desde windows:
`
C:\> pip install django
Linux/Mac:

$ pip install django
`
Si no arrojo errores esto es suficiente para poder correr el projecto.

3. Instalar Django bootstrap v5
`
C:\> pip install django-bootstrap-v5
Linux/Mac:

$ pip install django-bootstrap-v5
`

4. Correr el Servidor
Los siguinetes comandos son analogos en Mac/Linux/Windows:
`
cd mi-primer-mvt
python manage.py migrate
`
La consola mostrara las migraciones de la base de datos que se realizaron.

5. Luego iniciamos el servidor web
`
python manage.py runserver
`

Listo, estás en condiciones de ejecutar el ejemplo.
 
Para poder visualizar el material debés hacer click en el siguiente link:
http://127.0.0.1:8000/mi-familia/buscar