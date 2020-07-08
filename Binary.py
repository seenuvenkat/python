def binary_search(item_list,item):
	f = 0
	l = len(item_list)-1
	found = False
	while( f<=l and not found):
		m = (f + l)//2
		if item_list[m] == item :
			found = True
		else:
			if item < item_list[m]:
				l = m - 1
			else:
				f = m + 1	
	return found
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))
