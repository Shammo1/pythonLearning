#any sentence which is written in "..." '...' this it will consider it as string
sentence = "i love PYTHON"

# converts first character to uppercase and others to lowercase
capitalized_string = sentence.capitalize()

print(capitalized_string)

# Output: I love python

sentence = "Python is awesome"

# returns the centered padded string of length 24 
new_string = sentence.center(24, '*')

print(new_string)

# Output: ***Python is awesome****
text = "pYtHon"

# convert all characters to lowercase
lowercased_string = text.casefold()

print(lowercased_string)

# Output: python
message = 'python is popular programming language'

# number of occurrence of 'p'
print('Number of occurrence of p:', message.count('p'))

# Output: Number of occurrence of p: 4
message = 'Python is fun'

# check if the message ends with fun
print(message.endswith('fun'))

# Output: True
message = 'Python is a fun programming language'

# check the index of 'fun'
print(message.find('fun'))

# Output: 12
# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef"
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)

# translate string
print("Translated string:", string.translate(translation))