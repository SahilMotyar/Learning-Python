# python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle<=0:
        print("principle cannot be less than or equals to zero")

print(principle)

while rate <= 0:
    rate = float(input("Enter the Interest rate: "))
    if rate<=0:
        print("Interest rate cannot be less than or equals to zero")

print(rate)

while time <= 0:
    time = int(input("Enter the Time period (in yrs): "))
    if time<=0:
        print("Time period cannot be less than or equals to zero")

print(time)

total = principle*pow((1 +rate/100),time)
print(f"Balance after {time} year/s: ${total:.2f}")

