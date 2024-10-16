#Serenity and Lily
def too_long (word):
    if len (word) > 140:
        print ("Too long to be sent in a single SMS message.")
    else:
        print (word)


#emoji in strings
import unicodedata
print (unicodedata.lookup("sun"))
print (unicodedata.lookup("cat"))
print (unicodedata.lookup("two hearts"))

print ("Today is a good day",(unicodedata.lookup("two hearts")))

print (unicodedata.name("&"))
print (unicodedata.name("["))
print (unicodedata.name("/"))
