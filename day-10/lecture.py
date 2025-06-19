def format_name(first_name, last_name):
    first_name = first_name[0].upper() + first_name[1:].lower()
    last_name = last_name[0].upper() + last_name[1:].lower()
    return first_name, last_name
a = format_name("doniyOrbek", "boltayeV")
print(a)

name = "bEaSt"
print(name.title()) # rutrns string in title format

def is_leap_year(year):
    """Finds whether a year is leap or not"""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
