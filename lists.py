# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 1:
        del list_to_remove_elements [0]
    if len(list_to_remove_elements) >= 5 or len(list_to_remove_elements)>= 6:
        del list_to_remove_elements [3]
    return list_to_remove_elements

list_to_remove_elements = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_elements(list_to_remove_elements))


def add_elements(list_to_add_elements):
     list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements

list_to_add_elements=  ['Red', 'Green', 'White', 'Black']
print(add_elements(list_to_add_elements))


def is_empty(list_to_check):
     return len(list_to_check) == 0

list_to_check= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(is_empty(list_to_check))


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        return list_to_compare1[2] == list_to_compare2[2]
    else:
        return False
    
list_to_compare1 = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
list_to_compare2 = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
print(check_lista(list_to_compare1, list_to_compare2))


def list_of_lists(list_of_lists_to_modify):
     result5 = []
    if len(list_of_lists_to_modify) >= 1:
        result5.append(list_of_lists_to_modify[0][:2])

    if len(list_of_lists_to_modify) >= 2:
        if len(list_of_lists_to_modify[1]) >= 4:
            result5.append(list_of_lists_to_modify[1][1:4])

    if len(list_of_lists_to_modify) >= 3:
        if len(list_of_lists_to_modify[2]) >= 2:
            result5.append(list_of_lists_to_modify[2][-2:])

    return result5

sample_list = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
print(list_of_list(sample_list))
