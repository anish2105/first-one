#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello')


# In[2]:


first=input("How r u")


# In[3]:


print("Welcome")

ask=input("How r u:")

print("You have responded with " + ask)


# In[4]:


#data types


# In[5]:


#1.Numbers
num_one = 205
float_one=9.6


# In[6]:


type(num_one)


# In[7]:


type(float_one)


# In[8]:


#2.Strings
text = 'Hi my name is Anish'


# In[9]:


type(text)


# In[10]:


#3.List
a_list = [3,4,'hi',5,7,[1,2,3]]


# In[11]:


type(a_list)


# In[12]:


#4.dictionaries
my_dict = {'john': 2,'johnny':3}


# In[13]:


type(my_dict)


# In[14]:


print(7)
str(7)


# In[15]:


num=5
string = ' hi'
str(num)+string


# ***
# operations : +  -  *  /  **  %
# comparsion: >  <  >=  <=  ==  !=
# logical operators: and   or
# ***
# 
# 

# In[16]:


#format

name = 'John'
age = '30'
hobby = 'hiking'

print("{} is {} and his hobby is {} ".format(name,age,hobby))


# In[17]:


Name = input("Your name: ")
Number1 = int(input("Enter the first number: "))
Number2 = int(input("Enter the second number: "))
Number3 = int(input("Enter the third number: "))
result = (Number1+Number2)*Number3
print(" Your name is {} , you have entered {},{}&{} and the result is {}".format(Name,Number1,Number2,Number3,result))


# In[18]:


pound = int(input("Enter weight in pounds: "))
kg = 0.453592*pound
print("In kgs it is {} ".format(kg))


# In[19]:


#Modules
import random as rn


# In[20]:


rn.randint(10,20)


# In[21]:


roll4 = rn.randint(1,6)    #pratical
roll5 = rn.randint(1,6)
tot = roll4 + roll5
print("First dices rolled:{} Second dices rolled:{} ,Combined total = {}".format(roll4,roll5,tot))


# In[22]:


#if/elif/else
max_temp = 40
min_temp = 10
current_temp = 30

if current_temp > max_temp:
    print("Above safe level")
elif current_temp < min_temp:
    print("Temp levels low")
else:
    print("Everything is fine")


# In[23]:


#pratical
numb = rn.randint(1,10)
user = int(input("What is your guess:"))
if user == numb:
    print("You made a correct guess")
elif user < numb:
    print("Your guess was less than actual number.")
elif user > numb:
    print("Your guess was high than actual number.")
print("Your guess is {} , The number is {}".format(user,numb))


# In[24]:


#pratical
color = ["red","green","blue","yellow"]
parts = ["left leg","left hand","right leg","right hand"]
print(rn.choice(color) + " and " + rn.choice(parts))


# In[25]:


#List Methods
mylist = [1,56,4,32]


# In[26]:


#append
mylist.append(1000)
print(mylist)


# In[27]:


#remove
mylist.remove(1)
print(mylist)


# In[28]:


#pop
mylist.pop()
print(mylist)


# In[29]:


#sort
mylist.sort()
print(mylist)


# In[30]:


#reverse
mylist.reverse()
print(mylist)


# In[31]:


#List functions
#Length 
len(mylist)


# In[32]:


#min
min(mylist)


# In[33]:


#max
max(mylist)


# In[34]:


#list indexes
mylist1 = [1,4,7,[2,3,4,5],8,9]
a = mylist1[2]
b = mylist1[3][0]
print(a)
print(b)


# In[35]:


#list slicing
mylist2 = [1,66,7,'bear',5700,'cheese',8,7000,11,43]
mylist2[1:8:2]


# In[36]:


#pratical
list1=[1,2,3,4]


# In[37]:


list1.pop()
print(list1)


# In[38]:


list1.append([9,0,11,12])


# In[39]:


print(list1)


# In[40]:


z=list1[4][:2]
z[::-1]


# In[ ]:


y = list1[5][1:]


# In[ ]:


y[::-1]


# In[ ]:


#for loop
#Executing code a certain number of times
for i in range(10):
    print("Elements are : {}".format(i))


# In[ ]:


#Iterationg through datasets(e.g.lists)
my_list = [1,2,3,4,5,6]
for j in my_list:
    print(j)


# In[ ]:


#continue and break
fruit_list = ["apple","pear","banana","kiwi"]


