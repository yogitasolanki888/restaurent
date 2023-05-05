class Operation:

    def create_list_element(self, my_list,element):
        my_list.append(element)
        return my_list

    def get_list_element(self,my_list, index):
        return my_list[index]

    def update_list_element(self,my_list, index, new_value):
        my_list[index] = new_value
        return my_list

    def delete_list_element(self,my_list, index):
        del my_list[index]
        return my_list

    def search_list(self,my_list, ele):
        if ele in my_list:
         return ele

    def read_list(self,my_list):
        return my_list
my_list = []
n = int (input ("Enter number of elements: ")) 
for i in range(n):
    x=int(input())
    my_list.append(x)
# my_list = [1, 2, 3]
obj= Operation()
print(obj.create_list_element(my_list, 4))
print(obj.get_list_element(my_list, 1) ) 
print(obj.update_list_element(my_list, 1,6) )
print(obj.delete_list_element(my_list, 0) )   
print(obj.search_list(my_list,5))
print(obj.read_list(my_list))

