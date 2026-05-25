# user-engagement-classifer
Algoritmo simple para clasificar el compromiso de usuario basados en el tiempo de sesión y clics.

```markdown
# Sistema de Evaluación de Compromiso de Clientes (Customer Engagement Analysis)

Un sistema analítico basado en consola desarrollado en **Python 3.13** para estructurar, validar y procesar métricas de interacción de usuarios mediante matrices bidimensionales. El sistema captura variables cuantitativas de comportamiento (duración de sesión y clics) para categorizar el nivel de lealtad o compromiso (*engagement*) de un cliente bajo reglas lógicas de negocio algorítmicas.

## 📊 Arquitectura del Sistema y Lógica de Datos

El programa procesa la información estructurándola en una matriz dinámica en memoria. Cada fila representa una sesión de usuario única con el siguiente esquema de datos vectoriales:

Fila = [ID_Cliente (str), Duracion (int), Clics (int)]

### Reglas de Negocio Algorítmicas (Matriz de Decisiones)

La función core `evaluar_compromiso` aplica lógica condicional ramificada para determinar el nivel de interacción:

* **Alto:** Sesiones con una duración estrictamente mayor a 180 segundos **Y** más de 8 clics realizados.
* **Bajo:** Sesiones con una duración menor a 60 segundos **O** menos de 3 clics realizados (criterio de rebote).
* **Medio:** Sesiones que no cumplen con los extremos anteriores (comportamiento estándar).

---

## 🛠️ Requisitos e Instalación

### Prerrequisitos
* **Motor:** Python 3.11 o superior (Desarrollado y testeado en **Python 3.13 64-bit**).
* **Entorno:** Cualquier terminal de comandos (CMD, PowerShell, Bash) o el terminal integrado de **Visual Studio Code**.

### Clonación y Configuración (Próximamente con Git)
Cuando el repositorio se gestione mediante control de versiones de Git, el despliegue se realizará con los siguientes comandos en tu terminal:

```bash


# Ejecutar el script analítico
python main.py
