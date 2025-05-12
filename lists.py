def remove_elements (list_to_remove_elements):
	len_lista= len(list_to_remove_elements)
	if len_lista>= 6 :
		del list_to_remove_elements [5]
		del list_to_remove_elements [4]
		del list_to_remove_elements [0]
		return list_to_remove_elements
	elif len_lista ==5 :
		del list_to_remove_elements[4]
		del list_to_remove_elements [0]
		return list_to_remove_elements
	elif len_lista<5 and len_lista>= 1:	
		del list_to_remove_elements [0]
		return list_to_remove_elements	
	else:
		return []
def add_elements (list_to_add_elements):
	list_to_add_elements.append("Yellow")
	list_to_add_elements.insert(0,"Pink")		
	return list_to_add_elements
def is_empty (list_to_check):
	if list_to_check == []:
		return True 	
	else:
		return False

def check_lists(list_to_compare1,list_to_compare2):
	lista1= list_to_compare1
	lista2= list_to_compare2
	if len (lista1)	>= 3 and len (lista2) >=3:
		if lista1[2]==lista2[2]	:
			valor= True
		else:
			valor= False
	else:
		valor=False
	return valor

def list_of_lists(list_of_lists_to_modify):
	sub1= list_of_lists_to_modify[0]
	sub2= list_of_lists_to_modify [1]	
	sub3= list_of_lists_to_modify [2]	
	if len(sub1)>0:
		sub1=sub1[0:2]
	else:
		sub1=[]
	if len(sub2)>= 2 :
		sub2=sub2[1:4]
	else:
		sub2=[]
	if len (sub3) > 0:
		sub3=sub3[-2:]	
	todo=[sub1, sub2, sub3]
	return todo			
