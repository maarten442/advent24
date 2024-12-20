# in the ASCII char set 65 - 90 are capital letters
# 97 to 122 are lowercase letter
# The rest are other types of characters

LOWER_CASE = range(97, 123)
UPPER_CASE = range(65, 91)

def shift_ascii(character, shift):
    
    ascii_num = ord(character)

    if ascii_num in LOWER_CASE:
        return chr(((ascii_num - 97 + shift) % 26) + 97)
    
    elif ascii_num in UPPER_CASE:
        return chr(((ascii_num - 65 + shift) % 26) + 65)
    
    return character

if __name__ == "__main__":

    input_str = "Wrap around Python 3.9 boi!"
    shift_param = 27
    result = ""
    for j in input_str:
        result += shift_ascii(j, shift_param)
    print(result)
    decipher = ""
    for j in result:
        decipher += shift_ascii(j, - shift_param)
    print(decipher)
        