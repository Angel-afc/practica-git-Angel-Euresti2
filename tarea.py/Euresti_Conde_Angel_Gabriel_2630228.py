# NUMERO Y BOOLEANAS
# COVER PAGE
# Student name: Angel Gabriel Euresti Conde
# Student ID: 2630228
# Group: I.M 1-2
# Assignment: Numeric Types and Boolean Values


# EXECUTIVE SUMMARY
# int is used for whole numbers and float for decimals.
# bool stores True or False values.
# Comparisons like >=, ==, and < give boolean results.
# Logical operators like and, or, and not combine conditions.
# Validation helps to avoid program errors and division by zero.
# This file contains 6 exercises using numbers and booleans.
# Each problem has inputs, outputs, validations, and test cases.


# GOOD PRACTICES
# Use float for measurements and int for whole numbers.
# Use simple and clear variable names.
# Always check inputs before making operations.
# Print clear output messages.


# PROBLEM 1: LENGTH CONVERTER
# Description:
# Convert meters to feet and miles.
# Check if the distance is at least 100 meters.
#
# Inputs: meters (float)
# Outputs: Feet, Miles, Long distance
# Validations: meters >= 0
# Test cases:
# Normal: 150.0 -> 492.13 ft, 0.093 mi, true
# Border: 0.0 -> 0.0 ft, 0.0 mi, false
# Error: -10.0 -> Error: invalid input

def problem_1():
    try:
        meters = float(input("Enter distance in meters: "))

        if meters < 0:
            print("Error: invalid input")
            return

        feet = meters * 3.28084
        miles = meters / 1609.34
        is_long_distance = meters >= 100.0

        print("Feet:", round(feet, 2))
        print("Miles:", round(miles, 4))
        print("Long distance:", str(is_long_distance).lower())

    except ValueError:
        print("Error: invalid input")


# PROBLEM 2: FUEL CONSUMPTION AND TRIP COST
# Description:
# Calculate fuel needed for a trip and the total cost.
# Check if the cost is 50 or more.
#
# Inputs: distance_km (float), kpl (float), price_per_liter (float)
# Outputs: Liters needed, Total trip cost, Expensive trip
# Validations: distance_km >= 0, kpl > 0, price_per_liter > 0
# Test cases:
# Normal: 300 km, 15 kpl, 2.5 price -> 20.0 L, 50.0 cost, true
# Border: 0 km, 15 kpl, 2.5 price -> 0.0 L, 0.0 cost, false
# Error: 100 km, 0 kpl, 2.5 price -> Error: invalid input

def problem_2():
    try:
        distance_km = float(input("Enter trip distance in kilometers: "))
        kpl = float(input("Enter fuel efficiency (km per liter): "))
        price_per_liter = float(input("Enter fuel price per liter: "))

        if distance_km < 0 or kpl <= 0 or price_per_liter <= 0:
            print("Error: invalid input")
            return

        liters_needed = distance_km / kpl
        total_cost = liters_needed * price_per_liter
        is_expensive_trip = total_cost >= 50.0

        print("Liters needed:", round(liters_needed, 2))
        print("Total trip cost:", round(total_cost, 2))
        print("Expensive trip:", str(is_expensive_trip).lower())

    except ValueError:
        print("Error: invalid input")


# PROBLEM 3: EVENT TICKET PRICING
# Description:
# Calculate ticket price with a 10% discount for VIP, early bird, or 5+ tickets.
#
# Inputs: ticket_count (int), base_price (float), is_vip (string), is_early_bird (string)
# Outputs: Discount applied, Final price
# Validations: ticket_count > 0, base_price > 0, answers must be YES or NO
# Test cases:
# Normal: 2 tickets, 100.0 price, YES, NO -> Discount true, Final 180.0
# Border: 5 tickets, 100.0 price, NO, NO -> Discount true, Final 450.0
# Error: 0 tickets, 100.0 price, YES, NO -> Error: invalid input

def problem_3():
    try:
        ticket_count = int(input("Enter number of tickets: "))
        base_price = float(input("Enter price per ticket: "))
        is_vip_text = input("Is the buyer a VIP member? (YES/NO): ").strip().upper()
        is_early_bird_text = input("Is this an early bird purchase? (YES/NO): ").strip().upper()

        if ticket_count <= 0 or base_price <= 0:
            print("Error: invalid input")
            return

        if is_vip_text != "YES" and is_vip_text != "NO":
            print("Error: invalid input")
            return

        if is_early_bird_text != "YES" and is_early_bird_text != "NO":
            print("Error: invalid input")
            return

        is_vip = (is_vip_text == "YES")
        is_early_bird = (is_early_bird_text == "YES")

        subtotal = ticket_count * base_price
        discount_applied = is_vip or is_early_bird or (ticket_count >= 5)

        if discount_applied:
            final_price = subtotal * 0.90
        else:
            final_price = subtotal

        print("Discount applied:", str(discount_applied).lower())
        print("Final price:", round(final_price, 2))

    except ValueError:
        print("Error: invalid input")


