# python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle<0:
        print("principle cannot be less than zero")
    else:
        break

# print(principle)

while True:
    rate = float(input("Enter the Interest rate: "))
    if rate<0:
        print("Interest rate cannot be less than zero")
    else:
        break

# print(rate)

while True:
    time = int(input("Enter the Time period (in yrs): "))
    if time<0:
        print("Time period cannot be less than zero")
    else:
        break

# print(time)

total = principle*pow((1 +rate/100),time)
print(f"Balance after {time} year/s: ${total:.2f}")

