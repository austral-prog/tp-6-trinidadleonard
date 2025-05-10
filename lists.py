def remove_elements(list_to_remove_elements):
    len_lista = len(list_to_remove_elements)
	if len_lista >= 1 and len_lista < 5:
		del list_to_remove_elements[0]
		return list_to_remove_elements
	elif len_lista == 5:
		del list_to_remove_elements[4] 
		del list_to_remove_elements[0]
		return list_to_remove_elements
	elif len_lista >= 6:
		del list_to_remove_elements[5] 
		del list_to_remove_elements[4]
		del list_to_remove_elements[0]
		return list_to_remove_elements
	else:
		return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, 'Pink')
	list_to_add_elements.append('Yellow')
	return list_to_add_elements

def is_empty(list_to_check):
    len_lista = len(list_to_check)
	if len_lista == 0:
		return "True"
	else:
		return "False"

def check_lists(list_to_compare1, list_to_compare2):
    len1 = len(list_to_compare1)
	len2 = len(list_to_compare2)
	if len1 >= 3 and len2 >= 3:
		if list_to_compare1[2] == list_to_compare2[2]:
			return "True"
		else:
			return "False"
	else:
		return "False"

def list_of_lists(list_of_lists_to_modify):
    list0 = list_of_lists_to_modify[0]
	list1 = list_of_lists_to_modify[1]
	list2 = list_of_lists_to_modify[2]
	if len(list0) > 2:
		list0_new = [list0[0],list0[1]]
	else:
		list0_new = list0
	len1 = len(list1)
	if len1 == 2:
		list1_new = [list1[1]]
	elif len1 == 3:
		list1_new = [list1[1],list1[2]]
	elif len1 >= 4:
		list1_new = [list1[1],list1[2],list1[3]]
	else:
		list1_new = []
	if len(list2) > 2:
		list2_new = [list2[-2],list2[-1]]
	else:
		list2_new = list2
	final_list = [list0_new, list1_new, list2_new]
	return final_list
