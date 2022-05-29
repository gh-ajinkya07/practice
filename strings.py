
'''
fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index,letter)
    index += 1

fruit = "banana"
count = 0
for letter in fruit:
    if letter == 'a':
        count += 1

print(count) 

fruit = "banana"

"n" in fruit
"m" in fruit

if "a" in fruit:
    print("Found it!")

greet = "Hello Bob"
zap = greet.lower()
print(zap)
print(greet)
print("Hello There".lower())

stuff = "Hello World"

print(type(stuff))
print()

print(dir(stuff))

fruit = "banana"
pos = fruit.find("na")
print(pos)

aa = fruit.find("z")
print(aa)

greet = "Hello Bob"
string = greet.replace("Bob","Ajinkya")
print(string)
string1 = greet.replace("o","x")
print(string1)

string = "     Hello World   "
print(string.lstrip())
print()
print(string.rstrip())
print()
print(string.strip())


line = "Please have a nice day"
print(line.startswith("Please"))
print(line.startswith("p"))


data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
findex = data.find("@")

lindex = data.find(" ",findex)

host = data[findex+1:lindex]

print(host)

###  Files

fhand = open("demo.txt")
count = 0
for line in fhand:
    count +=1

print("Line Count:",count)

fhand = open("demo.txt")
inp = fhand.read()
print(inp)

fhand = open("demo.txt")
for line in fhand:
    if line.startswith("I"):
        print(line)
'''
