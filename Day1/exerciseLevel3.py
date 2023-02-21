temp = 37
print(temp)
age = 41
print(age)
famiy_size = 25
print(famiy_size)
weiht_kg = 56.7
print(weiht_kg)
height_m = 17.6
print(height_m)

#complex_num
angle_1 = (2-7j)
angle_2 =(3+5j)
angle_3 = (1 - 1j) 
print(angle_1, angle_2, angle_3)

#strings
my_son = 'Abdulladeef'
my_daughter = 'Khadija'
my_dish = 'semo_da_kubewa'
print(my_daughter, my_dish, my_son)

#boolian
are_you_alive = True
are_you_bad = False
print('are are_you_alive?', are_you_alive)
print('are_you_bad?', are_you_bad)

#Dictionary
Bio_data = {
'first_name':'Abdul',
'last_name':'Yusuf',
'country':'Nigeria', 
'age': 'about 42', 
'is_married':False,
'skills':['teaching', 'painting', 'sleeping', 'Python']
}
print('\n\nthis ois an exaple of Dictionary \n', Bio_data)

#tuple and list
print('\n\n This is examples of tuple and List')
tpl = ('Abdulladeef', 'Sani', 'Muhammad', 'Abraham', 'Lidiya') #tuple
lst = ['Sani', 'Pawel', 'Halima', 'Abraham', 'Khadiya'] #list

print(tpl)
print(lst)

#set exapmples
set_example = {'Abdulladeef', 'Sani', 'Muhammad', 'Abraham'}
set_example_num = {1,4,6,9,10}
print('\n\nThese are examples of set \n', set_example)
print(set_example_num)

#Ecledian distance
import math
a = 10 -2
b = 8 - 3
c = a**2 + b**2
distance = math.sqrt(c)
print('\n\n the ecledian distance of 2,3 and 10,8 is ', distance)
