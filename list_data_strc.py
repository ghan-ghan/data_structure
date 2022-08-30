



'''List is the data structure that stores multiples data of same types or different tyoes.
It is ordered i.e it position are ordered;therefore indexing is done on list ,. List is changables.
.List is seperated from others by [].list is created either by  
constructor method or by  simply [].
List  accepts the duplication of the data : if same data eg. [1,2,3,1] is present the list 
accepts or identity 1 and 1 as different elements'''


# list =[]
# print(list)

'''by constructor creating list'''
list1= list()
print(list1)




'''Checking whether the list is empty or not :'''


if len(list1) ==0:
    print("empty list")
if not list1:
    print("Empty list")
else:
    print("Not empty list")


'''Inserting the elements in the empty list ; append method , extend method, insert method.'''
#1..BY append() methood ''
'''Append() add the elements at the end of the list'''


'''
Syntax = list.append(element) ; element : any data types (string ,numer,object....)
'''
list1=[]
list1.append(1)
print(list1)
list1.append(2)
print(list1)
list1.append(3)
print(list1)
list1.append("Hair")
print(list1)
list1.append("Sita")
print(list1)
list1.append(True)
print(list1)


#2 ..BY insert() method
'''Insert add the elements at the specified position:'''

'''
Syntax = list.insert(position, elements)
position : specify where to insert the value
elements: specify types of data you want to insert (any data types)'''


list2= [1,2,34,"hari", "shayama"]
list2.insert(1,"Himal")
list2.insert(5,"hello")
print(list2)

# #BY Extend () method:

# '''Extend method add the list of the elements or any iterables(such as tuples, list ,string..) to the end of the current list>'''


'''syntax = list.extend(iterables) '''

list1 = [ 1,2,3,4,5]
list2=["himal", "cat","dog"]
list1.extend(list2)
print(list1)

# tuples=("name","time","sets")
# list1.extend(tuples)
# print(list1)


'''knowing the length of list is done by using len();'''

name =[1,2,34,"sagarmatha","cat", "dog"]
length = len(name)
print(length)


'''Accessing the elements of list ;indexing 
python has the first index 0 and follows the incremental index by 1 '''

name1 =[1,2,34,"sagarmatha","cat", "dog"]
print(name[0])
print(name1[2])


'''python also follow in the reverser of index ; -1 will be the first index following the decremental of index  by -1'''

print(name1[-1])
print(name1[-2])


'''slicing the list
syntax == listname[start:end:index_jump'''

print(name1[0:5])
print(name1[1:])
print(name1[-4:-1])
print(name1[1:6:2])
print(name1[::-1]) #It reverse the elements in the list 


'''Deletion or remove or the pop of the elements of list'''

'''Pop():removes the elementssss at the specified position 
Default condition it removes the last elements
Syntax ---> list.pop(position)
''' 
name1=["cat ", "dog", "deer", "elephant"]
name1.pop()
print(name1) # returns out the last element (elephant ) and displays the remaining element 

name1.pop(0)
print(name1)



#2.. remove () : removes the item with the specified value :syntax --> list.remove(element)

animals=["cat ", "dog", "deer", "elephant"]         
animals.remove("dog") 
print(animals)

#3..clear ():reamoves all the elements from the list and make empty list
#syntax --> list.clear()
pets=['cat','dog','elephant','deer']
pets.clear()
print(pets)



#4..del () operator : it removes the elements at specified idex position but the removed items is not returned as pop() method:

myList = ["Bran",11,22,33,"Stark",22,33,11]
del myList[2]
print(myList)


'''count(): it returns the numbers of time the elements appears in the list'''
#syntax --->list.count(value)

marks =[100,99 , 98 , 98 ,90 ,56,84,97,80]
mark=marks.count(98)
print(mark)

mark= marks.count(56)
print(mark)


#index():returns the index of the specified value/elements
'''Syntax --> list.index(element)'''
animals=["cat", "dog", "deer", "elephant"]    
print(animals.index("dog"))
print(animals.index("elephant"))
print(animals.index("cat"))




#copy():returns the copy of the list ; two types of copy is usually seen ; deep copy and shallow copy 
'''shallow copy : it stores the reference value and any change on the list of first cause impact on other list:'''



