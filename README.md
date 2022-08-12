# QR BOT

## Descripcion:
Script creado con la finalidad de automatizar la creacion del codigo QR para ingreso ingreso a la universidad, en este script se usa selenenium para la automatizacion web, y pywhatkit para el envio del QR via whatsapp.

## Instalacion:
* [instalar python.](https://www.python.org/downloads/)
* instalar selenium (python -m pip install selenium).
* [instalar chromeDriver (usar la misma version que chrome).](https://chromedriver.chromium.org/downloads)
* instalar dotenv y decouple (pip install python-dotenv python-decouple).
* instalar pywhatkit (pip install pywhatkit).

## Modo de uso:
* llenar  el archivo .env con los datos solicitados.
* ir a la linea 24 del bot.py e ingresar la ruta donde se instalo chromeDriver.
* usar el comando para inicar el script- **python bot.py**.

### Nota:
Si se traba al ingresar usuario solo volver a correr script.

El envio del whatsapp demora un poco(se esta buscando otra libreria).


