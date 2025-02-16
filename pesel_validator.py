import re
from datetime import datetime

def validate_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return False
    
    # Suma kontrolna PESEL
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    check_sum = sum(int(pesel[i]) * weights[i] for i in range(10))
    check_digit = (10 - (check_sum % 10)) % 10
    if check_digit != int(pesel[10]):
        return False
    
    # Data urodzenia (PESEL pierwsze 6 cyfr to data)
    birth_date_str = pesel[:6]
    try:
        birth_date = datetime.strptime(birth_date_str, "%y%m%d")
    except ValueError:
        return False
    
    # Płeć (10. cyfra PESEL)
    gender_digit = int(pesel[9])
    gender = 'M' if gender_digit % 2 != 0 else 'F'

    return gender
