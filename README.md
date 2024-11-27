# BINARIO2

Este es el proyecto BINARIO2, un sitio web que ofrece servicios, proyectos y una página de contacto. El proyecto está construido con Django y utiliza Bootstrap para el diseño y Toastr para las notificaciones.

## LAS IMAGENES SON ILUSTRATIVAS, SALVO LAS IMAGENES QUE SE CARGAN DESDE LA BASE DE DATOS EN PROYECTOS!

## Requisitos

- Python 3.x
- Django 3.x
- Bootstrap 5.3.0
- Toastr

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/binario2.git
    cd binario2
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

5. Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

6. Abre tu navegador y navega a `http://127.0.0.1:8000/` para ver el sitio en funcionamiento.

## Estructura del Proyecto

- **binario2/**: Directorio del proyecto principal.
  - **settings.py**: Configuración del proyecto.
  - **urls.py**: Definición de las rutas del proyecto.
  - **wsgi.py**: Configuración para el servidor WSGI.
  - **asgi.py**: Configuración para el servidor ASGI.
- **app/**: Directorio de la aplicación principal.
  - **migrations/**: Migraciones de la base de datos.
  - **static/**: Archivos estáticos (CSS, JS).
  - **templates/**: Plantillas HTML.
    - **base.html**: Plantilla base que incluye Bootstrap y Toastr.
    - **detalle_servicio.html**: Plantilla para mostrar los detalles de un servicio.
    - **contacto.html**: Plantilla para la página de contacto con un formulario y notificaciones Toastr.
    - **servicios.html**: Plantilla para la lista de servicios.
    - **proyectos.html**: Plantilla para la lista de proyectos.
  - **admin.py**: Configuración del administrador de Django.
  - **apps.py**: Configuración de la aplicación.
  - **forms.py**: Definición de formularios.
  - **models.py**: Definición de modelos de datos.
  - **tests.py**: Pruebas unitarias.
  - **views.py**: Definición de vistas.
- **manage.py**: Script de gestión de Django.
- **requirements.txt**: Archivo de dependencias del proyecto.

```plaintext
binario2/
├── binario2/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── app/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   ├── templates/
│   │   ├── base.html
│   │   ├── detalle_servicio.html
│   │   ├── contacto.html
│   │   ├── servicios.html
│   │   ├── proyectos.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── [manage.py](http://_vscodecontentref_/0)
└── [requirements.txt](http://_vscodecontentref_/1)



## Uso de Toastr

Toastr se utiliza para mostrar notificaciones en el sitio. Aquí hay un ejemplo de cómo se configura en `base.html`:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>
<script>
    toastr.options = {
        "closeButton": true,
        "debug": false,
        "newestOnTop": false,
        "progressBar": true,
        "positionClass": "toast-top-right",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    }
</script>
