#Serenity and Lily
def letter_o (word):
    total = 0
    for x in word:
        if x == "o":
            total += 1
    return total

letter_o ("bonobos")

#Indexing
print ("abc"[0])

print ("abc"[2])

print ("waffles"[1])

dinner = "falafels"
print (dinner[4])

print (["a", "b", "c"][2])

print ([1, 2, 3, 4][0])

colors = ["red", "green", "blue"]
print (colors[1])

countdown = [3, 2, 1, "action!"]
print (countdown[3])

print ("frog"[-1])

print ("fish"[-2])

print ("fish"[2])