# In[ ]:


for fruit in fruit_list:
    if fruit == "banana":
        continue
    else:
        print(fruit)


# In[ ]:


for fruit in fruit_list:
    if fruit == "banana":
        break
    else:
        print(fruit)


# In[ ]:


#list comprehension


# In[ ]:


#Quick way to create new lists
list1 = [i for i in range(5)]
print(list1)


# In[ ]:


#Quick way to create new lists with conditions (if x%2==0)
my_odd_list = [j for j in range(15) if j%2!=0]
print(my_odd_list)


# In[ ]:


#Means to filter through a list with new conditions
new_fruit = [fruit for fruit in fruit_list if fruit!= "banana"]
print(new_fruit)


# In[ ]:


#Tuple() and Sets{}
my_list5 = [1,2,3,4,5]
my_list5[1]=100
print(my_list5)


# In[ ]:


#in tuples u cant change the values once delaraced
my_tuple = (1,2,3,4,5)
my_tuple[1] = 100


# In[ ]:


# in sets all the values in the list when printed gives only once and in sorted manner
my_set = {22,1,2,3,22,4,4,4,'tiger','tiger'}
print(my_set)


# In[ ]:


#Dictoraries
my_dict = {'john':30,'Anna':29,'Fiona':29}


# In[ ]:


my_dict['Anna']


# In[ ]:


for pair in my_dict:
    print(pair)


# In[ ]:


for pair in my_dict:
    print(my_dict[pair])


# In[ ]:


#adding an element in a dict
my_dict['phil'] = 26
print(my_dict)


# In[ ]:


#deleting an element from a list 
my_dict.pop('phil')


# In[ ]:


print(my_dict)


# In[ ]:


#pratical
currency = {'usd':75.22,'pound':101.02,'yen':1.52,'dirham':20.45 }


# In[ ]:


user_in = int(input("Enter amount in INR: "))
convert_currency = input("Enter the currency they want to convert INR to: ")

if convert_currency == 'usd':    
    converted = user_in * currency[convert_currency]
elif convert_currency == 'pound':
    converted = user_in * currency[convert_currency]
elif convert_currency == 'yen':
    converted = user_in * currency[convert_currency]
elif convert_currency == 'dirham':
    converted = user_in * currency[convert_currency]
else:
    print("Enter currency in usd ,pound ,yen or dirham")
print("{} INR = {}{} ".format(user_in,converted,convert_currency))


# In[ ]:


#while loop in games
play = True

while play == True:
    real_number = 10
    user_guess = int(input("Enter your guess: "))
    if real_number == user_guess:
        play = False
print("Game ended")


# In[ ]:


import random as rn


# In[ ]:


play = True
computer = rn.randint(1,10)

while play == True:
    user_guess = int(input("Enter your guess (from 1 to 10): "))
    if user_guess != computer:
        print("try again")
    else:
        print("You have guessed it correct")
        break
        
    


# In[ ]:


#practical
life = 5
computer = rn.randint(1,15)

while play == True:
    user_guess = int(input("Enter your guess (from 1 to 15): "))
    if user_guess != computer:
        life = life - 1
        print("Life remaining = {}".format(life))
        if(life == 0):
            print("Game over")
            break
        else:
            print("try again")
    else:
        print("You have guessed it correct")
        print("Life remaining = {}".format(life))
        break
        


# #functions
# #instead of 
# 
# 
# '''
# 
# if person = 'bill':
#     print("have a good day")
# elif person = 'mindy':
#     print("have a good day")
# ...n so on
#     
# use functions
# '''

# In[ ]:


def welcome_function():
    print("Have a good day")


# In[ ]:


person = 'id'
if person == 'bill':
    welcome_function()
elif person == 'mindy':
    welcome_function()
else:
    print("Wassup")
        


# In[ ]:


#function paramaters
def multiplier(first,sec):
    third = first * sec
    print(third)


# In[ ]:


multiplier(4,7)


# In[ ]:


def greet(name):
    print("Hello {},Have a good day".format(name))


# In[ ]:


greet('Anish')


# In[41]:


#requests
import requests
url = 'http://www.google.com'
requests.get(url)


# In[42]:


response = requests.get(url)
response.content


# In[43]:


#json
#example api = 'https://api.echangerate-api.com/v4/lastest/USD'
#u have to know whether the website is in json form or not before only to use .json()
#.json is like .content


