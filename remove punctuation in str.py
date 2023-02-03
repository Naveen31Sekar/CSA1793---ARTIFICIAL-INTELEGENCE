import string

text = input("Enter a string: ")

text = "".join(c for c in text if c not in string.punctuation)

print("String without punctuation: ", text)
