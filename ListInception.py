#empty list
#somelist = [] # set a list variable to the empty list ~ no elements
#print(somelist)
shoppingList = ['apples', 'bananas', 'carrots', 'potatoes', 'dates', 'eggplant']
myIndex = input('Enter an index: ')
#Enter an index: 3
myIndex = int(myIndex) #convert to integer
myElement = shoppingList[myIndex]
print('The element at index', myIndex, 'is', myElement)
