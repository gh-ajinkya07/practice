
'''

print("Hello World")

x =float(2)
print(x)
y = int(3.4)
print(y)
z = int("123")
print(z)
s = str(2)
print(s)
print(type(s))

str = "banana"
print(str[2])
print(len(str))

for i in str:
    print(i)

txt = "The best things in life are free!"
print("free" in txt)

print("expensive" not in txt)

txt = "Hello World"

print(txt[3:])

print(txt[-8:])


a = "     Hello World"
print(a.upper())

print(a.lower())

print(a.strip())


a = "Hello , There , Cortana"
print(a.split())

a = "Hello"
b = "World"
c = a+" "+b
print(c)


quantity = 3
itemno = 467
price = 49.89
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity,itemno,price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)

l1 = [1,2,3,4]
l1.append(5)
print(l1)
print("___________")
l2 = l1.copy()
l2.clear
print()
print(l2)

a = [1,2,3,4,2,3,4,1,3]
x = a.count(3)
print(x)

a = [1,2,3,4,5]
b = [6,7,8,9,10]
a.extend(b)
c = ["a","b","c","d"]
a.extend(c)
print(a)
a = [2,3,1,7,8,5]
a.insert(2,"Orange")
print(a)
a.pop(2)
print(a)
a.sort()
print(a)

def multiply(n):
    if n == 1:
        return 1
    return n*multiply(n-1)

result = multiply(5)

print(result)

# OS module in python

import os

print(os.name)

print(os.getcwd())

print(os.listdir('.'))


## Random Module
import random


print(random.getstate())

print(random.randrange(3,9))
print(random.randint(3,9))

mylist = ["apple","banana","cherry","mango"]
print(random.choice(mylist))

l1 = [1,2,3,4,5]
print(random.choice(l1))

l1 = [1,2,3,4,5,6,7,8]
print(random.choices(l1))

l1 = [1,2,3,4,5,6,7,8]
random.shuffle(l1)
print(l1)

l1 = [1,2,3,4,5,6,7,8]

print(random.sample(l1,k=4))

print(random.uniform(1,10))

## Numpy ##
import numpy as np

# 0-D arrays
a1 = np.array(42)
print(a1)

# 1-D arrays
a2 = np.array([1,2,3,4,5])
print(a2)

# 2-D arrays
a3 = np.array([[1,2,3],[4,5,6]])
print(a3)

# 3-D arrays
a4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,3,6]]])
print(a4)

# checking dimensions of arrays

print("##################")
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)
print(a4.ndim)


arr = np.array([1,2,3,4,5],ndmin = 5)
print(arr)

print("Dimension of array is:",arr.ndim)


# Accessing array elements

arr = np.array([1,2,3,4,5])
print(arr[2])
print(arr[1]+arr[4])

a1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("2 element on first dimension: ",a1[0,1])
print(a1[1,4])

print("Negative Indexing: ")
print(a1[1,-1])

# Array Slicing 

arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[-5:-1])
print(arr[4:])
print(arr[:4])
print(arr[1:6:2])
print(arr[::2])
print("##############")

a1 = np.array([[1,2,3,4,5],[6,7,8,9,10]]) 
print(a1[:,1:3])


# Data types in Numpy

arr = np.array([1,2,3,4,5])
print(arr.dtype)

a1 = np.array(["apple","banana","cherry"])
print(a1.dtype)

a2 = np.array([1,2,3,4],dtype="S")
print(a2)
print(a2.dtype)
print("############")

ar = np.array([1.2,3.4,2.3])

newarr = ar.astype(int)
print(newarr)
print(newarr.dtype)

a3 = np.array([1,0,3,0,5])

newa3 = a3.astype(bool)
print(newa3)
print(newa3.dtype)

# Numpy array copy vs view

#The main difference between a copy and a view of an array is that 
# the copy is a new array, and the view is just a view of the original array.

#The copy owns the data and any changes made to the copy will not affect original array,
#and any changes made to the original array will not affect the copy.

# The view does not own the data and any changes made to the view will affect the original
# array, and any changes made to the original array will affect the view.

import numpy as np

arr = np.array([1,2,3,4,5])
x = arr.copy()

arr[0] = 20

print("Original Array",arr)
print("Duplicate Array",x)

a1 = np.array([1,2,3,4,5])
x1 = a1.view()

a1[0] = 20
x1[2] = 30

print("Origiinal Array",a1)
print("Duplicate Array",x1)


# Check if array own its data

import numpy as np

arr = np.array([1,2,3,4,5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr.shape)

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)

print(newarr)
print("##################")
new = arr.reshape(2,3,2)
print(new)
print("###########")
print(arr.reshape(3,4).base)

# Flattening the Arrays

import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])

newarr = arr.reshape(-1)
print(newarr)


# Numpy Array Iterating 

import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])

for x in arr:
    for y in x:
        print(y)
print("##############")
newarr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in newarr:
    for y in x:
        for z in y:
            print(z)

# Iterating Arrays using nditer()

import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)
print("###############")
newarr = np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(newarr[ : , : :2]):
    print(x)

'''
# Enumerated Iteraton Using ndenumerate()
''' Enumeration means mentioning sequence number of something one by one.'''
'''
import numpy as np

arr = np.array([1,2,3,4,5])

for idx, x in np.ndenumerate(arr):
    print(idx,x)

newarr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

for idx, x in np.ndenumerate(newarr):
    print(idx,x)


# Joining Numpy Arrays 

import numpy as np 

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

arr = np.concatenate((arr1,arr2))
print(arr)

arr3 = np.array([[1,2],[3,4]])
arr4 = np.array([[5,6],[7,8]])

newarr = np.concatenate((arr3,arr4))
print(newarr)

'''
# Joining Array Using Stack Functions 

