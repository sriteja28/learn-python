fav_band = 'Green Day'
print(fav_band[6])

print(fav_band[:6])

text = 'please capatilise me'
text_cap = text.upper()
print(text_cap)

user_number = input('Plese provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number')
else:
    print('Sorry,', user_number, 'is not a number')