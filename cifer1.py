from tokenize import Triple


var = 0
shoppinList = ['apples', 'bananas', 'carrots', 'potatoes', 'dates', 'eggplant']

while var != 'Q':
    myIndex = input(f"Enter an index: from 0 to {len(shoppinList)} or Q to quit'")
    #if myIndex == 'Q' or myIndex == 'q':
    if  str.lower(myIndex) == 'q':
        #str.lower converts any character to lowercase
        print('Fin')
        exit()
    myIndex = int(myIndex) #convert to integer
    if myIndex > len(shoppinList) or myIndex < 0:
        print("Invalid response")
        continue
    myElement = shoppinList[myIndex]
    print('The element at index', myIndex, 'is', myElement)
print('Fin')