invited_guests = ['Kate', 'Adam','Kerry', 'Joe','Anne','Marie']
name = input('Enter your name: ')
if name in invited_guests:
    print('Welcome')
else:
    print('You are not invited')

invited_guests = ['Kate', 'Adam','Kerry', 'Joe','Anne','Marie']
name = input('Enter your name: ')
if name not in invited_guests:
    print('You are not invited')
else:
    print('Welcome')