# In[44]:


currencyurl = 'https://openexchangerates.org/api/currencies.json'
response = requests.get(currencyurl)


# In[45]:


data = response.json()


# In[46]:


data['AED']


# In[47]:


#practical
#access_key=d90ad37519a3bdb4be051e4c24457f54
access_key='http://api.exchangeratesapi.io/v1/latest?access_key=d90ad37519a3bdb4be051e4c24457f54&format=1'
response = requests.get(access_key)


# In[48]:


data=response.json()


# In[54]:


data['rates']['AED']


# In[52]:


user_entry = input("Which entry u want to convert ur currency to:").upper()
convert = int(input("How much u want to convert: "))
output = data['rates'][user_entry]*convert
print("{}".format(output))


# In[ ]:


#creating a file and reading it
new_file = open("new_story.txt",'w')
new_file.write('Hello,How you doing?')
new_file.close()


# In[ ]:


file = open("new_story.txt",'r')
for i in file:
    print(i)
file.close()


# In[ ]:


#create own module


# In[ ]:


#OOPS
#class


# In[55]:


class My_class:
    z = 55
    my_list = ['big one','small one']
    name= "Mr Potato leg"


# In[56]:


My_class.z


# In[57]:


My_class.my_list


# In[59]:


My_class.name


# In[60]:


#Methods in class
class Methods:
    z = 55
    
    def method():
        print("Method is working!!!")
    
    def sub(one,two):
        three = one - two
        print("{}-{} = {}".format(one,two,three))


# In[61]:


Methods.sub(22,1)


# In[62]:


# __init__
#synatx = def __int__(self,........)
class Animals:
    def __init__(self,size,noice,legs):
        self.size = size
        self.noice = noice
        self.legs = legs


# In[63]:


tiger = Animals(100,'Rwaaawr',4)
doplin = Animals(80,'reeee',0)


# In[64]:


tiger.size


# In[65]:


doplin.legs


# In[67]:


#Objects -using Attributes in a Method
class Animal:
    def __init__(self,name,color,noise):
        self.name = name
        self.color = color
        self.noise = noise
    
    def describe(self):
        print("The {} is {} and it makes the noise:{}".format(self.name,self.color,self.noise))


# In[68]:


owl = Animal('owl','brown','twit tawoo')
dog = Animal('dog','black','barkkk')


# In[69]:


owl.describe()


# In[71]:


#changing variables in a class objects

class Warrior:
    def __init__(self,name,strength,health):
        self.name = name
        self.strength = strength
        self.health = health
        
    def report(self):
        print("HI {},your strength is {},your health is {}".format(self.name,self.strength,self.health))
    
    def heal(self,plus_health):
        self.health += plus_health
    
    def damage(self):
        self.health -= 1
    
    def workout(self):
        self.strength += 1


# In[72]:


warrior1 = Warrior("Hero",10,100)


# In[75]:


warrior1.report()


# In[74]:


warrior1.damage()


# In[76]:


#Practical

class Bank:
    def __init__(self,name,acc_type,balance):
        self.name = name
        self.acc_type = acc_type
        self.balance = balance
        
    def report(self):
        print("Your Account name is : {},\nYour Account type is {},\nYour balance is {}".format(self.name,self.acc_type,self.balance))
    
    def withdraw_money(self,withdraw):
        self.balance -= withdraw
    
    def deposit_money(self,deposit):
        self.balance -= deposit
        
    def check_balance(self):
        print("Your balance is:{}".format(self.balance))


# In[77]:


Anish = Bank('Anish','Savings',100)
A2 = Bank('a2','Current',20)


# In[78]:


Anish.report()


# In[79]:


Anish.withdraw_money(30)


# In[80]:


A2.deposit_money(25)


# In[81]:


A2.report()


# In[82]:


A2.check_balance()


# In[20]:


#practical
Wizard = {'health':100,'strength':75,'defense':40,'magic':80,'gold':70}
Elf = {'health':100,'strength':40,'defense':40,'magic':100,'gold':70}
Gobin = {'health':100,'strength':50,'defense':50,'magic':50,'gold':100}



