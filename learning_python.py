''' string slicing: creating substring from another string
                    we can use 2 methods indexing[] or slice()
                                         [start:stop:step] '''

name = "Sahil Motyar"

first_name = name[0:5]
last_name = name[6:] #we can leave the starting and the ending index, program will assume the values
funky_name = name[::2] #using the step function, we can leave the starting and ending index if we are using the whole string
reversed_name = name[::-1] #reversing the string
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


#slicing

website1 = "https://google.com"
website2 = "https://facebook.com"

slice = slice(8,-4) #using the stop as negative index to take out a specific part of the site, names are of different lengths
print(website1[slice])
print(website2[slice])
