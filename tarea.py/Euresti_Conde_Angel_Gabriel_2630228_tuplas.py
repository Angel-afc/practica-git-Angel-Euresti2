# ==============================================================================
# COVER PAGE
# ==============================================================================
# Student name: Angel Gabriel Euresti Conde
# Student ID: 2630228
# Group: I.M 1-2
# Assignment: Collections in Python (Lists and Tuples)
# ==============================================================================

# ==============================================================================
# EXECUTIVE SUMMARY
# ==============================================================================
# Las listas permiten almacenar conjuntos de datos ordenados y modificables.
# Las tuplas guardan colecciones ordenadas pero inmutables que no deben cambiar.
# Este documento cubre seis problemas prácticos sobre objetos, carros y artículos.
# Cada problema incluye descripciones, entradas, salidas, validaciones y pruebas.
# Se usan listas para inventarios dinámicos y tuplas para coordenadas o registros.
# ==============================================================================

# ==============================================================================
# GOOD PRACTICES
# ==============================================================================
# - Usar listas cuando necesites agregar, quitar o modificar elementos seguido.
# - Usar tuplas para datos fijos que no deben alterarse (como coordenadas).
# - Escribir código legible con nombres de variables descriptivos en inglés.
# - Validar siempre que los datos no estén vacíos antes de procesarlos.
# ==============================================================================


# ==============================================================================
# PROBLEM 1: CAR PARTS INVENTORY (LIST OPERATIONS)
# ==============================================================================
# Problem 1: Car parts inventory
# Description: Manages a list of car parts, allows adding a new part at the end,
# counts total items, and checks if a specific spare part is in the inventory.
#
# Inputs:
# - initial_items_text (string): Comma-separated car parts (e.g., "tire,battery,oil")
# - new_item (string): New car part to append
# - search_item (string): Spare part to search for
#
# Outputs:
# - "Items list:" <items_list>
# - "Total items:" <len_list>
# - "Found item:" true|false
#
# Validations:
# - initial_items_text not empty after strip.
# - new_item and search_item not empty.
#
# Test cases:
# 1) Normal: "tire, battery, oil", "brake", "battery" -> Found: true
# 2) Border: "tire", "light", "door" -> Found: false
# 3) Error: "", "tire", "oil" -> Error: invalid input

def problem_one_car_inventory():
    initial_items_text = input("Enter car parts separated by commas: ")
    new_item = input("Enter new car part to add: ")
    search_item = input("Enter car part to search: ")

    # Verifica que los textos de entrada no estén vacíos
    if not initial_items_text or not initial_items_text.strip():
        print("Error: invalid input")
        return
    if not new_item or not new_item.strip() or not search_item or not search_item.strip():
        print("Error: invalid input")
        return

    # .split(",") separa el texto por comas para convertirlo en lista
    # item.strip() elimina espacios extra alrededor de cada palabra
    items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]
    
    # .append() agrega el nuevo elemento al final de la lista de carros
    items_list.append(new_item.strip())
    
    # len() obtiene la cantidad total de elementos en la lista
    len_list = len(items_list)
    
    # El operador 'in' busca si el objeto buscado está dentro de la lista
    found = search_item.strip() in items_list
    found_str = "true" if found else "false"

    print("Items list:", items_list)
    print("Total items:", len_list)
    print("Found item:", found_str)


# ==============================================================================
# PROBLEM 2: GPS CAR COORDINATES WITH TUPLES
# ==============================================================================
# Problem 2: GPS car coordinates with tuples
# Description: Uses immutable tuples to represent two GPS coordinate points of a car,
# calculates the Euclidean distance between them, and gets the midpoint tuple.
#
# Inputs:
# - x1, y1, x2, y2 (float): Coordinate values.
#
# Outputs:
# - "Point A:" (x1, y1)
# - "Point B:" (x2, y2)
# - "Distance:" <distance>
# - "Midpoint:" (mx, my)
#
# Validations:
# - Verify all inputs can convert to float.
#
# Test cases:
# 1) Normal: 0.0, 0.0, 3.0, 4.0 -> Distance: 5.0, Midpoint: (1.5, 2.0)
# 2) Border: 1.0, 1.0, 1.0, 1.0 -> Distance: 0.0, Midpoint: (1.0, 1.0)
# 3) Error: "abc", 2.0, 3.0, 4.0 -> Error: invalid input

def problem_two_car_gps():
    try:
        x1 = float(input("Enter point A x-coordinate: "))
        y1 = float(input("Enter point A y-coordinate: "))
        x2 = float(input("Enter point B x-coordinate: "))
        y2 = float(input("Enter point B y-coordinate: "))
    except ValueError:
        # Si el usuario escribe letras en lugar de números muestra error
        print("Error: invalid input")
        return

    # Las tuplas se crean con paréntesis y sirven para datos que no deben cambiar
    point_a = (x1, y1)
    point_b = (x2, y2)

    # Fórmula matemática de distancia euclidiana usando potencias (** 0.5 para raíz cuadrada)
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    # Cálculo de la tupla del punto medio
    midpoint = ((x1 + x2) / 2.0, (y1 + y2) / 2.0)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)


