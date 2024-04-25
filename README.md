# Página de huertos
Pakal es una aplicación extremadamente sencilla en Django, montada para ejemplificar el despliegue en AWS de desarrollos con características similares. Al ingresar a su dirección asignada, el usuario podrá ver una lista de huertos registrados en la base de datos SQLite.

# Ejecución

Una vez clonado el repositorio, es necesario crear un entorno virtual en la raíz. Para esto, estando en una distribución de Linux, ejecute el siguiente comando:

```shell
python -m venv pyenv
```

Seguidamente, active el entorno:

```shell
source pyenv/bin/activate
```

Django es la única dependencia del proyecto. Se instala con el comando:

```shell
pip install Django
```

Finalmente, para ejecutar la aplicación, haga correr el servidor proporcionado por Django:

```shell
python manage.py runserver
```

Al ingresar a la dirección IP por defecto, http://127.0.0.1:8000/, se podrá visualizar la siguiente lista:

![Lista de huertos](https://i.ibb.co/nC7CcrH/image.png)