def calculate_bill(units):
    # Initialize charges
    first_charge = second_charge = remaining_charge = 0
# Remaining units → ₹5/unit
    if units > 200:
        remaining_units = units - 200
        remaining_charge = remaining_units * 5
    else:
        remaining_units = 0

    # Total bill
    total = first_charge + second_charge + remaining_charge

    # First 100 units → ₹2/unit
    if units > 0:
        first_units = min(units, 100)
        first_charge = first_units * 2

    # Next 100 units → ₹3/unit
    if units > 100:
        second_units = min(units - 100, 100)
        second_charge = second_units * 3
