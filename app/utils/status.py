from datetime import date

def get_medicine_status(expiry_date, quantity):
    today = date.today()

    if expiry_date < today:
        return "Expired"
    elif quantity == 0:
        return "Out of Stock"
    elif quantity < 10:
        return "Low Stock"
    else:
        return "Active"