# PROBLEM 4: DATA PACKET METRICS
# Description:
# Read 3 latency values in ms, calculate sum, average, max, min,
# and check if all are below 50 ms.
#
# Inputs: p1, p2, p3 (float)
# Outputs: Total latency, Average latency, Max latency, Min latency, Low latency network
# Validations: p1 >= 0, p2 >= 0, p3 >= 0
# Test cases:
# Normal: 12.5, 24.0, 18.0 -> Total 54.5, Average 18.17, Max 24.0, Min 12.5, true
# Border: 50.0, 50.0, 50.0 -> Total 150.0, Average 50.0, Max 50.0, Min 50.0, false
# Error: -5.0, 20.0, 30.0 -> Error: invalid input

def problem_4():
    try:
        p1 = float(input("Enter latency for packet 1 (ms): "))
        p2 = float(input("Enter latency for packet 2 (ms): "))
        p3 = float(input("Enter latency for packet 3 (ms): "))

        if p1 < 0 or p2 < 0 or p3 < 0:
            print("Error: invalid input")
            return

        total_latency = p1 + p2 + p3
        average_latency = total_latency / 3.0
        max_latency = max(p1, p2, p3)
        min_latency = min(p1, p2, p3)

        is_low_latency = (p1 < 50.0) and (p2 < 50.0) and (p3 < 50.0)

        print("Total latency:", round(total_latency, 2))
        print("Average latency:", round(average_latency, 2))
        print("Max latency:", round(max_latency, 2))
        print("Min latency:", round(min_latency, 2))
        print("Low latency network:", str(is_low_latency).lower())

    except ValueError:
        print("Error: invalid input")


# PROBLEM 5: ELECTRICITY CONSUMPTION TIER
# Description:
# Calculate kWh per kW ratio and check high efficiency tier
# (usage <= 1500 kWh and peak <= 50 kW).
#
# Inputs: total_kwh (float), peak_demand_kw (float)
# Outputs: Ratio kWh/kW, High efficiency tier
# Validations: total_kwh >= 0 and peak_demand_kw > 0
# Test cases:
# Normal: 1200 kWh, 40 kW -> Ratio 30.0, true
# Border: 1500 kWh, 50 kW -> Ratio 30.0, true
# Error: 1000 kWh, 0 kW -> Error: invalid input

def problem_5():
    try:
        total_kwh = float(input("Enter total electricity usage in kWh: "))
        peak_demand_kw = float(input("Enter peak demand in kW: "))

        if total_kwh < 0 or peak_demand_kw <= 0:
            print("Error: invalid input")
            return

        ratio = total_kwh / peak_demand_kw
        is_high_efficiency = (total_kwh <= 1500.0) and (peak_demand_kw <= 50.0)

        print("Ratio kWh/kW:", round(ratio, 2))
        print("High efficiency tier:", str(is_high_efficiency).lower())

    except ValueError:
        print("Error: invalid input")


# PROBLEM 6: STORAGE SPACE CAPACITY
# Description:
# Calculate storage usage percentage and classify status as normal, high usage, or critical.
#
# Inputs: used_gb (float), total_gb (float)
# Outputs: Usage percentage, Normal storage, High usage, Critical
# Validations: total_gb > 0, used_gb >= 0, used_gb <= total_gb
# Test cases:
# Normal: 450 GB used, 1000 GB total -> 45.0%, Normal true
# Border: 800 GB used, 1000 GB total -> 80.0%, High usage true
# Error: 1200 GB used, 1000 GB total -> Error: invalid input

def problem_6():
    try:
        used_gb = float(input("Enter used storage in GB: "))
        total_gb = float(input("Enter total storage capacity in GB: "))

        if used_gb < 0 or total_gb <= 0 or used_gb > total_gb:
            print("Error: invalid input")
            return

        percentage = (used_gb / total_gb) * 100.0

        is_normal = percentage < 75.0
        is_high_usage = (percentage >= 75.0) and (percentage < 90.0)
        is_critical = percentage >= 90.0

        print("Usage percentage:", round(percentage, 2))
        print("Normal storage:", str(is_normal).lower())
        print("High usage:", str(is_high_usage).lower())
        print("Critical:", str(is_critical).lower())

    except ValueError:
        print("Error: invalid input")


# MAIN MENU

def main():
    while True:
        print("\nNUMERIC TYPES AND BOOLEAN VALUES")
        print("1. Length converter")
        print("2. Fuel consumption and trip cost")
        print("3. Event ticket pricing")
        print("4. Data packet metrics")
        print("5. Electricity consumption tier")
        print("6. Storage space capacity")
        print("0. Exit")

        option = input("Select a problem: ").strip()

        if option == "1":
            problem_1()
        elif option == "2":
            problem_2()
        elif option == "3":
            problem_3()
        elif option == "4":
            problem_4()
        elif option == "5":
            problem_5()
        elif option == "6":
            problem_6()
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Error: invalid input")


if __name__ == "__main__":
    main()


# CONCLUSIONS
# Integers represent whole numbers and floats represent decimals.
# Comparisons return Boolean values (True or False).
# Input validation stops incorrect numbers and division by zero.
# Logical operators (and, or, not) help to test multiple conditions.
# Testing normal, border, and error inputs makes sure the code works fine.