# ==============================================================================
# PROBLEM 3: STORE OBJECTS CATALOG (PARALLEL LISTS)
# ==============================================================================
# Problem 3: Store objects catalog
# Description: Manages store items and their prices using two parallel lists.
# Reads an object name and quantity, then calculates total purchase cost.
#
# Inputs:
# - product_name (string): Name of the store object.
# - quantity (int): Quantity to buy.
#
# Outputs:
# - If found: "Unit price:", "Quantity:", "Total:"
# - If not found: "Error: product not found"
#
# Validations:
# - quantity > 0 and product_name not empty.
#
# Test cases:
# 1) Normal: product="lamp", quantity=2 -> Unit price: 150.0, Total: 300.0
# 2) Border: product="pen", quantity=1 -> Unit price: 10.0, Total: 10.0
# 3) Error: product="computer", quantity=2 -> Error: product not found

def problem_three_store_catalog():
    # Listas paralelas: los nombres y los precios coinciden por su posición (índice)
    product_names = ["lamp", "pen", "desk", "chair"]
    product_prices = [150.0, 10.0, 1200.0, 450.0]

    product_name = input("Enter object name to buy: ")
    quantity = input("Enter quantity: ")

    if not product_name or not product_name.strip():
        print("Error: invalid input")
        return

    try:
        qty = int(quantity)
        if qty <= 0:
            print("Error: invalid input")
            return
    except ValueError:
        print("Error: invalid input")
        return

    target = product_name.strip().lower()

    # .index() busca la posición de un elemento en la lista
    if target in product_names:
        idx = product_names.index(target)
        unit_price = product_prices[idx]
        total_price = unit_price * qty

        print("Unit price:", unit_price)
        print("Quantity:", qty)
        print("Total:", total_price)
    else:
        print("Error: product not found")


# ==============================================================================
# PROBLEM 4: CAR MODELS AND MILEAGE STATS (LIST OF NUMBERS)
# ==============================================================================
# Problem 4: Car models and mileage stats
# Description: Manages a list of car mileage numbers, calculates the total sum,
# average, maximum, minimum, and verifies if all milages are over 1000 km.
#
# Inputs:
# - mileages_text (string): Comma-separated mileage numbers (e.g., "5000,12000,8500").
#
# Outputs:
# - "Mileages:" <list>
# - "Average mileage:" <avg>
# - "Max mileage:" <max>
# - "Min mileage:" <min>
# - "All high mileage:" true|false
#
# Validations:
# - Input text not empty and elements convertible to float.
# - List must not be empty.
#
# Test cases:
# 1) Normal: "5000, 12000, 8500" -> Average: 8500.0, Max: 12000.0, Min: 5000.0, All high: true
# 2) Border: "1000, 2000" -> Average: 1500.0, All high: false
# 3) Error: "" -> Error: invalid input

def problem_four_car_mileage():
    mileages_text = input("Enter car mileages separated by commas: ")

    if not mileages_text or not mileages_text.strip():
        print("Error: invalid input")
        return

    try:
        # Convierte los textos separados por comas en una lista de números flotantes
        mileage_list = [float(x.strip()) for x in mileages_text.split(",") if x.strip()]
    except ValueError:
        print("Error: invalid input")
        return

    if not mileage_list:
        print("Error: invalid input")
        return

    # sum() suma todos los números de la lista
    total_sum = sum(mileage_list)
    avg_value = total_sum / len(mileage_list)
    
    # max() y min() encuentran el número mayor y menor de la lista
    max_val = max(mileage_list)
    min_val = min(mileage_list)

    # Verificación booleana para comprobar si todos son mayores o iguales a 1000
    all_high = True
    for m in mileage_list:
        if m < 1000.0:
            all_high = False
            break

    print("Mileages:", mileage_list)
    print("Average mileage:", round(avg_value, 2))
    print("Max mileage:", max_val)
    print("Min mileage:", min_val)
    print("All high mileage:", str(all_high).lower())


# ==============================================================================
# PROBLEM 5: MATERIAL OBJECTS INVENTORY SORTING
# ==============================================================================
# Problem 5: Material objects inventory sorting
# Description: Reads a list of material objects (strings), sorts them alphabetically,
# and reverses the order to display sorted inventory status.
#
# Inputs:
# - objects_text (string): Comma-separated material names (e.g., "wood, plastic, metal").
#
# Outputs:
# - "Original list:" <list>
# - "Sorted list:" <list>
# - "Reversed sorted list:" <list>
#
# Validations:
# - Input text not empty after strip.
#
# Test cases:
# 1) Normal: "wood, plastic, metal" -> Sorted: ['metal', 'plastic', 'wood']
# 2) Border: "glass" -> Sorted: ['glass']
# 3) Error: "" -> Error: invalid input