class Game:
    def __init__(self,health,strength,defense,magic,gold):
        
        self.health = health
        self.strength = strength
        self.defense = defense
        self.magic = magic
        self.gold = gold
        
    def report(self):
        print("Your character name is : '{}' \nHealth   : {}\nStrength : {}\nDefense  : {}\nMagic    : {}\nGold     : {}".format(self.name,self.health,self.strength,self.defense,self.magic,self.gold))
    
    def report_health(self):
        print("Your current health is :{}".format(self.health))    
    
    def add_health(self,get_health):
        self.health += get_health
    
    def remove_health(self,take_health):
        self.balance -= take_health
        
    def add_gold(self,get_gold):
        self.health += get_health
        
    def remove_gold(self,get_gold):
        self.health += get_health
        
    



# In[ ]:





# In[21]:


#def character():
print("Choose your character from :")
print("1.Wizard\n2.Elf\n3.Gobin\n")
user_input = int(input("Enter the number corresonding to your character: "))
if user_input == 1:
    player_charater = Game(Wizard['health'],Wizard['strength'],Wizard['defense'],Wizard['magic'],Wizard['gold'])
    print("You have choosen the character : Wizard")
    print("\n")
        #Wizard.report()
elif user_input == 2:
    player_charater = Game(Elf['health'],Elf['strength'],Elf['defense'],Elf['magic'],Elf['gold'])
    print("You have choosen the character : Elf")
    print("\n")
        #Elf.report()
elif user_input == 3:
    player_charater = Game(Gobin['health'],Gobin['strength'],Gobin['defense'],Gobin['magic'],Gobin['gold'])
    print("You have choosen the character : Gobin")
    print("\n") 
        #Gobin.report()
else:
    print("Invalid input")
    print("Choose again")
        
            #Add go to here


# In[ ]:





# In[33]:


'''
import random as r
def frd_emy():
    f_or_e = r.randint(1,2)
    if f_or_e == '1':
        opp = 'f'
    elif f_or_e=='2':
        opp = 'e'
   '''
 


# In[32]:


'''
i =frd_emy()
print(i)
'''


# wizard = {'health':100,'strength':75,'defense':40,'magic':80,'gold':70}
# elf = {'health':100,'strength':40,'defense':40,'magic':100,'gold':70}
# gobin = {'health':100,'strength':50,'defense':50,'magic':50,'gold':100}
# 
# 
# 
# class Character:
#     def __init__(self,name,health,strength,defense,magic,gold):
#         self.name = name
#         self.health = health
#         self.strength = strength
#         self.defense = defense
#         self.magic = magic
#         self.gold = gold

# In[1]:


#practical
import time
avaiable_points = 5

Wizard = {'health':100,'strength':75,'defense':40,'magic':80,'gold':70}
Elf = {'health':100,'strength':40,'defense':40,'magic':100,'gold':70}
Gobin = {'health':100,'strength':50,'defense':50,'magic':50,'gold':100}



class Game:
    def __init__(self,health,strength,defense,magic,gold):
        
        self.health = health
        self.strength = strength
        self.defense = defense
        self.magic = magic
        self.gold = gold
        
    def stats(self):
        print("Character health : {}\t Character Strength : {}\t Character Defense : {}".format(self.health,self.strength,self.defense))

    
    

class Enemy:
    def __init__(self,health,strength,defense):
        
        self.health = health
        self.strength = strength
        self.defense = defense
    
skeleton = Enemy(40,30,30)
cat = Enemy(70,45,65)


# In[2]:


def attack(attacker_str,defender_def):
    damage = attacker_str - defender_def
    return damage



#def character():
print("Choose your character from :")
print("1.Wizard\n2.Elf\n3.Gobin\n")
user_input = int(input("Enter the number corresonding to your character: "))
if user_input == 1:
    player_charater = Game(Wizard['health'],Wizard['strength'],Wizard['defense'],Wizard['magic'],Wizard['gold'])
    print("You have choosen the character : Wizard")
    print("\n")
    player_charater.stats()
    
        #Wizard.report()
elif user_input == 2:
    player_charater = Game(Elf['health'],Elf['strength'],Elf['defense'],Elf['magic'],Elf['gold'])
    print("You have choosen the character : Elf")
    print("\n")
        #Elf.report()
    player_charater.stats()
    
elif user_input == 3:
    player_charater = Game(Gobin['health'],Gobin['strength'],Gobin['defense'],Gobin['magic'],Gobin['gold'])
    print("You have choosen the character : Gobin")
    print("\n")
    player_charater.stats()
    
