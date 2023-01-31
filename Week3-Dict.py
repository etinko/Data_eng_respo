# Etienne
# Nkoume
# 2022-12-1-de-eastem
# 01/14/2023


import json
import pandas as pd
from faker import Faker
import secrets
import string

#1 creating the variable sen
sen = "The quick brown fox jumped over the lazy dog"
#2
print('the variable sen is ', sen)

#3
print("the variable sen type is", type(sen))

#4 Assigning variable to each word in sen
a = 'The'
b = 'quick'
c = 'brown'
d = 'fox'
e = 'jumped'
f = 'over'
g = 'the'
h = 'lazy'
i = 'dog'

#5 defining lst1
lst1 = [a, b, c, d, e, f, g, h, i]

#6
print('lst1 is ', lst1)

#7
print('lst1 type is ', type(lst1))

#8 creating lst2 from sen using string split function
lst2 = sen.split()

print('lst2 is ', lst2)
print('lst2 type is ', type(lst2))

#9 creating sen2 by using sen2 from lst2
sen2 = ' '.join(lst2)
print('sen2 is ',sen2)

#10 Creating and assigning new variables 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'i2' by using the String split() function
[a2, b2, c2, d2, e2, f2, g2, h2, i2] = sen.split(' ')
print(a2, b2, c2, d2, e2, f2, g2, h2, i2)



word = "Hello World"

another_word = ", I love Python"

#11 creating a dictionary
dict = {"hello": word, "love": another_word}

#12
print('my first dictionary is ', dict)

#13
e1 = dict["hello"]

#14
print('e1 is ', e1)

#15
print('the value of love is ',dict["love"])

#16  Make the console print "Hell or Python" using String slicing and the dictionary dict
print(word[0:4], word[-4:-2], another_word[-6:])

#17
dict2 = {'a3': a2, 'b3': b2, 'c3': c2, 'd3': d2, 'e3': e2, 'f3': f2, 'g3': g2, 'h3': h2, 'i3': i2}

#18
print(dict2)

#19
print('dict2 type is ', type(dict2))

#20
sen3 = ''
for k in dict2.values():
     sen3 = sen3 + " " + k
print('sen3 is ', sen3)




# creating a dictionary of us trucks
#21 - 24
us_trucks1 = {'make': 'Ford', 'model': 'F-150'}
us_trucks2 = {'make': 'Chevrolet', 'model': 'Silverado'}
us_trucks3 = {'make': 'Dodge', 'model': 'Ram 1500'}
us_trucks4 = {'make': 'Jeep', 'model': 'Gladiator'}

#25, 
print(us_trucks2)
#26
print(us_trucks3['make'])

#27 creating a list of dictionary
us_trucks_list = (us_trucks1, us_trucks2, us_trucks3, us_trucks4)
#28
print(us_trucks_list)
#29
print(us_trucks_list[1])

#30
#print(us_trucks_list[0][1]) # Got an error
#31
print(us_trucks_list[0]['make'])
#32
print(us_trucks_list[0]['model'])
# 33) Find and print the element in the list where the truck is made by Chevrolet.
print(us_trucks_list[1]['make'])
# 34) Print the element in the list where the truck is made by Jeep.
print(us_trucks_list[3]['make'])
# 35) Parse the model of the truck made by Jeep from the list and print it to the console.
print(us_trucks_list[3]['model'])

#36 Merging 2 dictionary with update methode
Merg_tucks1 = us_trucks1.update(us_trucks2)

print(Merg_tucks1)
# with ** methode
Merg_tucks2 = {**us_trucks1, **us_trucks2}
print(Merg_tucks2)

# 37 
dict1 = {'Dodge': 'Ram 150'}
#38
dict2 = {'Ford': 'F-150'}
#39
print(dict1)
#40
print(dict2)
#41
dict1.update(dict2)
#42
print(dict1)
#43
print(dict2)

#44 - 
dict1 = {'Dodge': 'Ram 150'} 
#45
dict2 = {'Ford': 'F-150'}
#47
dict3 = {**dict1, **dict2}
#48
print(dict1)
#49
print(dict2)
#50
print(dict3)

# 51)  read the 'new_families.txt' file and assign file variable
file = open('new_families2.txt','r')

#52)  Can you read the data in the file?  the file can't be printed, need to use for loop to read the fine one by one
# 53) What is the datatype of the file variable? IO text file
#  How can you read the data from the file variable? use the for loop to iterate the file
print('the file type is', type(file))
#54)  a FOR loop to iterate over the Text IO object 
for f in file:
   # print(file)
#55) What is the datatype of object returned in the iteration? a string
#56) changing a string variable into a list of dictionaries type
    json_in = f.replace("'", '"')
    new_f = json.loads(json_in)
#57) Now that you have a list, print only the second item from the list. 
print(new_f[1])
#What is its type? it is a dictionary
print(type(new_f[1]))

print(new_f[0]['Father'])
print(new_f[0]['Mother'])
#print(new_f[0]['Son'])

new_lst1 = [1, 2, 3]
new_lst2 = ['a', 'b', 'c']
new_lst3 = new_lst1 + new_lst2
print(new_lst3)


def data_generator(records):
    fake = Faker('en_us')

    customers = []

    for i in range(records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        street_address = fake.street_address()
        city = fake.city()
        state = fake.state_abbr()
        zip = fake.postcode()
        email = str.lower(f'{first_name}.{last_name}@domaine.com')
        phone_number = fake.phone_number()
        loyalty_acct = ''.join(secrets.choice(string.digits)for i in range(5))

        customers.append({
            'first_name': first_name,
            'last_name':last_name,
            'street_address':street_address,
            'city':city,
            'state':state,
            'zip':zip,
            'email':email,
            'Phone_number':phone_number,
            'loyalty_acct':loyalty_acct
            })
    return customers

df = pd.DataFrame(data_generator(1000))

df_to_csv = df.to_csv('customer_data.csv', index = False)