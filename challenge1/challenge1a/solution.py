# Implement a string compression using python.
# For example, aaaabbbccddddddee would become a4b3c2d6e2. 

# If the length of the string is not reduced, return the original string.

def compress(s: str):
    char_count = 1
    pointer1 = 0
    pointer2 = 1
    compressed_string = ''
    compressed = False
    while pointer2 < len(s) and pointer1 < pointer2:
        if s[pointer1] == s[pointer2]:
            char_count = char_count + 1
            compressed = True
            pointer2 = pointer2 + 1
        else:
            compressed_string = compressed_string + s[pointer1] + str(char_count)
            char_count = 1
            pointer1 = pointer2
            pointer2 = pointer2 + 1
    
    compressed_string = compressed_string + s[pointer1] + str(char_count)

    if compressed:
        return compressed_string
    else:
        return s

    

if __name__ == '__main__':
    string = input('Enter string to compress: ')
    response = compress(string)
    print('response', response)