''' Stacking is same as concatenation, the only difference is that stacking 
is done along a new axis'''
'''
import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

newarr = np.stack((arr1,arr2), axis = 1)
print(newarr)


# Splitting Numpy arrays 

import numpy as np

arr = np.array([1,2,3,4,5,6])

newarr = np.array_split( arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

arr1 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr1 = np.array_split(arr1, 3)

print(newarr1)

# Time converter to 24 hour military formate

import os
import sys

def timeConversion(time):
    night =0
    if "PM" in time:
        night = 12
    time = time[:8].split(':')
    if time[0] == '12':
        time[0] = 0
    time[0] = str(int(time[0])+ night)
    newtime = str()
    for x in time:
        newtime += x + ':'    
    if len(newtime) < 9:
        newtime = '0' + newtime
    
    return newtime[:8]

time = input("Enter time:")
result = timeConversion(time)
print(result)    
print("Hello World")
for i in range(0,5):
    print(i)

x = eval("My {0} is {1} {2}.".format("name","Ajinkya","Patil"))
print(x)

print(ord("i"))

# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	# Function to print a BFS of graph
	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as 
		# visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:

			# Dequeue a vertex from 
			# queue and print it
			s = queue.pop(0)
			print (s, end = " ")

			# Get all adjacent vertices of the
			# dequeued vertex s. If a adjacent
			# has not been visited, then mark it
			# visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Breadth First Traversal"
				" (starting from vertex 2)")
g.BFS(2)

import requests
import bs4
base_url = "https://books.toscrape.com/catalogue/page-{0}.html"
two_star_title = []
for i in range(1,5):

    scrape_url = base_url.format(i)
    req = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(req.text,"lxml")

    books = soup.select(".products_pod")

    for book in books:
        if len(book.select(".star-rating.Two")) != 0:
            book_title = book.select('a')[1]['title']
            two_star_title.append(book_title)
		
			
print(len(two_star_title))

class Node:
    def __init__(self,data,level,fval):

        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
        x,y = self.find(self.data,'_')
        """ val_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
                children = []
                for i in val_list:
                    child = self.shuffle(self.data,x,y,i[0],i[1])
                    if child is not None:
                        child_node = Node(child,self.level+1,0)
                children.append(child_node)
                return children

    def shuffle(self,puz,x1,y1,x2,y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 <len(self.data) and y2 >= 0 and y2 <len(self.data):
temp_puz = []
temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
temp_puz[x2][y2] = temp_puz[x1][y1]
temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None


    def copy(self,root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
t.append(j)
temp.append(t)
        return temp    

    def find(self,puz,x):
        """ Specifically used to find the position of the blank space """
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j


class Puzzle:
    def __init__(self,size):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
self.n = size
self.open = []
self.closed = []

    def accept(self):
        """ Accepts the puzzle from the user """
puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
puz.append(temp)
        return puz

    def f(self,start,goal):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        return self.h(start.data,goal)+start.level

    def h(self,start,goal):
        """ Calculates the different between the given puzzles """
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp


    def process(self):
        """ Accept Start and Goal Puzzle state"""
        print("Enter the start state matrix \n")
        start = self.accept()
        print("Enter the goal state matrix \n")        
        goal = self.accept()

        start = Node(start,0,0)
start.fval = self.f(start,goal)
        """ Put the start node in the open list"""
self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            print("")
            print("  | ")
            print("  | ")
            print(" \\\'/ \n")
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                print("")
            """ If the difference between current and goal node is 0 we have reached the goal node"""
            if(self.h(cur.data,goal) == 0):
                break
            for i in cur.generate_child():
i.fval = self.f(i,goal)
self.open.append(i)
self.closed.append(cur)
            del self.open[0]

            """ sort the opne list based on f value """
self.open.sort(key = lambda x:x.fval,reverse=False)


puz = Puzzle(3)
puz.process()


email = input("Enter your email address: ").strip()

new = email.split("@")

domain = new[1]

name = new[0]

result = "Your name is {}\n Your Domain is {}".format(name,domain)

print(result)
'''


