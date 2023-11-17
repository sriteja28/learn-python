# Boolean operators
'''
and
or
not
'''

#and
user_age = int(input('What is your age? '))
user_country = input('What is your country? ')
if user_age < 25 and user_country == 'Germany':
    print('You can apply for German student exchange programme')
else:
    print('Sorry, you do not qualify')

# or
user_country = input('What is your country? ')
if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for Scandinavian student exchange programme')
else:
    print('Sorry, you dont qualify')

#not
user_country = input('What is your country? ')
if not user_country == 'Germany':
    print('You are not from Germany')
else:
    print('you are from germany')

# all conditions
user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if ((not user_country == 'Germany') and user_age < 25) or \
    (user_country == 'Germany' and user_age < 23):
    print('You Qualify')
else:
    print('you dont Qualify')

'''
Priority is
1. not
2. and
3. or
'''