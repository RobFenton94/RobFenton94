# This is my string.
def my_string(string):
    return ' '.join(
        ''.join(
            # The below sequence identifies the pattern of the capitalisation.
            char.upper() if idx % 2 != 1 else char.lower()
            for idx, char in enumerate(word)
        )
        for word in string.split()
    )
#  Printing the results of the above code.


print(my_string("This is my string"))

# This is my string.
my_string = "This is my string"

sentence = my_string.split()

sentence[0] = sentence[0].upper()  # List created to split the sentence into two parts.
sentence[2] = sentence[2].upper()

sentence = ' '.join(sentence)  # Join function to connect modified words.

print(sentence)
