'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

# unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6), ('fourth element', 1)]
print('unsorted list is: ' + str(unsorted_list))
sorted_list = []

values = []
for tuple_ in unsorted_list:
    values.append(tuple_[1])

while len(values) > 0:
    min_value = min(values)
    min_index = values.index(min_value)
    sorted_list.append(unsorted_list.pop(min_index))
    values.pop(min_index)

print('sorted list is:' + str(sorted_list))