else:
    print("Invalid input")
    print("Choose again")

    

    

    
    
            


# In[4]:


avaiable_points = 5

while avaiable_points>0:
        print("Which stat You wanna increase of your character by 10 points?")
        player_charater.stats()
        increase = int(input("1.Heath\n2.Strength\n3.Defense\n"))
        if increase == 1:
            player_charater.health += 10
        elif increase == 2:
            player_charater.health += 10
        elif increase == 3:
            player_charater.health += 10
        else:
            break
        avaiable_points -=1


# In[8]:


play = True
        
user_name = input("Your name is : ")
while play == True:
        player_charater.stats()
        print("\n")
        print("{} ,You see 4 paths ahead ,path 1 leads you to a skeleton,path 2 leads to some rich dude,path 3 leads to a cat,path 4 is going back".format(user_name))
        path_choice = input('Which one do you want to walk (1,2,3,4): ')
        if path_choice =='1':
            fight_option = input("You see...A skeleton.Fight(y/n)")
            if fight_option == 'y':
                while 1==1:
                    #user goes first
      
                    damage = attack(player_charater.strength,skeleton.defense)
                    skeleton.health -= damage
                    print("Skeleton health is {}".format(skeleton.health))
                    if skeleton.health <=0:
                        print("Skeleton dies")
                        break
                    time.sleep(2)
                    print("Now skeleton attacks....")
                    time.sleep(1)
                    #skeleon goes second
                    damage = attack(skeleton.strength,player_charater.defense)
                    player_charater.health -= damage
                    print("Player  health is {}".format(player_charater.health))
                    
                    if player_charater.health <=0:
                        print("You die")
                        play = False
                        break
                    time.sleep(2)
                    print("Now you attack....")
                    time.sleep(1)


        elif path_choice == '2':
            money_info = input("You see.....A rich man...He will give you money if u help  him..yes or no(y/n)")
            if money_info == 'y':
                print("He says .....nice of you")
                player_charater.gold +=100
            else:
                print("He says ..how rude of you")
                player_charater.health -= 10
                
                
        elif path_choice == '3':
            fight_option = input("You see...A Cat.Fight(y/n)")
            if fight_option == 'y':
                while 1==1:
                    #user goes first
                    damage = attack(player_charater.strength,cat.defense)
                    cat.health -= damage
                    print("Cat health is {}".format(cat.health))
                    if cat.health <=0:
                        print("Cat dies")
                        break
                    time.sleep(2)
                    print("Now Cat attacks....")
                    time.sleep(1)
                    #cat goes second
                    damage = attack(cat.strength,player_charater.defense)
                    player_charater.health -= damage
                    print("Player  health is {}".format(player_charater.health))
                    if player_charater.health <=0:
                        print("You die")
                        play = False
                        break
                        time.sleep(2)
                    print("Now skeleton attacks....")
                    time.sleep(1)
        else:
            play = False


# In[9]:


# Functional Programming
# 3 types

#1st one is Lambda
#instead of : 
#def function(num):
#    num2 = num + 1
#we can use

lam_func = lambda x: x+3


# In[10]:


lam_func(10)


# In[11]:


my_lambda = lambda name:"Hello {}".format(name)


# In[12]:


my_lambda('Anish')


# In[25]:


#2nd one is Map
#map using normal functions

list_of_nums = [1,10,1000,2000]

def divider(x):
    y = x/5
    return y

list_of_large = list(map(divider,list_of_nums))

list_of_large


# In[19]:


#Map using Lambda on a list

old_nums = [1,2,3,4,5]
new_nums = list(map(lambda x : x+9,old_nums))
new_nums


# In[21]:


#Map using Lambda on a tuples

old_tuple = (2,4,6,8,10)
new_tuple = tuple(map(lambda num : num/2,old_tuple))
print(new_tuple)


# In[23]:


#3rd type
#map with lambda and multiple input

list_one = [1,2,3,4,5]
list_two = [100,200,300,400,500]

list_three = list(map(lambda x,y:x+y,list_one,list_two))

list_three


# In[27]:


#Filter

my_list = [1,14,53,72,2,99]
filtered_list = list(filter(lambda x:x%2==0,my_list))
filtered_list


# In[28]:


names_list = ['John','Phil','Joe','Jochie','Anish']

short_names = list(filter(lambda name : len(name)<=4,names_list))
print(short_names)


# In[ ]:




