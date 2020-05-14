

def is_palindrome(text):
    left_index = 0
    right_index = len(text) - 1
    while left_index <= right_index:
        if text[left_index] != text[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True




    def is_palindrome_recursive(text, left_index, right_index):
        #base cases

        if text[left_index] != text[right_index] :
            return False
        if left_index == right_index or left_index > right_index:
            return True
        #recursive case
        return is_palindrome_recursive(text, left_index + 1, right_index - 1)