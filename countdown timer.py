import time

my_time = int(input("Enter the time (in seconds): "))

for x in range(my_time,0,-1):
    seconds = x % 60 # we used %60 because we don't want to go over 60 seconds
    minutes = int(x/60) % 60
    hours = int(x/3600) 
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # :02 is a format specifier where it does the padding with 0 for 2 places
    time.sleep(1) # our program will sleep for a given amount of time, before starting again. 

print("Time's up")