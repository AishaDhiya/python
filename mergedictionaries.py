dict1 = {'a':10 , 'b':8, 'c':6}
dict1 = {'a':4, 'e':2, }
for key in dict1:
	if key in dict2:
		dict2[key]=dict2[key]+dict1[key]
	else:
			dict2[key]=dict1[key]
			print(dict2)
