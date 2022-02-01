password = input("Podaj nowe hasło: ")

has_lower = False
has_upper = False
has_digit = False
for char in password:  # idź znak po znaku
    if char.isalpha() and char.isupper():
        has_upper = True
    if char.isalpha() and char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
long_enough = len(password) >= 8

is_correct = has_lower and has_upper and has_digit and long_enough
if is_correct:
    print("Twoje hasło jest wystarczająco złożone")
else:
    print("Zmień poniższe rzeczy w Twoim haśle:")
    if not has_lower:
        print("- przynajmniej jedna mała litera")
    if not has_upper:
        print("- przynajmniej jedna duża litera")
    if not has_digit:
        print("- przynajmniej jedna cyfra")
    if not long_enough:
        print("- przynajmniej 8 znaków")