# class Mobile:

#     def __init__(self,brand,price):

#         print("inside constructor")
#         self.brand = brand
#         self.price = price


# Mob1 = Mobile("Apple",20000)
# print("Mobile 1 has brand",Mob1.brand,"and price",Mob1.price)

# Mob2 = Mobile("China",1200)
# print("Mobile 2 has brand",Mob2.brand,"and price",Mob2.price)

# class Mobile:
#     def __init__(self, price, brand):
#         print("Id of self in constructor", id(self))
#         self.price = price
#         self.brand = brand

# mob1=Mobile(1000, "Apple")
# print("Id of mob1 in driver code", id(mob1))

# mob2=Mobile(1000, "Apple")
# print("Id of mob2 in driver code", id(mob2))

# class Customer:
#     def __init__(self, cust_id, name, age,wallet_balance):
#         self.cust_id = cust_id
#         self.name = name
#         self.age = age
#         self.__wallet_balance = wallet_balance

#     def update_balance(self, amount):
#         if amount < 1000 and amount> 0:
#             self.__wallet_balance += amount

#     def show_balance(self):
#         print ("The balance is ",self.__wallet_balance)

# c1=Customer(100, "Gopal", 24, 1000)
# c1._Customer__wallet_balance = 100000000000
# c1.show_balance()


# class Customer:
#     def __init__(self,id,name,age,wallet_balance):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.__wallet_balance = wallet_balance

#     def set_wallet_balance(self,amount):
#         if amount<1000 and amount>0:
#             self.__wallet_balance = amount

#     def get_wallet_balance(self):
#         return self.__wallet_balance

# c1 = Customer(200,"Gopal",24,1000)
# c1.set_wallet_balance(120)
# print(c1.get_wallet_balance())

# class Mobile:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price

# mob1 = Mobile("Apple",2000)
# mob2 = Mobile("Xiomee",1000)
# mob3 = Mobile("Vivo",1500)
# mob4 = Mobile("Samsung",1800)
# mob5 = Mobile("OnePlus",1900)

# list_of_mobiles = [mob1,mob2,mob3,mob4,mob5]

# for mobile in list_of_mobiles:
#     print(mobile.brand,mobile.price)
        
