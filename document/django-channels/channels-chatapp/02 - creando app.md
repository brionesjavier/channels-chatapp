ahora que el proyecto esta corriendo vamos a crear la aplicación para el chat , para ello ejecutemos el siguiente comando dentro de la carpeta `chatproject` y con el entorno activo

```python
	python manage.py startapp chat
```

luego tenemos que ir dentro de la carpeta `chatproject` y buscar el archivo  `settings.py` y buscamos la variable que se llama `INSTALLED_APPS` y agregamos la app que creamos recién 


```
# Application definition

  

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'chat'
	]
```

con eso la aplicación esta conectada ya al proyecto de igual manera se puede modificar la configuración desde ese archivo