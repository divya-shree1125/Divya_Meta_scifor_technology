#1.find sum of list element
a=[1,3,4,56,6,7]
print(sum(a))

#2.largest element in a list
b=[2,4,6,8,6,9]
print(max(b))
#(or)
number=b[0]
for i in range(len(b)):
    if b[i]>number:
        number=b[i]
print(number)

#3.remove duplicates in a list
c=[1,2,4,4,3,3,5,5]
print(list(set(c)))


#4.check if all elements in a list are unique
list=[1,1,1,1]
print(len(set(list))==1)

#5.program to reverse list
a=['a','b','b','e','f']
print(a[::-1])

#6.count no of odd n even numbers in a list
lst=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
for i in lst:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)


#7.check if a list is subset of another list
e=[1,2,3]
f=[1,2,3,4,5]
subset=all(item in f for item in e)
print(subset)

#8.max diff btw two consecutive element in a list
list = [10,7,6,9,2,0]
diff = 0
for i in range(len(list)-1):
  d= abs(list[i] - list[i+1])
  if d > diff:
    diff = d

print(diff)


#9.merge multiple dictionaries
d={1:2,2:3}
d1={4:5,5:6}
d.update(d1)
print(d)


#10.find words frequency in  sentence
str = "learning python for data science "
words = str.split()
frequency = {}

for i in words:
  if i in frequency:
    frequency[i] += 1
  else:
    frequency[i] = 1

print(frequency)