def problem_five_material_sorting():
    objects_text = input("Enter material objects separated by commas: ")

    if not objects_text or not objects_text.strip():
        print("Error: invalid input")
        return

    # Limpia y separa los objetos materiales en una lista
    objects_list = [obj.strip() for obj in objects_text.split(",") if obj.strip()]

    if not objects_list:
        print("Error: invalid input")
        return

    # Creamos copias para no perder el orden original
    original_list = list(objects_list)
    
    # sorted() ordena alfabéticamente los elementos de la lista
    sorted_list = sorted(objects_list)
    
    # reversed_list invierte el orden de la lista ya ordenada
    reversed_list = sorted(objects_list, reverse=True)

    print("Original list:", original_list)
    print("Sorted list:", sorted_list)
    print("Reversed sorted list:", reversed_list)


# ==============================================================================
# PROBLEM 6: GARAGE CAR LIST CRUD (ADD, SEARCH, DELETE)
# ==============================================================================
# Problem 6: Garage car list CRUD
# Description: Implements a mini system for a garage list using basic list methods 
# (append, in search, remove) for actions: ADD, SEARCH, or DELETE.
#
# Inputs:
# - action_text (string): "ADD", "SEARCH", or "DELETE"
# - car_model (string): Name of the car model.
#
# Outputs:
# - For ADD: "Car saved:" <model>
# - For SEARCH: "Car found: true|false"
# - For DELETE: "Car deleted:" <model> or "Error: car not found"
#
# Validations:
# - action_text must be valid (ADD, SEARCH, DELETE).
# - car_model not empty.
#
# Test cases:
# 1) Normal: action="ADD", car="Toyota" -> Car saved: Toyota
# 2) Border: action="SEARCH", car="Ford" -> Car found: true/false
# 3) Error: action="UPDATE", car="Mazda" -> Error: invalid input

def problem_six_garage_crud():
    # Lista inicial de carros en el garaje
    garage_cars = ["toyota", "ford", "chevrolet", "nissan"]

    action_text = input("Enter action (ADD, SEARCH, DELETE): ")
    car_model = input("Enter car model: ")

    if not action_text or not action_text.strip():
        print("Error: invalid input")
        return

    # .upper() convierte la acción a mayúsculas para estandarizar
    action = action_text.strip().upper()
    if action not in ["ADD", "SEARCH", "DELETE"]:
        print("Error: invalid input")
        return

    if not car_model or not car_model.strip():
        print("Error: invalid input")
        return

    model = car_model.strip().lower()

    if action == "ADD":
        # .append() añade el carro nuevo al final de la lista
        garage_cars.append(model)
        print("Car saved:", car_model.strip())
        print("Updated garage list:", garage_cars)

    elif action == "SEARCH":
        # Comprueba con 'in' si el modelo del carro está en la lista del garaje
        found = model in garage_cars
        print("Car found:", str(found).lower())

    elif action == "DELETE":
        if model in garage_cars:
            # .remove() elimina el elemento específico de la lista
            garage_cars.remove(model)
            print("Car deleted:", car_model.strip())
            print("Updated garage list:", garage_cars)
        else:
            print("Error: car not found")


# ==============================================================================
# MAIN MENU
# ==============================================================================

def main():
    while True:
        print("\n--- COLLECTIONS IN PYTHON (LISTS AND TUPLES) ---")
        print("1. Car parts inventory")
        print("2. GPS car coordinates with tuples")
        print("3. Store objects catalog")
        print("4. Car models and mileage stats")
        print("5. Material objects inventory sorting")
        print("6. Garage car list CRUD")
        print("0. Exit")

        option = input("Select a problem (0-6): ").strip()

        if option == "1":
            problem_one_car_inventory()
        elif option == "2":
            problem_two_car_gps()
        elif option == "3":
            problem_three_store_catalog()
        elif option == "4":
            problem_four_car_mileage()
        elif option == "5":
            problem_five_material_sorting()
        elif option == "6":
            problem_six_garage_crud()
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Error: invalid input")


if __name__ == "__main__":
    main()


# ==============================================================================
# CONCLUSIONS
# ==============================================================================
# Las listas son estructuras mutables ideales para inventarios que cambian seguido.
# Las tuplas protegen datos fijos como coordenadas gracias a su inmutabilidad.
# Usar listas paralelas ayuda a relacionar elementos cuando no se usan diccionarios.
# Validar entradas previene errores fatales al buscar o procesar datos.
# El dominio de los métodos de listas facilita la administración de colecciones.
# ==============================================================================

# ==============================================================================
# REFERENCES
# ==============================================================================
# 1) Python documentation - Built-in Types: list, tuple.
# 2) Python Software Foundation - Data Structures Tutorial.
# 3) Lutz, Mark. Learning Python. 5th Edition, O'Reilly Media, 2013.
# 4) Matthes, Eric. Python Crash Course. 3rd Edition, No Starch Press, 2022.
# 5) Apuntes de clase sobre colecciones y métodos básicos en Python.
# ==============================================================================
