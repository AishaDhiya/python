num=input( " enter list of numbers : " )
list1=[]
list1=[int(i)for i in num.split()]
list2=[ i for i in num.split()]
print(" ACTUAL LIST =",list1)
print(" POSITIVE NUMBERS IN LIST =" , list2)
