# Example 1 - Common Design Mistakes
# Program Goal, print a list of words delimeted by commas
# Delimeted: having fixed boundaries or limits.

# Solution 1 - What's wrong? {This is hard coded with periods}
listOfWords = ["hello", "yes", "goodbye", "last"]
print(listOfWords[0]+ "." + listOfWords[1]+ "." + listOfWords[2]+ "." + listOfWords[3])

# Solution 2 
list_of_words = ["hello", "yes", "goodbye", "last"]
toPrint = ""

for i in range(4):
    toPrint += list_of_words
    if i != 3:
        toPrint += ","

print(toPrint)