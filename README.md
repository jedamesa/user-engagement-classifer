# user-engagement-classifer
Algoritmo simple para clasificar el compromiso de usuario basados en el tiempo de sesión y clics.

# User Session Classifier

Un script interactivo diseñado como una línea de producción secuencial para capturar, validar y clasificar el nivel de compromiso de los usuarios según su comportamiento en sesión.

## 🚀 Arquitectura y Funcionamiento

El programa procesa la información de manera controlada a través de tres grandes etapas lógicas:

### 1. Entrada y Validación de Datos (Sistema Anti-Fallos)
El sistema arranca desplegando las instrucciones en pantalla e inicia un bucle dinámico para registrar a cada cliente solicitando tres variables aisladas:
* **Identificador:** Nombre o ID de la sesión.
* **Tiempo:** Duración de la visita medida en segundos.
* **Interacciones:** Cantidad de clics realizados.

> 🛠️ **Robustez:** Si el operador introduce caracteres alfabéticos o texto en los campos numéricos (tiempo o clics), el programa captura el error, evita un colapso (*crash*), emite una alerta visual y vuelve a solicitar el dato correcto sin perder el progreso.

### 2. Control de Umbral Obligatorio (El "Candado")
Para garantizar una muestra de datos estadísticamente válida, el sistema aplica una regla de control estricta:
* **Mínimo obligatorio:** Se deben registrar al menos **5 usuarios**.
* El sistema bloquea cualquier intento de salida prematura antes de alcanzar este número.
* Tras guardar con éxito el quinto registro, se desbloquea un menú numérico de navegación:
  * `Presionar 1`: Continuar ingresando más usuarios.
  * `Presionar 0`: Finalizar la captura y pasar al reporte.

### 3. Motor de Clasificación y Reporte Final
Al cerrar la captura (`0`), el programa limpia por completo la pantalla para eliminar el ruido visual y evalúa cada registro mediante la siguiente matriz lógica de determinantes:


| Clasificación | Condición Lógica | Criterio de Activación |
| :--- | :--- | :--- |
|  **Alto** | `Tiempo > 180` **Y** `Clics > 8` | Cumplimiento estricto de ambas métricas altas. |
|  **Bajo** | `Tiempo < 60` **O** `Clics < 3` | Se activa si cualquiera de las dos métricas es deficiente. |
|  **Medio** | *Rango intermedio* | Casos que se encuentran entre los límites de las reglas anteriores. |

El resultado final se despliega de manera elegante en una **tabla limpia y ordenada** en la terminal, vinculando directamente el ID de cada cliente con su nivel de compromiso asignado.

## 💻 Instalación y Uso


Puedes poner en marcha este clasificador en tu computadora de dos maneras diferentes:

### Opción A: Descarga rápida (Sin usar comandos de Git)
1. Haz clic en el botón verde **"Code"** (arriba a la derecha) y selecciona **"Download ZIP"**.
2. Descomprime el archivo `.zip` descargado en tu computadora.
3. Abre tu terminal o consola de comandos, navega hasta esa carpeta y escribe:
   ```bash
   python NOMBRE_DE_TU_ARCHIVO.py
   ```

### Opción B: Mediante la Terminal (Para desarrolladores)
Copia y pega este bloque de comandos en tu terminal para clonar, ingresar a la carpeta y ejecutar el programa automáticamente:
```bash
git clone https://github.com
cd NOMBRE_DE_TU_REPOSITORIO
python NOMBRE_DE_TU_ARCHIVO.py
```


## 📝 Licencia

Este proyecto es de código abierto y está disponible para fines educativos o de portafolio personal.
