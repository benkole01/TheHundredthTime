print('Ben Kole Coding...')

print('o----')
print(' |||| ')
print('*' * 10)
print('Ben ! ' * 3 )

"""
VARIABLES - Containers that store information
"""

website = 'thejobsaround.com'
print(f'My new website is found at: {website}')

pie = 22/7
radius = 14
area = pie * radius**2
print(f'The area of a circle with radius {radius} is : {area}')

"""
RECEIVE INPUT FROM USERS
"""

# Ask a user their name and print it
name = input('What is your name? ')
print('Hi ' + name) # concatenating

# Ask a user their name and color
name = input('What is your name? ')
color = input('What is your favorite color? ')
print(name + ' likes ' + color)


"""
TYPE CONVERSION
"""
birth_year = input('Birth Year: ')
age = 2022 - int(birth_year)
print('Your age is: ' + str(age))

# Tell me your weight
weight_pound = int(input('What is your weight in pounds? '))
weight_kg = weight_pound * 0.454
print('You are currently weighing ' + str(weight_kg) + 'kgs')

# The above code in another version
# input function is a string by default
weight_pound = input('Please tell me your weight in pounds again ')
weight_kg = int(weight_pound) * 0.454 #converts to integer
print('Alright, You are weighing ' + str(weight_kg) + ' pounds')

"""
PYTHON STRINGS
"""
# Why am I coding now?
coding_moment = "Ben Kole's hundredth time of learning Python"
print(coding_moment)

# Send an email to Ben Kole offering him a job as a Python Security Officer
email = """
SUBJECT: JOB OFFER AS PYTHON SECURITY OFFICER

Hello Ben Kole,

So after looking at your recent Python codes,

We realized you have been learning Python for more than hundred times

And we thought it would be a good time to consider you 

For a position in our company as a Top Python Security Officer

We know you are currently running more than two websites online

Please tell us if you are okay to take this kind offer from us

We look forward to hearing back from you

Yours Sincerely,
Juli Mian
The Console Company
"""

print('KINDLY DELIVER THIS EMAIL TO BEN KOLE')
print(email)


############################
# INDEXING
############################

name = 'Jennifer Lopez'
print(name[1:-1])
print(name[::])

############################
# STRING FORMATING
############################
name = 'Ben Kole'
nationality = 'Kenyan'
age = 23
zodiac_sign = 'Pisces'

print(name + ' is a Tech Author and Editor at BENKOLE.COM')

# Formatted version
print(f'{name} is a Tech Author and Editor at BENKOLE.COM')

# Or
print('{} is a Tech Author and Editor at BENKOLE.COM'.format(name))
print('The first traveller on board is {}, who is a {}'.format(name,nationality))


############################
# STRING FUNCTIONS AND METHODS
############################
verdict = 'All Programmers are Psychopaths'

print(len(verdict)) #the total number of characters in this string

# Methods...
print(verdict.upper())
print(verdict.lower())

print(verdict.split()) #returns a list of individual words forming the string
print(verdict.replace('Psychopaths','Kind'))

# Does our string have the word 'Programmers'?
print('Programmers' in verdict)

#Find where the word 'Programmers' first appears
print(verdict.find('Programmers'))


"""
ARITHMETIC OPERATIONS
"""

# Two types of division operator
print(20 / 3) #returns the actual result
print(20 // 3) #returns only the integer value of the result

# modulus operator (%) - returns the remainder of a division
print(20 % 3)

# power operaror (**)
print(10**2)

############################
# OPERATOR PRECEDENCE
############################

# Order of Operation, guided by BODMAS
# parenthesis
# exponentiation
# multiplication or division
# addition or subtraction

x = 10 + 4 / 2 * 3
print(x)

y = 10 + 4 / 2 * 3**3
print(y)

z = (10 + 4) / 2 * 3**3
print(z)


"""
MATH FUNCTIONS
"""

x=3.5
# round off to the nearest number
print(round(x))

# get the absolute of a number (always a positive number)
print(abs(-3.555))

# math module - contains lots of mathematical functions
# suitable for complex mathematical calculations

import math

print(math.cos(45))
print(math.ceil(3.5))
print(math.floor(3.5))


"""
IF STATEMENTS
"""

'''
if it's hot
    It's a hot day
    Wear light clothes
    
otherwise if it's cold
    It's a cold day
    Wear warm clothes
    
otherwise
    It's a lovely day
'''

# It's hot today
day_hot = True

if day_hot:
    print("It's a hot day \nWear light clothes")
else:
    print("It's a lovely day")


# It's cold today
day_hot = False
day_cold = True

if day_hot:
    print("It's a hot day \nWear light clothes")

elif day_cold:
    print("It's a cold day \nWear warm clothes")
else:
    print("It's a lovely day")


# It's neither hot nor cold today
day_hot = False
day_cold = False

if day_hot:
    print("It's a hot day \nWear light clothes")

elif day_cold:
    print("It's a cold day \nWear warm clothes")
else:
    print("It's a lovely day")

'''
Price of a house is $1M
If buyer has good credit,
    they put down 10%
Otherwise
    they put down 20%
Print the down payment
'''

house_price = 1000000

# buyer has good credit
good_credit = True

if good_credit:
    down_payment = house_price * 0.1
    print(f'You have good credit \nPay: {down_payment} dollars')
else:
    down_payment = house_price * 0.2
    print(f'You have bad credit \nPay: {down_payment} dollars')


# buyer has bad credit
good_credit = False

if good_credit:
    down_payment = house_price * 0.1
    print(f'You have good credit \nPay: {down_payment} dollars')
else:
    down_payment = house_price * 0.2
    print(f'You have bad credit \nPay: {down_payment} dollars')


"""
LOGICAL OPERATORS
"""
# AND - BOTH CONDITIONS MUST BE TRUE
# OR - ONE CONDITION MUST BE TRUE
# NOT - Makes a False Condition True, and a True Condition False


"""
COMPARISON OPERATORS
"""
'''
> Greater than
< Less than
== equal to
!= not equal to

'''
temperature = 30
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

'''
if name is less than 3 characters long
    name must be at least 3 characters
otherwise if it's more than 50 characters long
    name can be a maximum of 50 characters
otherwise
    name looks good!
'''

name = input('Enter your name: ')

if len(name)<3:
    print('Name must be at least 3 characters')
elif len(name)>50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good!')


#### THIS IS A WEIGHT CONVERTER

weight = input('Weight: ')
response = input('(L)bs or (K)g: ')

if response.upper() == 'L':
    weight_kg = int(weight) * 0.454
    print(f'You are {weight_kg} kilos')
elif response.upper() == 'K':
    weight_pound = int(weight) * 2.20
    print(f'You are {weight_pound} pounds')
else:
    print("I DON'T KNOW WHAT YOU ARE TALKING ABOUT!")