# Write a function to reverse a string without using string slices or inbuilt methods

# We want to take in a string, find each position index of a character and push the character to the back 
# of the string



# input = 'Hello' output = 'olleH'


# transverse through the string and push character to the end of the string

# turn string into an array
# loop from - to len str array exclusive
# get the reverse get the len by 1, then appen letter with the

a = 'Hello'

def reverse_string(str):
    reverse_string = ''
    index = len(str) - 1
    while index >= 0:
        reverse_string += str[index]
        index -= 1
    return reverse_string

