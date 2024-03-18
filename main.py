def add_element(lst, element):
    lst.append(element)
    return lst

#Usage
my_list = [1, 2, 3]
my_list = add_element(my_list, 4)
print(my_list)

#-------------------------------

def extend_list(lstl, lst2):
    lstl.extend(lst2)
    return lstl

#Usage
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1 = extend_list(list1, list2)
print(list1)