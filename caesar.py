# Requires string to be lowercase

# shifts characters by n
def shift(char, n):
    return chr((ord(char) - ord('a') + n) % 26 + ord('a'))

cipher_text = input("enter text to decode: ")

# strings are immutable so convert to workable data
char_list = list(cipher_text)
    
while True:
    action = input("j, k, shift amount, or q to exit \n")
    
    if action == 'j':
        solution = [shift(i, 1) for i in char_list]
        print(''.join(solution))
        char_list = solution
    elif action == 'k':
        solution = [shift(i, -1) for i in char_list]
        print(''.join(solution))
        char_list = solution
    elif action == 'q':
        break
    elif int(action) in range(1, 26):
        solution = [shift(i, int(action)) for i in char_list]
        print(''.join(solution))
        char_list = solution
    