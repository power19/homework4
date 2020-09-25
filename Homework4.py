"""
Create a global variable called myUniqueList. 
It should be an empty list to start
"""
# Global Variables
myUniqueList = []
myLeftovers = []

"""
Next, create a function that allows you to add things to that list. 
Anything that's passed to this function should get added to myUniqueList, 
unless its value already exists in myUniqueList. 
If the value doesn't exist already, 
it should be added and the function should return True. 
If the value does exist, it should not be added, 
and the function should return False;

Add another function that pushes all the rejected inputs into a separate global 
array called myLeftovers. 
If someone tries to add a value to myUniqueList but it's rejected (
for non-uniqueness), 
it should get added to myLeftovers instead.
"""
def leftovers(leftover):
    if leftover in myUniqueList:
        myLeftovers.append(leftover) 
    return myLeftovers

def addValues(toAppend):
    result = False
    if toAppend not in myUniqueList:
        result = True
        myUniqueList.append(toAppend)
    else: 
        leftovers(toAppend)   
    return print(result)



var0 = 0 
var1 = 1
var2 = 2
var3 = 3
var4 = 4
var5 = 5 
var6 = 6
var7 = 7

addValues(var0)
addValues(var1)
addValues(var2)
addValues(var3)
addValues(var4)
addValues(var5)
addValues(var6)
addValues(var7)
addValues(var1)
addValues(var2)
addValues(var3)
addValues(var4)
addValues(var5)
addValues(var6)
addValues(var7)
addValues(var1)
addValues(var2)
addValues(var3)
addValues(var4)
addValues(var5)
addValues(var6)
addValues(var7)
addValues(var1)
addValues(var2)
addValues(var3)
addValues(var4)
addValues(var5)
addValues(var6)
addValues(var7)
addValues(var1)
addValues(var2)
addValues(var3)
addValues(var4)
addValues(var5)
addValues(var6)
addValues(var7)
addValues(var1)
addValues(var2)
addValues(var3)
addValues(var4)
addValues(var5)
addValues(var6)
addValues(var7)
print(myUniqueList)
print(myLeftovers)