list3 =[1,2,3,4,5]
list6 =list3 # copy the value of list3 by list6
print(list3)
print(list6)  
list6.append(9) # 9 is added to the list6;it changes the list3 values too
print(list6)
print(list3)



'''Deep copy ; it  returns the copy of the specified list
deep copy :the original and copied items are not of same type , change on one items donot affect other '''

#Syntax --> list.copy()
subj=['maths','datascience','machine learning','artificila intelligence','economics','pshychology']
subject=subj.copy()
print(subject)
subj.remove('economics')  #removes the economics from the subj
subj.remove('maths')      #remove the maths from the subj
print(subj)               #display the elements after the removale of maths and economics from the subj
print(subject)            #Although the changes on the subj seems to change to the subjects , it doesnot change on the subjects

# Deep copy is purely independent of the original object


#sort ():sorts the list in ascending or decending order

#Syntax ---> list.sort()

'''sorting in ascending order'''

subj=['maths','datascience','machine learning','artificila intelligence','economics','pshychology']
subj.sort()
print(subj)

'''sorting in the descending order'''

subj.sort(reverse = True)
print(subj)


#Loops in list:
'''for loops and while loops:'''
list = ['apple','mango','orange','carrot']
for i in list:        # i is variable it can be any ; variable (a,b,c...) or any items .
    print(i) 

''' #similarly in other list if we want to print every elements in  other list we can use other items but 
whatever items we use in loop we must print the same item'''
#such as 
for x in list:
    print(x)



for items in list:
    print(items)


#for loops using range
for items in range(len(list)):
    print(items)               # it displays the index of the elements


'''LIST COMPREHENSION'''
'''It is the shortest or concise way of creating list.'''
#for instances; suppose we want to create square of 1 to 10 

'''Normally we work as '''
list=[]
for i in range(1,11):
    list.append(i*2)

print(list)

'''but using the list comprehension method we can print as '''

list = [ i*2 for i in range(1,11)]
print(list)

#so the syntax for list comprehesion ----> list=[expression for items in iterables(list,string,tuples ....)]
'''list comprehesion containing condition statements'''

#list =[expression for items in iterables if condition]

num= [-4, -2, 0, 2, 4]
list=[i for i in num if i >=0]   #IT prints the numbers in num that are greater or equal to 0)
print(list)


'''Data structure : 1..Stack; it works on last in first out method . The operation that works on the stack are
1.push() --> add elements ;but using list method we use append() to add elements
2.pop()  ---> remove the elements similar as in list 
3.peek or top -->
4. isEmpty --> ''' 

stack=[]
if len(stack) ==0 :
    print("Empty list ")

stack.append(10)     # firstly 10 is added in the stack 
stack.append(20)     # 20 is stored above the 10
stack.append(40)     # 40 is stored above the 20 and 10
stack.append(50)     # 50 is stored above the  40 and 20 and 10
stack.append(60)     # 60 is stored above the m50 and 40 20 and 10
print(stack)         # The top elements is 60 50 40 20   ; In stack the top elements which are placed lately must be removed fist


stack.pop()  
print(stack)         # Firstly 60 is removed from the stack and then 50 , 40 ,20 ,10
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)


'''2.Queue: using the list method we can  also operate the Queue datastructure
It works on first in first out (FIFO);QUEUE  has enque and dequeue method that can be operated in 
list by append method and pop method:
'''


queue =[]
queue.append(10)       # Here 10 is added to queue and following the 10 ,20,30,..60 are added 
queue.append(20)       #queue becomes = [ 10,20,30,40,50,60]
queue.append(30)       # In queue 10 is the first item that is added firstly so it must be removed first 
queue.append(40)       
queue.append(50)
queue.append(60)
print(queue) 

''' pop(0) ----> helps to pop out the elements that are first inserted in the queue '''

queue.pop(0)           #10 is returned and removed from the queue 
print(queue)
queue.pop(0)            # 20 is removed 
print(queue)
queue.pop(0)            # 30 is removed
print(queue)
queue.pop(0)            #40 is  removed
print(queue)
queue.pop(0)
print(queue)          # 50 is removed 
