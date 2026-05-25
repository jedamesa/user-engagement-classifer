# ==========================================
# 1. FUNCIÓN DE LÓGICA DE NEGOCIO
# ==========================================
def evaluar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

# ==========================================
# 2. INTERFAZ DE BIENVENIDA E INSTRUCCIONES
# ==========================================
print("====================================================")
print("     SISTEMA DE EVALUACIÓN DE COMPROMISO DE CLIENTES")
print("====================================================")
print("Instrucciones:")
print("- Ingrese los datos de las sesiones uno por uno.")
print("- Duración y Clics deben ser números enteros.")
print("- El ID del cliente no debe superar los 30 caracteres.")
print("- REQUISITO: Debe registrar un MÍNIMO DE 5 SESIONES.")
print("====================================================\n")

matriz_sesiones = []

# ==========================================
# 3. CAPTURA DE DATOS PASO A PASO
# ==========================================
while True:
    numero_fila = len(matriz_sesiones) + 1
    print(f"--- REGISTRANDO SESIÓN #{numero_fila} ---")
    
    while True:
        id_cliente = input("1. Ingrese ID del Cliente (máx 30 caracteres): ").strip()
        if 0 < len(id_cliente) <= 30:
            break
        print(">> Error: El ID no puede estar vacío ni superar los 30 caracteres.")
    
    while True:
        try:
            duracion = int(input("2. Ingrese la Duración (en segundos enteros): "))
            if duracion >= 0:
                break
            print(">> Error: La duración no puede ser negativa.")
        except ValueError:
            print(">> Error: Por favor, ingrese solo números enteros.")
            
    while True:
        try:
            clics = int(input("3. Ingrese la cantidad de Clics (enteros): "))
            if clics >= 0:
                break
            print(">> Error: Los clics no pueden ser negativos.")
        except ValueError:
            print(">> Error: Por favor, ingrese solo números enteros.")
            
    matriz_sesiones.append([id_cliente, duracion, clics])
    print(f"¡Sesión de {id_cliente} guardada con éxito!\n")
    
    cantidad_actual = len(matriz_sesiones)
    
    if cantidad_actual >= 5:
        while True:
            print("¿Qué desea hacer ahora?")
            print("[1] Agregar más sesiones")
            print("[0] Ir al informe")
            opcion = input("Seleccione una opción (1 o 0): ").strip()
            
            if opcion == '1' or opcion == '0':
                break
            print(">> Error: Opción inválida. Ingrese estrictamente 1 o 0.\n")
        
        if opcion == '0':
            break
        print()
    else:
        print(f"-> Llevas {cantidad_actual} de 5 sesiones mínimas requeridas. Continuando...\n")

# ==========================================
# 4. PROCESAMIENTO Y SALIDA (INFORME FINAL)
# ==========================================
print("\n========================================")
print("           INFORME DE COMPROMISO        ")
print("========================================")
print(f"{'ID CLIENTE':<15} | {'NIVEL DE COMPROMISO'}")
print("----------------------------------------")

for sesion in matriz_sesiones:
    id_clie = sesion[0]
    tiempo = sesion[1]
    num_clics = sesion[2]
    
    resultado = evaluar_compromiso(tiempo, num_clics)
    
    print(f"{id_clie:<15} | {resultado}")

print("========================================\n")
print("Proceso finalizado con éxito.")