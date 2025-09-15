comenzamos por crear un entorno virtual con virtualenv

```bash
virtualenv venv
```
activamos el entorno virtual

```bash
source venv/bin/activate
```

creamos un archivo llamado requirements.txt
pip install daphne


```requirements.txt
# Este es el archivo de dependencias para mi proyecto Django
Django==5.2.6  # Framework principal
daphne==4.2.1  # Servidor ASGI para Django Channels
channels==4.3.1  # WebSockets con Django
```

ahora la instalamos con el siguiente comando

```shell
pip install -r requirements.txt
```

