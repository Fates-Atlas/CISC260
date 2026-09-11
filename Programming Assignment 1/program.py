user_value = input("Please enter a value in base 10: ")

def make_binary(value):
    result = ""
    bit = 31
    value = int(value)
    while (bit >= 0):
        currBit = 2**bit
        if (value>=currBit):
            result += "1"
            value -=currBit
        else:
            result += "0"
        bit -= 1

    print(f"{len(result)}\n")
    return result

def make_hex(value):
    result = ""
    bit = 7
    value = int(value)
    while(bit>=0):
        currBit = 16**bit
        if
        

print(make_binary(user_value))