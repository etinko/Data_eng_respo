# Etienne
# Nkoume
# 2022-12-1-de-eastem
# 01/21/2023


lst1 =  ['1', '2', [3]]
lst2 =  [('3', 4), '5', 6]
# joining lst1 and lst2 to create lst3
lst3 = []  
# iterating through lst1 and lst2 to add interger and string in lst3 and flatening the list of the list
for item in (lst1 + lst2):   
    if type(item) is int:
            lst3.append(item)
    else:
         for i in item:
            lst3.append(i)       
print('the new list with only string and interger is ', lst3)
#4 Creating a new distionary by iterating through lst3 and adding odds number to key odds and evens numbers to key evens
odds_evens = {}
even=[]
odd=[]
for i in lst3: 
    if int(i)%2 == 0: # force read a string number
        even.append(i)
    else:
        odd.append(i)       
odds_evens['Even']=even
odds_evens['Odd']=odd
print('the odds_evens dictionary is ', odds_evens)

#5 list comprehension to create a liste of interger
number = [int(i) for i in lst3]
print('the new list of interger from lst3 is ', number)

#6 converting string to interger in odds_evens dictionary
for k in odds_evens:
     odds_evens[k] = [int(i) for i in odds_evens[k]]
    
print(odds_evens)

#7 dictionary comprehension to add max of number to odds_evens dictionary
Max_odds_evens = {k:[int(i) + max(number) for i in odds_evens.values()] for (k,v)in odds_evens.items()}
print([i  for i in odds_evens.values()])

#8 adding error handling