# class Customer:
#     def __init__(self, name, age, phone_no, address):
#         self.name = name
#         self.age = age
#         self.phone_no = phone_no
#         self.address = address

#     def view_details(self):
#         print (self.name, self.age, self.phone_no)
#         print (self.address.door_no, self.address.street, self.address.pincode)

#     def update_details(self,add):
#         self.address = add

# class Address:
#     def __init__(self, door_no, street, pincode):
#         self.door_no = door_no
#         self.street = street
#         self.pincode = pincode

#     def update_address(self):
#         pass

# add1=Address(123, "5th Lane", 56001)
# add2=Address(567, "6th Lane", 82006)
# cus1=Customer("Jack", 24, 1234, add1)

# cus1.view_details()

# cus1.update_details(add2)

# cus1.view_details()


# Linked List:

# class Node:

#     def __init__(self,data):
#         self.__data = data
#         self.__next = None
    
#     def get_data(self):
#         return self.__data
#     def set_data(self,new_data):
#         self.__data = new_data
    
#     def get_next(self):
#         return self.__next
#     def set_next(self,next_node):
#         self.__next = next_node

# item_node = Node("Sugar")
# print(item_node.get_data())
# print(item_node.get_next())
# class LinkedList:

#     def __init__(self,head,tail):
#         self.__head = None 
#         self.__tail = None

#     def get_head(self):
#         return self.__head
#     def set_head(self,node):
#         self.__head = node

#     def get_tail(self):
#         return self.__tail
#     def set_tail(self,node):
#         self.__tail = node
    
#     def add(self,data):
#         new_node = Node(data)
#         if self.__head is None:
#             self.__head = self.__tail = new_node
#         else:
#             self.__tail.set_next(new_node)
#             self.__tail = new_node
    
#     def display(self):

#         temp = self.__head
#         while(temp is not None):
#             print(temp.get_data())
#             temp = temp.get_next()

# mytuple = ("John","ramesh","suresh","kalia")
# x = "".join(mytuple)
# print(x)


# def merge_list(list1, list2):
#     merged_data=""
#     #write your logic here
#     new_list2 = list2[::-1]
#     ziped = list(zip(list1,new_list2))
#     for i in ziped:
#         for j in i:
#             if j == None:
#                 pass
#             else:
#                 merged_data = merged_data + j 
#         merged_data = merged_data + " "
#     return merged_data

# #Provide different values for the variables and test your program
# list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
# list2=['y','tor','e','eps','ay',None,'le','n']
# merged_data=merge_list(list1,list2)
# print(merged_data)

# def check_double(list1,list2):
#     new_list=[]
#     #write your logic here
#     list1_double = [2*i for i in list1]
#     for i in list1_double:
#         if i in list2:
#             new_list.append(i)
#     new_list = [int(i/2) for i in new_list]
#     return new_list

# #Provide different values for the variables and test your program
# list1=[11,8,23,7,25,15]
# list2=[6,33,50,31,46,78,16,34]
# print(check_double(list1, list2))

# class Node:
#     def __init__(self,data):
#         self.__data=data
#         self.__next=None

#     def get_data(self):
#         return self.__data
    
#     def set_data(self,data):
#         self.__data=data
    
#     def get_next(self):
#         return self.__next
    
#     def set_next(self,next_node):
#         self.__next=next_node
    
# class LinkedList:
#     def __init__(self):
#         self.__head=None
#         self.__tail=None
    
#     def get_head(self):
#         return self.__head
    
#     def get_tail(self):
#         return self.__tail
    
#     def add(self,data):
        
#         new_node = Node(data)
#         if self.__head == None:
#             self.__head = self.__tail = new_node
#         else:
#             self.__tail.set_next(new_node)
#             self.__tail = new_node
#         #Remove pass and copy the code you had written to add an element.
    
#     def display(self):
        
#         temp = self.__head
#         while(temp is not None):
#             print(temp.get_data())
#             temp = temp.get_next()
            
#         #Remove pass and copy the code you had written to display the element(s).
    
