# MATRIZ: Lista de productos con sus cantidades
matriz_inventario = [
    ["A001", "Arroz 1kg", 45, 50],
    ["A002", "Aceite 1L", 12, 20],
    ["A003", "Pasta 500g", 60, 40],
    ["A004", "Leche 1L", 15, 30],
    ["A005", "Azúcar 1kg", 8, 25]
]

# FUNCIÓN: Aquí se hace la matemática de la resta
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        resta = stock_minimo - stock_actual
        return resta
    else:
        return 0

# INICIO DEL INFORME
print("=== INFORME DE INVENTARIO ===")

# RECORRIDO: Revisamos producto por producto
for producto in matriz_inventario:
    codigo = producto[0]
    nombre = producto[1]
    stock_actual = producto[2]
    stock_minimo = producto[3]
    
    # Llamamos a la función para que nos dé el número
    cantidad_a_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
    
    # Mostramos el resultado simple en la pantalla
    print("Producto:", nombre, "| Actual:", stock_actual, "| Mínimo:", stock_minimo, "| Pedir:", cantidad_a_pedir)

print("=============================")
