from tokenize import Triple


while True:
    shoppinList = ['apples', 'bananas', 'carrots', 'potatoes', 'dates', 'eggplant']
    myIndex = input('Enter an index: ')
    myIndex = int(myIndex) #convert to integer
    myElement = shoppinList[myIndex]
    print('The element at index', myIndex, 'is', myElement)
    
    goAgain = input('Press Return/Enter to quit, or anything else to continue): ')
    if goAgain == "": # check for no entry
        break #user said they want to quit
    if goAgain == True:
        continue
print('Fin')