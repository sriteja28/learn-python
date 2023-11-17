'''
Avalible logical operators

<
>
<=
>=
==
!=
'''

password = input('Do you know the secret password? ')
if password != '--secret':
    print('not correct')
else:
    print('correct password')

if True:
    print('Condition met')

if False:
    print('Condition not met')

if 2 ==2:
    print('true')

if 1 == 2:
    print('true')

if 2 == 2.0:
    print('true')