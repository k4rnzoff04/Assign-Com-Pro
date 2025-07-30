kiloperh = int(input("Enter the speed in kilometers per hour: "))

for kiloperh in range(50, kiloperh, 10):
    miles_per_hour = kiloperh * 0.6214
    print(f"{kiloperh} km/h is approximately {miles_per_hour:.2f} mph")

