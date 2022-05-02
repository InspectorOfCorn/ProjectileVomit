count = 1
while count == 1:
        shoppinList = ['apples', 'bananas', 'carrots', 'potatoes', 'dates', 'eggplant']
        myIndex = input('Enter an index: ')
        myIndex = int(myIndex) #convert to integer
        myElement = shoppinList[myIndex]
        print('The element at index', myIndex, 'is', myElement)
        while True:
            goAgain = input('Press Return/Enter to quit): ')
            if goAgain == 'Enter':
                continue
            if goAgain == 'F':
                break
print('Finished')


#if not(width == length):