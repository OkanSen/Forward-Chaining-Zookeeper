# Made by VERBATIM
# IDs and Names: 
# 21403007 Mastan Abdulkhaligli
# 21202377 Okan Sen
# 21503756 Nurlan Farzaliyev

"""
We have implemented a simple, specialized forward chaining (FC) to identify the animal(s) if all the required
information is given in advance, except the ones that program supposed to find by triggering and firing the 
rules. To implement FC we have considered pseudo algortithms provided in Wilson (Ch7) and Bob Berwick.
"""


"""
# The program works in FORWARD CHAINING (FC)
# The zookeeper inserts all his observations to the program. The observations must be added without any mistakes and strings should match.
# The program then starts iterating through all of these known facts and asserts new binding sets according to the rules; such as if animal has hair then it is
# a mammal. These assertions are added to the WM. THe size of WM grows. 

# When an animal is found/realized the program stops any further checking for the that specific animal. All the assumptions are kept in one big list of tuples.
# The tuples contain the animal's known information such as "has hair", and the second index holds the animal's name; "Stretch". 
#
# The checking process goes like this; if Stretch is found to be a "mammal" then we check if Stretch also "has long neck" and "has long legs" etc... to see if it is a 
# giraffe, or if it is a "bird" we check if it "has long legs", "is black and white" etc... 

# An example output is attached below the program

# """

# This boolean acts as "an if is fired"
is_changed = True

# Here is our Working Memory that we insert our known facts into.
Working_Memory = [
    ["has hair","stretch"],["chews cud","stretch"],["has long legs","stretch"],["has long neck","stretch"],["has tawny color","stretch"],["has dark spots","stretch"],
    ["eats meat","Sadie"], ["has feathers","Sadie"],["lays eggs","Sadie"],["flies", "Sadie"],["is a good flyer","Sadie"],["swims","Sadie"],["is black and white","Sadie"],
    ["has pointed teeth","swifty"],["has claws","swifty"],["has dark spots","swifty"],["has tawny color","swifty"],["has forward pointing eyes","swifty"],["has hair","swifty"],
    ["has feathers","Splashy"],["lays eggs","Splashy"],["does not fly","Splashy"],["is black and white","Splashy"],["swims","Splashy"],
    ["is black and white", "Sweetie"], ["has long neck", "Sweetie"], ["has long legs", "Sweetie"], ["does not fly", "Sweetie"], ["has feathers", "Sweetie"], ["lays eggs", "Sweetie"]
    ]

# Empty list to append final animal assumptions
results = []

# This method works to assert a new binding set to the WM. If the parameter fact is already inside the WM, we do not add it,
# and boolean does not turn True, meaning that no if is fired. Otherwise, the fact is added to WM and program knows an if has been fired.
def assert_fact(fact,is_changed):
    
    if not fact in Working_Memory:
        Working_Memory.append(fact)
        is_changed = True

# We also want to keep our final assumptions in a separate list, to print them easily. If the found animal is already found before
# we do not add it to this list as well. Same as before.
def assert_result(fact):
    if not fact in results:
        results.append(fact)
            
    
