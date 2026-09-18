word = input("Enter a word : ")
print("Your word backwards is:" , word[::-1])
print("Your word in Uppercase is:", word.upper())
length = (len(word))
print("The length of your word is:" , length)
first = word[0]
print("The code of the first letter in your word is:" , ord(first))
mid = length//2
middle = word[mid]
print("The middle letter in your word is:" , middle)
if word.lower() == word[::-1].lower() :
    print("Palindrome: True")
else:
    print("Palindrome: False")
