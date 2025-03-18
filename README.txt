Hay que crear un Virtual enviroument. Para esto hay que correr el siguiente comando en la carpeta raiz:
    py -m venv venv

Luego, activar el enviroument con el comando
    venv\Scripts\activate

Una vez activado instalar django y pillow:
    pip install -r requirements.txt

    python.exe -m pip install --upgrade pip

    python -m pip install Pillow

Instalar pylint:
    pip install pylint-django

Para activar pylint:
    1) ir a archivo
    2) Preferencias/configuración
    3) Buscar pylintArgs en el buscador
    4) En python.linting.pylintArgs tocar agregar elemenots
        a) "pylint.args": ["--errors-only"]
        b) "pylint.args": ["--load-plugins"]
        c) "pylint.args": ["--pylint_django"]


Dirigirnos a:
    cd webpersonal

Levantar el proyecto con:
    python manage.py runserver



Correr migraciones:

Ejecutar: 
    python manage.py makemigrations <nombre de la carpeta a migrar>

    ejemplo: python manage.py makemigrations about_me

Luego correr:
    python manage.py migrate <nombre de la carpeta a migrar>


