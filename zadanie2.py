
def sum_of_values(dict1):
    values = 0
    for i in dict1.values():
        values += i
    return values

dict1 = {'data1': 10.5,
             'data2': -4,
             'data3': 2}
print(sum_of_values(dict1))
