import re
from datetime import datetime

def validate_pesel(pesel):
    if not re.match(r"^\d{11}$", pesel):
        return False

    # PESEL checksum
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    checksum = sum(int(pesel[i]) * weights[i] for i in range(10)) % 10
    checksum = 10 - checksum if checksum != 0 else 0
    if int(pesel[10]) != checksum:
        return False

    # Birthdate verification
    birthdate_str = pesel[:6]  # YYMMDD
    try:
        birthdate = datetime.strptime(birthdate_str, "%y%m%d")
        current_year = datetime.now().year
        if birthdate.year > current_year:
            return False
    except ValueError:
        return False

    # Gender matching with PESEL
    gender_digit = int(pesel[9])
    if gender_digit % 2 == 0:
        gender = 'F'
    else:
        gender = 'M'
    return True
