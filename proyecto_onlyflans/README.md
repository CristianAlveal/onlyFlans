# OnlyFlans 🍮

Aplicación web desarrollada con **Python y Django** para presentar un catálogo de flanes y gestionar el contacto con los clientes. El proyecto corresponde a una aplicación web de una empresa familiar de pastelería y postres llamada **OnlyFlans**, ubicada en Providencia, Santiago de Chile.

## 📌 Descripción del proyecto

OnlyFlans permite a los visitantes conocer los productos disponibles, revisar información sobre la empresa y enviar consultas mediante un formulario de contacto. También cuenta con una sección de acceso para usuarios autenticados y una vista para que el administrador consulte los mensajes recibidos.

## ✨ Funcionalidades principales

- **Catálogo público:** muestra los flanes marcados como públicos, con nombre, descripción e imagen.
- **Sección privada:** requiere iniciar sesión y permite acceder a la página de bienvenida.
- **Información de la empresa:** presenta la historia y ubicación de OnlyFlans.
- **Formulario de contacto:** valida y registra nombre, correo electrónico y mensaje.
- **Confirmación de envío:** muestra una página de confirmación tras enviar el formulario correctamente.
- **Administración de contactos:** el superusuario puede acceder a la lista de mensajes recibidos.
- **Panel de administración de Django:** permite administrar los registros de flanes y formularios de contacto.
- **Diseño adaptable:** utiliza componentes de Bootstrap para organizar el contenido en tarjetas y formularios.

## 🧰 Tecnologías utilizadas

- **Python**
- **Django**
- **SQLite** como base de datos configurada por defecto
- **HTML5**
- **CSS3**
- **Bootstrap** para el diseño de la interfaz
- **Sistema de autenticación de Django**

> La versión exacta de Python y Django dependerá del entorno utilizado. El proyecto incluye configuración de Django, pero no se encontró un archivo `requirements.txt` en el ZIP entregado.

## 📁 Estructura del proyecto

```text
proyecto_onlyflans/
├── manage.py
├── db.sqlite3
├── proyecto_onlyflans/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
├── web/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── contactDataForm.py
│   ├── views.py
│   ├── apps.py
│   └── tests.py
├── template/
│   ├── layout/
│   │   ├── base.html
│   │   ├── navbar.html
│   │   ├── header.html
│   │   └── footer.html
│   ├── index.html
│   ├── welcome.html
│   ├── about.html
│   ├── contacto.html
│   ├── exito.html
│   ├── lista_contactos.html
│   └── login.html
└── static/
    ├── css/
    │   └── style.css
    └── img/
        └── onlyflans.png
```

### Componentes relevantes

- `web/models.py`: define los modelos `Flan` y `ContactForm`.
- `web/contactDataForm.py`: contiene el formulario de contacto y sus campos.
- `web/views.py`: implementa las vistas del catálogo, bienvenida, información, contacto y listado de contactos.
- `web/admin.py`: registra los modelos en el administrador de Django.
- `proyecto_onlyflans/urls.py`: define las rutas de la aplicación.
- `template/layout/`: contiene la estructura compartida de las páginas.
- `static/`: almacena los estilos CSS y recursos gráficos.

## ⚙️ Requisitos previos

Antes de ejecutar el proyecto, instala:

- Python instalado en Windows.
- Visual Studio Code u otro editor de código.
- `pip`, el administrador de paquetes de Python.

Comprueba la instalación desde una terminal:

```bash
python --version
python -m pip --version
```

## 🚀 Instalación y ejecución

### 1. Descargar o clonar el repositorio

Si el proyecto ya está en tu equipo, abre la carpeta que contiene `manage.py` en Visual Studio Code.

Si está publicado en GitHub, clónalo con:

```bash
git clone URL_DEL_REPOSITORIO
cd proyecto_onlyflans
```

Reemplaza `URL_DEL_REPOSITORIO` por la dirección real del repositorio.

### 2. Crear y activar el entorno virtual

En Windows, desde la terminal de Visual Studio Code:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

