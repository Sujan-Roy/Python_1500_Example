#
def new_list_zip_function(list1,list2):
    if (len(list1)!=len(list2)):
        print("The index is not equal")
    else:
        list3= zip(list1,list2)
        new_list=[i+j for i,j in list3]
        return new_list

list1= ["M","Na"]
list2= ["y","me"]
result= new_list_zip_function(list1,list2)
print(result)