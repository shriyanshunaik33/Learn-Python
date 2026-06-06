password = "Hello123467"

len_of_pass = len(password)

if len_of_pass<6:
    strength = "Weak"
elif 6<=len_of_pass<11:
    strength = "Medium"
else:
    strength = "Strong"

print("Strength of the password you entered is", strength)