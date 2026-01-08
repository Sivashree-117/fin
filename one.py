# Remaining units → ₹5/unit
    if units > 200:
        remaining_units = units - 200
        remaining_charge = remaining_units * 5
    else:
        remaining_units = 0

    # Total bill
    total = first_charge + second_charge + remaining_charge

