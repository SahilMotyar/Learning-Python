'''for loop = execute a block of code a fixed number of times.
              you can iterate over a range, string, sequence, etc.'''

for i in reversed(range(1,11,2)): #second number is exclusive
    print(i)

print("Happy new years!!")

# range function: we give a range and a step after the 2nd comma, to reverese a range we used reversed function.

credit_card = "1234-5678-9012-3456"

for i in credit_card:
    print(i)

for x in range(1,21):
    if x==13:
        continue #this section of code is used to skip over a number if we want
    else:
        print(x)
