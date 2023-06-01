
#suppose we want to create a string that says "Learn how to ______"
# word = "make money" # some string variable

#There are a few ways to do that
#print("Learn how to " + word)
#print("Learn how to ".format(word))
#print(f"Learn how to {word}")


adj= input("Adjective: ")
verb1= input("Verb: ")
verb2= input("Verb: ")
hobbie = input("A hobbie: ")
famous_person= input("A famous person: ")

madlib = f"Computer Programming is so {adj}! It makes me so excited all the time because \n" \
        f"I love to {verb1}.Stay hydrated and  {verb2} like you are {famous_person}"

print(madlib)