# first = input('Enter first number: ')
# second = input('Enter second number: ')
# print('Before swapping', first, second)
# first = second
# second = first
# print('After swapping', first, second)


# first = input('Enter first number: ')
# second = input('Enter second number: ')
# print('Before swapping', first, second)
# temporary = first
# first = second
# second = temporary
# print('After swapping', first, second)


# first = input('Enter first number: ')
# second = input('Enter second number: ')
# print('Before swapping', first, second)
# first, second = second, first
# print('After swapping', first, second)

top_cities = ['New York', 'Los Angles', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

top_cities = ['New York', 'Los Angles', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort()
print(top_cities)

random_numbers = [2, 5, -1, 0, -3, 4]
random_numbers.sort()
print(random_numbers)

random_numbers = [2, 5, -1, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)

top_cities = ['New York', 'Los Angles', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)