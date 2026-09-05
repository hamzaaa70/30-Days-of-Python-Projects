print("PASSWORD STRENGTH ANALYZER")

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_number = False
has_special = False

for character in password:

    if character.isupper():
        has_upper = True

    elif character.islower():
        has_lower = True

    elif character.isdigit():
        has_number = True

    else:
        has_special = True

length = len(password)

print("\nPassword Analysis:")

print("Length:", length)
print("UpperCase:", has_upper)
print("LowerCase:", has_lower)
print("Number:", has_number)
print("Special Characters:", has_special)

if (length >= 8 and has_upper and has_lower
        and has_number and has_special):
    print("Strength: Strong")
else:
    print("Strength: Weak")