# This loop continues until all the searched animals are found.
# is_changed is a boolean which keeps track of firing a rule. If
# all the if patterns are satisfied, the rule gets triggered
# which causes it to be fired and control the is_changed variable
# to determine either to finish or continue the chaining
while is_changed:
    is_changed = False
    for item in Working_Memory:
        # Z1 
        if item[0] == "has hair":
            assert_fact(["is a mammal",item[1]],is_changed)
        # Z2
        if item[0] == "gives milk":
            assert_fact(["is a mammal",item[1]],is_changed)
        # Z3
        if item[0] == "has feathers":
            assert_fact(["is a bird",item[1]],is_changed)
        # Z4
        # Some mammals fly and some reptiles lay eggs but no mammal or reptile does both so these if s must be "or"ed.
        # See Winston pg. 122 about Z4
        if item[0] == "flies" or ["lays eggs",item[1]] in Working_Memory:
            assert_fact(["is a bird",item[1]],is_changed)
        # Z5
        if item[0] == "is a mammal" and ["eats meat",item[1]] in Working_Memory:
            assert_fact(["is a carnivore",item[1]],is_changed)
        # Z6
        if item[0] == "is a mammal" and (["has pointed teeth",item[1]] in Working_Memory or ["has claws",item[1]] in Working_Memory or ["has forward pointing eyes",item[1]] in Working_Memory):
            assert_fact(["is a carnivore",item[1]],is_changed)
        # Z7
        if item[0] == "is a mammal" and ["has hoofs",item[1]] in Working_Memory:
            assert_fact(["is an ungulate",item[1]],is_changed)
        # Z8
        if item[0] == "is a mammal" and ["chews cud",item[1]] in Working_Memory:
            assert_fact(["is an ungulate",item[1]],is_changed)
        # Z9
        if item[0] == "is a carnivore" and ["has tawny color",item[1]] in Working_Memory and ["has dark spots",item[1]] in Working_Memory:
            assert_fact(["is a cheetah",item[1]],is_changed)
            assert_result(["is a cheetah",item[1]])
        # Z10
        if item[0] == "is a carnivore" and ["has tawny color",item[1]] in Working_Memory and ["has black stripes",item[1]] in Working_Memory:
            assert_fact(["is a tiger",item[1]],is_changed)
            assert_result(["is a tiger",item[1]])
        # Z11
        if item[0] == "is an ungulate" and ["has long legs",item[1]] in Working_Memory and ["has long neck",item[1]] in Working_Memory and ["has tawny color",item[1]] in Working_Memory and ["has dark spots",item[1]] in Working_Memory:
            assert_fact(["is a giraffe",item[1]],is_changed)
            assert_result(["is a giraffe",item[1]])
        # Z12
        if item[0] == "is an ungulate" and ["has white color",item[1]] in Working_Memory and ["has black stripes",item[1]] in Working_Memory:
            assert_fact(["is a zebra",item[1]],is_changed)
            assert_result(["is a zebra",item[1]])
        # Z13
        if item[0] == "is a bird" and ["does not fly",item[1]] in Working_Memory and ["has long legs",item[1]] in Working_Memory and ["has long neck",item[1]] in Working_Memory and ["is black and white",item[1]] in Working_Memory:
            print("pint")
            assert_fact(["is an ostrich",item[1]],is_changed)
            assert_result(["is an ostrich",item[1]])
        # Z14
        if item[0] == "is a bird" and ["does not fly",item[1]] in Working_Memory and ["swims",item[1]] in Working_Memory and ["is black and white",item[1]] in Working_Memory:
            assert_fact(["is a penguin",item[1]],is_changed)
            assert_result(["is a penguin",item[1]])
        # Z15
        if item[0] == "is a bird" and ["is a good flyer",item[1]] in Working_Memory:
            assert_fact(["is an albatross",item[1]],is_changed)
            assert_result(["is an albatross",item[1]])

# Print all of the WM
print()
print("Working memory with all consequents:")
print(Working_Memory)

print()

# Print found animals      
for item in results:
    print(item[1],item[0])

# Example Output
"""
Working memory with all consequents:
[['has hair', 'stretch'], ['chews cud', 'stretch'], ['has long legs', 'stretch'], ['has long neck', 'stretch'], ['has tawny color', 'stretch'], ['has dark spots', 'stretch'], ['eats meat', 'Sadie'], ['has feathers', 'Sadie'], ['lays eggs', 'Sadie'], ['flies', 'Sadie'], ['is a good flyer', 'Sadie'], ['swims', 'Sadie'], ['is black and white', 'Sadie'], ['has pointed teeth', 'swifty'], ['has claws', 'swifty'], ['has dark spots', 'swifty'], ['has tawny color', 'swifty'], ['has forward pointing eyes', 'swifty'], ['has hair', 'swifty'], ['has feathers', 'Splashy'], ['lays eggs', 'Splashy'], ['does not 
fly', 'Splashy'], ['is black and white', 'Splashy'], ['swims', 'Splashy'], ['is black and white', 'Sweetie'], ['has long neck', 'Sweetie'], ['has long legs', 'Sweetie'], ['does not fly', 'Sweetie'], ['has feathers', 'Sweetie'], ['lays eggs', 'Sweetie'], ['is a mammal', 'stretch'], ['is a bird', 'Sadie'], ['is a mammal', 'swifty'], ['is a bird', 'Splashy'], ['is a bird', 'Sweetie'], ['is an ungulate', 'stretch'], ['is an albatross', 'Sadie'], ['is a carnivore', 'swifty'], ['is a penguin', 'Splashy'], ['is an ostrich', 'Sweetie'], ['is a giraffe', 'stretch'], ['is a cheetah', 'swifty']]

Sadie is an albatross
Splashy is a penguin
Sweetie is an ostrich
stretch is a giraffe
swifty is a cheetah



"""


