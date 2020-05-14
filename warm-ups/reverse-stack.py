
def reverse_string(text):

    my_stack = []

    for letter in text:
        my_stack.append(letter)

    reversed_string = ""
    while len(my_stack) != 0:
        reversed_string += my_stack.pop(-1)

    return reversed_string




print(reverse_string('hello'))