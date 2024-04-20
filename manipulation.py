# the user enters a sentence
str_manip = input("Please enter a sentence: ")

# calculate the length of the sentence
length = len(str_manip)
print("Length of str_manip:", length)

# last letter of the sentence
last_letter = str_manip[-1]

# replace every occurrence of the last letter with @
str_manip_modified = str_manip.replace(last_letter, '@')

# print the modified sentence
print("Modified string:", str_manip_modified)

# the last 3 characters in str_manip reversed
last_three_reversed = str_manip[-1:-4:-1]

# printed result
print("Last three characters in str_manip reversed", last_three_reversed)

# 5 letter word made up of the first 3 characters and last two characters of str_manip
first_three = str_manip[:3]
last_two = str_manip[-2:]

# form a 5 letter word
five_letter_word = first_three + last_two

# print the word
print("Five-letter word:", five_letter_word)