#     def find_node(self,data):
#         temp = self.__head
#         while(temp is not None):
#             if temp.get_data() == data:
#                 return temp
#                 break
#             temp = temp.get_next()
            
#         #Remove pass and write the logic to find the node and return the node if found or return None.
                                            
#     #You can use the below __str__() to print the elements of the DS object while debugging
#     def insert(self,data,data_before):
#         new_node = Node(data)
#         if data_before == None:
#             self.__head = new_node
#             if self.__head.get_next() == None:
#                 self.__head.set_next(self.__tail)
#         else:
            
#             temp = self.__head
#             while(temp is not None):
#                 if temp.get_data() == data_before:
#                     node_before = temp
#                     new_node.set_next(node_before.get_next())
#                     node_before.set_next(new_node)
#                     if new_node.get_next() == None:
#                          new_node.set_next(self.__tail)
                
#                 temp = temp.get_next()
    #   def delete(self,data):
        
    #     node = self.find_node(data)
    #     if (node is not None):
    #         if (node == self.__head):
    #             if self.__head == self.__tail:
    #                 self.__tail = None
    #             self.__head = node.get_next()
    #         else:
    #             temp = self.__head
    #             while(temp is not None):
    #                 if(temp.get_next() == node):
    #                     temp.set_next(node.get_next())
    #                     if (node == self.__tail):
                            
    #                         self.__tail = temp
    #                     node.set_next(None)
    #                     break
    #                 temp = temp.get_next()
    #     else:
    #         print("Please enter valid elements")
#     def __str__(self):
#         temp=self.__head
#         msg=[]
#         while(temp is not None):
#            msg.append(str(temp.get_data()))
#            temp=temp.get_next()
#         msg=" ".join(msg)
#         msg="Linkedlist data(Head to Tail): "+ msg
#         return msg


# list1=LinkedList()
# #Add all the required element(s)
# #Search for the required node
# list1.add("Milk")
# list1.add("Salt")
# list1.add("Biscuit")
# list1.add("Apple Juice")
# list1.add("Pomegranate")
# list1.add("Watermelon")
# list1.add("Sugar")
# node=list1.find_node("Pomegranae")
# if(node!=None):
#     print("Node found")
# else:
#     print("Node not found") 


# def get_passenger_name(self):
#     return self.__passenger_name


# class Flower:
#     flower_list = ['Orchid','Rose','Jasmine']
#     def __init__(self):
#         self.__flower_name = None
#         self.__price_per_kg = None 
#         self.__stock_available = None
    
#     def get_flower_name(self):
#         return self.__flower_name
#     def set_flower_name(self,name):
#         self.__flower_name = name

#     def get_price_per_kg(self):
#         return self.__price_per_kg 
#     def set_price_per_kg(self,price):
#         self.__price_per_kg = price

#     def validate_flower(self):
#         if self.__flower_name in flower_list:



# def sms_encoding(data):
#     #start writing your code here
#     vowels = 'AEIOUaeiou'
#     data = data.split()
#     # return data
#     new = ''
#     for i in data:
#         if i in vowels:
#             new = new + i
#         for j in i:
#             if j in vowels:
#                 pass
#             else:
#                 new = new + j
#         new = new + ' '
#     return new

# data="I will not repeat mistakes"
# print(sms_encoding(data))

## Dictionaries in python

# thisdict = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year" : 1978,
# }
# print(thisdict["brand"])
# print(type(thisdict))
# print(len(thisdict))
# print(thisdict["colors"])

# Key method will return all the keys in the dictionary

# x = thisdict.keys()
# print(x)
# thisdict["color"] = "red"
# print(x)

# Values method will return all the values in the Dictionary

# y = thisdict.values()
# print(y)
# thisdict["color"] = "white"
# print(y)

# Items emthod will return each item in a dictionary as a tuple in list 

# x = thisdict.items()
# print(x)

# if "model" in thisdict:

# fruits = ('grapes','apples','mangos')

# for i in fruits:
#     print(i)

