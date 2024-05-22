# Login sencillo con mysql
## Configuración del Entorno Virtual y Instalación de Dependencias

Este repositorio utiliza un entorno virtual para gestionar las dependencias del proyecto. Sigue estos pasos para configurar tu entorno de desarrollo:

### Crear y Activar el Entorno Virtual

1. Abre una terminal en el directorio raíz del proyecto.
2. Ejecuta el siguiente comando para crear un entorno virtual llamado `env`:

  ```
   python -m venv env
  ```
Una vez creado el entorno virtual, actívalo. Dependiendo de tu sistema operativo, puedes utilizar uno de los siguientes comandos:
En Windows:
  ```
  env\Scripts\activate
  ```
En macOS y Linux:
  ```
  source env/bin/activate
  ```
### Instalar dependencias
Una vez que hayas activado el entorno virtual, utiliza el siguiente comando para instalar las dependencias del proyecto desde el archivo requirements.txt:
  ```
  pip install -r requirements.txt
  ```
