

stack = []

def add_num(number):
    while (number != 0):
        stack.append(number % 10)
        number = int(number / 10)

def reverse_int(number):

    add_num(number)

    reverse = 0
    index = 1

    while (len(stack) > 0):
        reverse = reverse + (stack[len(stack) - 1] * index)
        stack.pop()
        index = index * 10
    return reverse


print(reverse_int(344553224))