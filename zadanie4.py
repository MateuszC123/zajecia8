"""
def znak(napis):
    dict1 = {}
    for i in napis:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1
print(znak("samochodaa"))
"""

def znak(napis):
    dict1 = {}
    for i in napis:
      dict1[i] = dict1.get(i, 0) + 1
    return dict1

dict2 = znaki("samochódao")
for i in sorted(dict_2.keys()):
    print(i, dict_2[i])