Si utilizas la terminal CMD en lugar de PowerShell:

```bat
env\Scripts\activate.bat
```

### 3. Instalar Django

Como el ZIP entregado no incluye `requirements.txt`, instala Django en el entorno virtual:

```bash
python -m pip install django
```

Si el proyecto se ejecuta con una versión específica de Django en el entorno original, utiliza esa versión compatible. Para futuras entregas se recomienda mantener las dependencias en un archivo `requirements.txt`.

### 4. Aplicar migraciones

Desde la carpeta donde se encuentra `manage.py`, ejecuta:

```bash
python manage.py migrate
```

### 5. Crear un usuario administrador

Para acceder al panel de administración o probar las vistas restringidas, crea un superusuario:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones de la terminal para definir usuario, correo y contraseña.

### 6. Iniciar el servidor

```bash
python manage.py runserver
```

Abre el sitio en el navegador:

- Aplicación: http://127.0.0.1:8000/
- Inicio de sesión: http://127.0.0.1:8000/login/
- Administración: http://127.0.0.1:8000/admin/

Detén el servidor con `Ctrl + C`.

## 🗃️ Modelos de datos

### `Flan`

Representa un producto del catálogo y contiene los siguientes campos:

- `flan_uuid`: identificador UUID del flan.
- `name`: nombre del producto.
- `description`: descripción del producto.
- `image_url`: dirección de la imagen.
- `slug`: identificador legible para URL.
- `is_private`: indica si el flan es privado.

Los flanes con `is_private=False` se muestran en el catálogo público. Los que tienen `is_private=True` se consultan desde la vista de bienvenida, que requiere autenticación.

### `ContactForm`

Almacena los mensajes enviados desde el formulario de contacto:

- `contact_form_uuid`: identificador UUID generado automáticamente.
- `customer_email`: correo electrónico del cliente.
- `customer_name`: nombre del cliente.
- `message`: contenido del mensaje.

## 🖼️ Capturas de pantalla

Agrega capturas reales de la aplicación para mostrar su interfaz. Puedes crear una carpeta `docs/screenshots/` en el repositorio y guardar allí las imágenes.

Cuando las hayas agregado, reemplaza o completa los siguientes espacios con sus nombres de archivo:

| Pantalla | Archivo sugerido |
|---|---|
| Catálogo público | `docs/screenshots/catalogo.png` |
| Página Acerca de | `docs/screenshots/acerca.png` |
| Formulario de contacto | `docs/screenshots/contacto.png` |
| Página de bienvenida | `docs/screenshots/bienvenida.png` |
| Administración de contactos | `docs/screenshots/contactos-admin.png` |

Para mostrar una imagen en esta sección, usa Markdown. Por ejemplo, cuando exista el archivo:

```markdown
![Catálogo público de OnlyFlans](docs/screenshots/catalogo.png)
```

## 🔐 Consideraciones de acceso y seguridad

- La vista de bienvenida requiere que el usuario haya iniciado sesión.
- La opción de listar contactos se muestra en la navegación a superusuarios.
- Para un despliegue real, no se debe publicar la clave secreta de Django ni utilizar `DEBUG=True`.
- Configura `ALLOWED_HOSTS`, variables de entorno y una configuración de correo apropiada antes de desplegar.
- No publiques una base de datos que contenga información personal real.

## 🧪 Pruebas

El proyecto contiene `web/tests.py`, destinado a las pruebas automatizadas. Para ejecutar las pruebas disponibles:

```bash
python manage.py test
```

## 📚 Objetivo académico

Este proyecto permite aplicar conocimientos de desarrollo web con Django, incluyendo:

- Definición de modelos y migraciones.
- Creación de vistas y rutas.
- Uso de plantillas HTML reutilizables.
- Procesamiento y validación de formularios.
- Persistencia de información en una base de datos.
- Autenticación y control de acceso.
- Integración de recursos estáticos y estilos para la interfaz.

## 👤 Autor

**Cristian Alveal**

---

Proyecto desarrollado con fines académicos.
