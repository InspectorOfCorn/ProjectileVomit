#string concatenation (aka how to put strings together)
#suppose we want to create a string that says "This is one crazy _______"
#individual = "Cat"
#a few ways to do this
#print("This is one crazy " + individual)
#print("This is one crazy {}".format(individual))
#^^^^ second line is useful for later codes
#print(f"This is one crazy {individual}")
#Third line is an F string (i havent used it a lot)

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"computer programming is so {adj}! It makes me so excited all the time \
    because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)