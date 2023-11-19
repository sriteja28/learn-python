name_original = 'Jon Snow'
name_new = name_original
name_original = 'Deanerys Targeryon'
print(name_original, name_new)

lists_original = [1,2,3]
list_new = lists_original
lists_original[0] = -5
print('Original', lists_original, '\nNew', list_new)

lists_original = [1,2,3]
list_new = lists_original[:]
lists_original[0] = -5
print('Original', lists_original, '\nNew', list_new)

lists_original = [1,2,3]
list_new = lists_original[:2]
lists_original[0] = -5
print('Original', lists_original, '\nNew', list_new)