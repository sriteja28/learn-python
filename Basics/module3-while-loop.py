'''
loops
while
for
'''

counter = 1
while counter < 11:
    print(counter)
    counter += 1
print('Finished')

secret_number = 14
print('''
========================
===SECRET NUMBER GAME===
========================
''')
user_input = int(input('Try to guess a number from 0 to 20: '))
while user_input != secret_number:
    print('wrong')
    user_input = int(input('Try to guess a number from 0 to 20: '))
print('Perfect, you guessed correct')