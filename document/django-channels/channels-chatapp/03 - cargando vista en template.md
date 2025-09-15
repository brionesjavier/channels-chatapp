ahora que tenemos la app configurada en `setting` vamos a crear un template básico para mostrar un mensaje para ello vamos a:
	- crear una vista
	- configurar el url
	- crear un template

primero en la app que creamos vamos a crear un archivo `urls.py`

```python
#chat/urls.py
from django.urls import path
from chat.views import Main


urlpatterns = [
	path('', Main.as_view() ,name='main')
]
```

ahora vamos al archivo que de `urls.py` que esta  en `chatproject` dejándolo así

```python
#chatproject/urls.py
from django.contrib import admin
from django.urls import path, include

  

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('chat.urls'))
]
```

ahora vamos a crear un paquete de `views` para tenerlo separados y que sea modular:
-creamos una carpeta llamada `views` dentro de la carpeta agregamos un archivo `__init__.py` y un archivo `main.py` , dentro del archivo 

```python
#views/__init__.py
from .main import Main


__all__ = [
	Main,
]
```
ya con el  archivo creado vamos a `main.py`

```python
#views/main.py
from django.views import View
from django.shortcuts import render


class Main(View):
	def get(self, request):
	return render(request,template_name='chat/main.html')
```

ahora vamos a crear la carpeta de `template` en la carpeta de app que se llama chat
y lo vamos a separar creando otra carpeta llamada chat y dentro de esta carpeta va a estar  `main.html`

pero antes vamos a crear la carpeta de templates y dentro de esta va a estar chat y img para las imagenes que vamos a ocupar

```django

{% load static %} <!-- cargamos los archivo estaticos-->

<!DOCTYPE html>

<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">

	<title>Main page</title>
	
	<style>
	
		body{
			padding: 0;
			margin: 0;
			border: 0;
			background-color: brown;
		}
	
		a{
			text-decoration: none;
		}
	
		main{
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;
			padding: 25px;
		}
	
		main h1{
			font-size: 35px;
			color: rgb(255, 255, 255);
			font-weight: bold;
			text-align: center;
			margin: 25px;
		}
	
		main img{
			width: 200px;
			height: 200px;
			margin: 25px;
			padding: 25px;
			background-color: rgb(255, 255, 255);
			border-radius: 25px;
			box-shadow: 0 0 25px 2.5px rgb(255, 255, 255);
		}
	
		main div button{
			width: 200px;
			height: 50px;
			margin: 25px;
			background-color: rgb(47,177,212);
			border: 0;
			border-radius: 10px;
			color: rgb(255, 255, 255);
			font-weight: 600;
			font-size: 15px;
			box-shadow: 0 0 7px 0.1px rgb(255, 255, 255);
		}
	
		main div button:hover{
			background-color: rgb(113, 219, 248);
		}
	
		main div button:active{
			background-color: rgb(26, 146, 179);
		}
	
	</style>

</head>

<body>
	<main>
		<h1>The best chat application ever !!!</h1>
		<img src="{% static 'chat/img/chat.png' %}"> <!-- acedemos al archivo estatico-->
		<div>
			<a href="#register"><button>New Member</button></a>
			<a href="#login"><button>Old Member</button></a>
		</div>
	</main>
</body>

</html>
```

reiniciamos el servidor y probamos

ahora se puede probar en el navegador en la direccion 
```copy
http://127.0.0.1:8000/
```

