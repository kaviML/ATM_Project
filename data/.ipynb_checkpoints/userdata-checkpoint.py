existingusers = {
    101:{'name':'Asha Ramesh' ,'gender':'F' ,'account no.':'1234567890123450', 'pin':'4321', 'city': 'Hydrabad', 'Saving': 2500},
    102:{'name':'Manoj Kumar','gender':'M','account no.':'9876543210987650', 'pin':'2468', 'city':'Jaipur' , 'Saving': 8000},
    103:{'name':'Sneha Raj','gender':'F','account no.':'2222333344445550', 'pin':'1357', 'city':'Bhopal' , 'Saving': 12000},
    104:{'name':'Ravi Sharma' ,'gender':'M' ,'account no.':'4444555566667770', 'pin':'8642' , 'city':'Dehradun', 'Saving': 6700},
    105:{'name':'Arun Das','gender':'M','account no.':'6666777788889990', 'pin':'2580', 'city':'Kolkata', 'Saving': 900}
    }

##IMPORTANT::
# Why account_no and pin should be strings (not integers)
# 🧩 1. Leading zeros matter --
# If an account number or PIN starts with a 0, integers will drop those zeros automatically.

# 2. They’re identifiers, not quantities --
# An account number or PIN isn’t something you’ll add, subtract, or multiply.
# They’re IDs, like your Aadhaar number or phone number — which should stay fixed as text.

# 3. Avoids integer size issues
# Some banks use 14–16 digit account numbers.
# Python handles large integers fine, but other systems (like Excel or databases) can round off or distort them if stored as numbers.