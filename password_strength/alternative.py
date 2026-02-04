password = input("Enter your password: ")

length_ok = False
digit_ok = False
special_ok = False

if len(password) >= 8:
    length_ok = True

special_chars = {"!", "@", "#", "$", "%", "^", "&", "*"}

for char in password:
    if char.isdigit():
        digit_ok = True
    if char in special_chars:
        special_ok = True

conditions_met = 0

if length_ok:
    conditions_met += 1
if digit_ok:
    conditions_met += 1
if special_ok:
    conditions_met += 1

if conditions_met == 1:
    print("Weak")
elif conditions_met == 2:
    print("Medium")
elif conditions_met == 3:
    print("Strong")


