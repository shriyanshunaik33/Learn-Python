distance = 1000000000000000000

if distance < 3:
    transport = "Walk"
elif distance <=15:
    transport = "Bike"
else:
    transport = "Car"

print("Suggested transport is: ",transport)