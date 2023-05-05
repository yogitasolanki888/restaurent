# class DataManipulator:
#     def __init__(self):
#         self.data_list = []
#         self.data_tuple = ()
#         self.data_dict = {}
#         self.data_set = set()

#     # Create data
#     def create_list(self, data):
#         self.data_list.append(data)

#     def create_tuple(self, data):
#         self.data_tuple += (data,)

#     def create_dict(self, key, value):
#         self.data_dict[key] = value

#     def create_set(self, data):
#         self.data_set.add(data)

#     # Update data
#     def update_list(self, index, data):
#         self.data_list[index] = data

#     def update_tuple(self, index, data):
#         temp_list = list(self.data_tuple)
#         temp_list[index] = data
#         self.data_tuple = tuple(temp_list)

#     def update_dict(self, key, value):
#         self.data_dict[key] = value

#     def update_set(self, data):
#         self.data_set.add(data)

#     # Delete data
#     def delete_list(self, index):
#         del self.data_list[index]

#     def delete_tuple(self, index):
#         temp_list = list(self.data_tuple)
#         del temp_list[index]
#         self.data_tuple = tuple(temp_list)

#     def delete_dict(self, key):
#         del self.data_dict[key]

#     def delete_set(self, data):
#         self.data_set.remove(data)

#     # Search data
#     def search_list(self, data):
#         return data in self.data_list

#     def search_tuple(self, data):
#         return data in self.data_tuple

#     def search_dict(self, key):
#         return key in self.data_dict.keys()

#     def search_set(self, data):
#         return data in self.data_set

#     # Get data
#     def get_list(self):
#         return self.data_list

#     def get_tuple(self):
#         return self.data_tuple

#     def get_dict(self):
#         return self.data_dict

#     def get_set(self):
#         return self.data_set
# data_manipulator = DataManipulator()
# data_manipulator.create_list(1)
# print(data_manipulator.get_list())  # Output: [1]


import datetime
latest=datetime.datetime(2023,4,19)
latest_date=latest.strftime('%y-%m-%d')
oldest=datetime.datetime(2023,4,8)
oldest_date=oldest.strftime('%y-%m-%d')
print(latest_date)
print(oldest_date)
































# class DataStructureCRUD:
#     def __init__(self):
#         self.data = None

#     def create_data(self, data_structure, data):
#         if data_structure == 'list':
#             self.data = list(data)
#         elif data_structure == 'tuple':
#             self.data = tuple(data)
#         elif data_structure == 'dictionary':
#             self.data = dict(data)
#         elif data_structure == 'set':
#             self.data = set(data)

#     def update_data(self, data_structure, index_or_key, new_value):
#         if data_structure == 'list':
#             self.data[index_or_key] = new_value
#         elif data_structure == 'tuple':
#             temp_list = list(self.data)
#             temp_list[index_or_key] = new_value
#             self.data = tuple(temp_list)
#         elif data_structure == 'dictionary':
#                self.data[index_or_key] = new_value
#         elif data_structure == 'set':
#                self.data.remove(index_or_key)
#                self.data.add(new_value)

#     def delete_data(self, data_structure, index_or_key):
#         if data_structure == 'list':
#             del self.data[index_or_key]
#         elif data_structure == 'tuple':
#             temp_list = list(self.data)
#             temp_list.pop(index_or_key)
#             self.data = tuple(temp_list)
#         elif data_structure == 'dictionary':
#             del self.data[index_or_key]
#         elif data_structure == 'set':
#             self.data.remove(index_or_key)

#     def search_data(self, data_structure, search_value):
#         if data_structure == 'list':
#             return search_value in self.data
#         elif data_structure == 'tuple':
#             return search_value in self.data
#         elif data_structure == 'dictionary':
#             return search_value in self.data.values()
#         elif data_structure == 'set':
#             return search_value in self.data

#     def get_data(self):
#         return self.data
# my_data_structure = DataStructureCRUD()
# lst= [1,2,3,4,5]
# tup=(11,23,45,56)
# dic={"fname": "yogita","lname":"solanki"}
# s={1,2,3,4}
# # Create data
# my_data_structure.create_data('list', lst)
# print(my_data_structure.get_data())  

# my_data_structure.create_data('tuple', tup)
# print(my_data_structure.get_data())  

# my_data_structure.create_data('dictionary', dic)
# print(my_data_structure.get_data())  

# my_data_structure.create_data('set', s)
# print(my_data_structure.get_data()) 

# # # # Update data
# my_data_structure.update_data('list',  1, 4)
# print(my_data_structure.get_data()) 

# my_data_structure.update_data('tuple', 2, 'd')
# print(my_data_structure.get_data()) 

# my_data_structure.update_data('dictionary','branch', 'cse')
# print(my_data_structure.get_data())  

# my_data_structure.update_data('set', 2, 4)
# print(my_data_structure.get_data()) 
