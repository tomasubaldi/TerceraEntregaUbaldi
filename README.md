# Proyecto Web Django con patrón MVT

Este es un proyecto web creado con Django utilizando el patrón MVT. 

## Funcionalidades

- Herencia de HTML.
- Crear un modelo con 4 campos (atributos) de texto.
- Un formulario para insertar datos a de tu models.
- Un formulario para buscar algo en la base de datos y mostrar esos datos en un listado.

## Orden de pruebas

1. Asegurarse de tener Django instalado.
2. Clonar el repositorio desde GitHub.
3. Configurar la base de datos en settings.py.
4. Correr las migraciones con `python manage.py migrate`.
5. Crear un superusuario con `python manage.py createsuperuser`.
6. Correr el servidor con `python manage.py runserver`.
7. Visitar `http://localhost:8000/` para ver la lista de equipos musicales.
8. Visitar `http://localhost:8000/equipos_musicales/nuevo` para agregar un nuevo equipo musical.
9. Visitar `http://localhost:8000/equipos_musicales/buscar` para buscar un equipo musical.