# animals = tuple(('lion','tiger','bear'))
# print(animals)

# print(len(animals))

# fruits = {'grapes','apples','berries','mangos'}

# for fruit in fruits:
#     print(fruit)

# animals = set(('lion','tiger','bear'))
# print(animals)

# print(len(animals))


# root = Tk()
# root.title('Counting Sec')
# button = tkinter.Button(root,text = 'STOP',width = 25,command = root.destroy)
# button.pack()
# root.mainloop()

# root = Tk()
# w = Canvas(root,width = 40,height = 60)
# w.pack()
# canvas_height = 20
# canvas_width = 200

# y = int(canvas_height/2)
# w.create_line(0,y,canvas_width,y)
# root.mainloop()


# from tkinter import *
# from tkinter import Tk

# root = Tk()
# var = IntVar()
# Checkbutton(root, text = 'male', variable = var).grid(row = 0,sticky = W)
# var1 = IntVar()
# Checkbutton(root,text = 'female', variable = var1).grid(row = 1, sticky = W)
# var3 = IntVar()
# Checkbutton(root, text = "other",variable = var3).grid(row = 2, sticky = W)
# root.mainloop()

# root = Tk()
# Label(root,text = 'First Name: ').grid(row = 0)
# Label(root,text = 'Last Name: ').grid(row = 1)
# e1 = Entry(root).grid(row = 0, column = 1)
# e2 = Entry(root).grid(row = 1, column = 1)
# root.mainloop()

# from tkinter import *
# master = Tk()

# w = Label(master, text = 'Welcome to the World of Python!', bg = 'yellow')
# w.pack()
# master.mainloop()

# from tkinter import *

# master = Tk()

# Lb = Listbox(bg = 'yellow')
# Lb.insert(1, 'Python ')
# Lb.insert(2, 'Java')
# Lb.insert(3, 'C++')
# Lb.insert(4, 'Any Other')
# Lb.pack()
# master.mainloop()

# import datetime

# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime('%A'))

# import datetime

# x = datetime.datetime(2020,12,4)
# print(x)

# 

# '''Python GUI package'''
# '''Frames: Are containers in which we can group multiple items
#             It is nott visible to user.'''
# from tkinter import *
# root = Tk()

# canvas = Canvas(width = 400, height = 200, bg = 'red')
# canvas.pack(expand = YES, fill = BOTH)

# photo = PhotoImage(file = "photo.png")
# canvas.create_image(0,0, image = photo, anchor = NW)

# mainloop()

# from tkinter import *
# import tkinter
# from tkinter.font import BOLD
# from pytube import YouTube

# def download():
#     #url1 = url.get()
#     #print(url1)
#     #url.set("")
#     #l2.insert(END,url1)
    
#     url1 = url.get()
#     #url1 = 'https://www.youtube.com/watch?v=1KppB7Xe0BU'
#     my_video = YouTube(url1)
#     l2.insert(END,"***Video Title****\n")
#     #print("********Video Title*********")
    
#     #get Video Title
#     #print(my_video.title)
#     l2.insert(END,my_video.title)

    
#     #get Thumbnail Image
#     l2.insert(END,"**Tumbnail Image**\n")
#     l2.insert(END,my_video.thumbnail_url)


#     #get all the stream resolution for the 
#     l2.insert(END,"**Download video**\n")
#     for stream in my_video.streams:
#         l2.insert(END,stream)

#     #set stream resolution
#     #my_video = my_video.streams.get_highest_resolution()

#     #or
#     my_video = my_video.streams.first()

#     #Download video
#     my_video.download()
    




# root=Tk()
# root.title("My First YOUTUBE VIDEO DOWNLOADER")
# root.geometry("700x700")
# root.resizable(0,0)
# f1 = Frame(root,bg="cyan")
# f1.pack()
# url=tkinter.StringVar()
# l1 = tkinter.Label(f1,text="YouTube Video Downloader",font="Arial 30 bold",bg="black", fg = "cyan")
# l1.grid(column=0,row=1,padx=40,pady=50)

