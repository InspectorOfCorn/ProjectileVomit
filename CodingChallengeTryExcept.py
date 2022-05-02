from xml.dom.minidom import Element


def getIntegerInRange(prompt, lowEnd, includedHighEnd):
    while True:
        number = input(prompt)
        try:
            number = int(number)
        except:
            print('That is not an integer, please try again.')
            continue
        #everything ok
        if (number < lowEnd) or (number > includedHighEnd):
            print('The number you entered is not in the range of -5 to 20', \
            lowEnd, 'and', includedHighEnd)
        else:
            return number
#Ask the user to give a number between -5 and 20
myInteger = getIntegerInRange('Please enter an integer: ', -5, 21)
print('The number you entered was: ', myInteger)
