top_cities = ['New York', 'Los Angles', 'Chicago', 'Houston', 'Phoenix']
for city in top_cities:
    print('Current City', city)

top_cities = ['New York', 'Los Angles', 'Chicago', 'Houston', 'Phoenix']
for city_index in range(len(top_cities)):
    print('Current Index:', city_index, '| Current city:', top_cities[city_index], )

spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings:
    sum += spending
print('Money Spent:', sum)