# f2 = Frame(root,width=500,height=200, bg = "#5cdb95")
# f2.pack()
# l2 = Label(f2,text="Enter the URL Here...",font="Arial 20 bold", bg = "black", fg = "cyan")
# l2.grid(column=0,row=1,padx=40,pady=40)
# t1 = Entry(f2,textvariable = url, font=('calibre',10,'normal'),width=50, borderwidth = 1)
# #t1.grid(column=,row=2)
# t1.grid(column=0,row=2)

# f3 = Frame(root,width=500,height=600, bg = "cyan")
# f3.pack()
# b1 = tkinter.Button(f3,text="Download", fg="white", bg = "black",command=download)
# b1.grid(column=5,row=5, padx=100,pady=10)

# l2 = Text(f3,bg="black",fg="white")
# l2.grid(column=5,row=12,pady=10)


# root.mainloop()










# # Various Operators in Python

# # Arithmatic Operators:

# a = 50 
# b = 10
# print("Additon: ", a+b)
# print("Substraction: ", a-b)
# print("Multiplication: ", a*b)
# print("Division: ", a/b)
# print("Modulo: ", a%b)


# # Logical Operators:

# c = True
# d = False

# print("\nAND operator: ", c and d)
# print("OR operator: ", c or d)
# print("NOT operator: ", not d)


# # Comparison Operator

# e = 20
# f = 10

# print("\nGreater than operator", e > f)
# print("Less than operator", e < f)
# print("Greater than equal to operator", e >= f)
# print("Less than equal to operator", e >= f)
# print("Not equal to", e != f)
# print("Equal to", e == f)

# # Assignment Operator
# print()
# a = 10
# print(a)
# a += 10
# print(a)
# a *= 10
# print(a)
# a -= 20
# print(a)


# def min_Star(arr, n):
#     min_star = 0

#     for i in range(n):
#         if arr[i] != i+1:
#             print(abs(arr[i] - (i+1)))
#             min_star = min_star + abs(arr[i] - (i+1))
    
#     return min_star

# arr = [1,1,3,4]
# result = min_Star(arr, 4)
# print(result)
# sum = arr[0]w
# main = [sum]
# for k in range(1,k+1):
#     sum += arr[k]
#     main.append(sum)
# Python program to rearrange
# a linked list in given manner

# Link list node
# class Node:
	
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None

# # Function to reverse the linked list
# def arrange( head):

# 	temp = head
	
# 	# defining a deque
# 	d = []
	
# 	# push all the elements of linked list in to deque
# 	while (temp != None) :
# 		d.append(temp.data)
# 		temp = temp.next
	
# 	# Alternatively push the first and last elements
# 	# from deque to back to the linked list and pop
# 	i = 0
# 	temp = head
# 	while (len(d) > 0) :
# 		if (i % 2 == 0) :
# 			temp.data = d[0]
# 			d.pop(0)
		
# 		else :
# 			temp.data = d[-1]
# 			d.pop()
		
# 		i = i + 1

# 		# increase temp
# 		temp = temp.next
		
# 	return head
	
# # UTILITY FUNCTIONS
# # Push a node to linked list. Note that this function
# # changes the head
# def push( head_ref, new_data):

# 	# allocate node
# 	new_node = Node(0)

# 	# put in the data
# 	new_node.data = new_data

# 	# link the old list off the new node
# 	new_node.next = (head_ref)

# 	# move the head to point to the new node
# 	(head_ref) = new_node
# 	return head_ref

# # printing the linked list
# def printList( head):

# 	temp = head
# 	while (temp != None) :
# 		print( temp.data,end=" ")
# 		temp = temp.next

# # Driver program to test above function

# # Let us create linked list 1.2.3.4
# head = None

# head = push(head, 5)
# head = push(head, 4)
# head = push(head, 3)
# head = push(head, 2)
# head = push(head, 1)
# print("Given linked list\t")
# printList(head)
# head = arrange(head)
# print( "\nAfter rearrangement\t")
# printList(head)

# # This code is contributed by Arnab Kundu





