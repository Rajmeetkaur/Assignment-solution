# Python program to find largest 
# number in a list 

  
# list of numbers 

list1 = [10, 20, 4, 45, 99] 

  
# sorting the list 
list1.sort() 

  
# printing the last element 

print("Largest element is:", list1[-1])

# Merge two list
a=[]
c=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    a.append(b)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    c.append(d)
new=a+c
new.sort()
print("Sorted list is:",new)

# Python program to find second largest
# number in a list
 
# list of numbers
list1 = [10, 20, 4, 45, 99]
 
# sorting the list
list1.sort()
 
# printing the second last element
print("Second largest element is:", )

# Python3 program to swap first 
# and last element of a list 
  
# Swap function 
def swapList(newList): 
      
    newList[0], newList[-1] = newList[-1], newList[0] 
  
    return newList 
      
# Driver code 
newList = [12, 35, 9, 56, 24] 
print(swapList(newList))
