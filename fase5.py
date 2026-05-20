# =====================================================================
# FASE 5 - FUNDAMENTOS DE PROGRAMACIÓN
# ESTUDIANTE: ERIKA YADIRA HERNÁNDEZ ROMERO
# PROGRAMA: INGENIERÍA DE SISTEMAS
# PROBLEMA SELECCIONADO: PROBLEMA 3 (AUDITORÍA DE INVENTARIO)
# =====================================================================

# REQUERIMIENTO: Crear matriz con los 5 artículos de inventario
# Estructura: [Código, Nombre, Stock Actual, Stock Mínimo Requerido]
matriz_inventario = [
    ["A001", "Arroz de primera 1kg", 45, 50],
    ["A002", "Aceite vegetal 1L", 12, 20],
    ["A003", "Frijol cargamanto 500g", 60, 40],
    ["A004", "Azúcar blanca 1kg", 18, 25],
    ["A005", "Leche entera 1L", 30, 30]
]

# REQUERIMIENTO: Definir la función para determinar la cantidad exacta a pedir
def calcular_pedido(matriz):
    lista_pedidos = []
    
    # Ciclo para recorrer los artículos de la matriz uno por uno
    for articulo in matriz:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        
        # Estructura de decisión: Validar condición de reabastecimiento
        if stock_actual < stock_minimo:
            # Fórmula: Cantidad exacta a pedir = Mínimo - Actual
            cantidad_a_pedir = stock_minimo - stock_actual
            lista_pedidos.append([nombre, cantidad_a_pedir])
            
    return lista_pedidos

# =====================================================================
# EJECUCIÓN DEL PROGRAMA PRINCIPAL
# =====================================================================
# Llamar a la función pasando la matriz como argumento
resultados = calcular_pedido(matriz_inventario)

# Mostrar los resultados formateados en la terminal
print("=========================================")
print("  ARTÍCULOS A SOLICITAR REABASTECIMIENTO  ")
print("=========================================")
for articulo in resultados:
    print(f"- {articulo[0]}: {articulo[1]} unidades")
print("=========================================")
