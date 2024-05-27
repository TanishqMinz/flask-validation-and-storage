import re

def validatetext(firstname, lastname):
    nameregex = r"^[a-zA-Z]+$"
    if re.match(nameregex, firstname) and re.match(nameregex, lastname):
        return True
    return False

def validaterollno(rollno):
    noregex = r"^\d{7}$"
    return re.match(noregex, rollno)

def validateoption(option):
    return bool(option)

def verify(form):
    errors = {}
    firstname = form.get("firstname", "").strip()
    lastname = form.get("lastname", "").strip()
    rollno = form.get("rollno", "").strip()
    option = form.get("option", "").strip()
    
    if not validatetext(firstname, lastname):
        errors["name"] = "First name and Last name must contain only letters."
    if not validaterollno(rollno):
        errors["rollno"] = "Roll number must be exactly 7 digits."
    if not validateoption(option):
        errors["option"] = "You must select an option."
        
    return errors if errors else None
