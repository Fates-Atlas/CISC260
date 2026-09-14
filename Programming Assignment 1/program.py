user_value = input("Please enter a value in base 10: ")

def make_binary(value: str) -> str:
    result = ""
    bit = 31
    #Allow only positive integers
    value = abs(int(value))
    while (bit >= 0):
        #whitespace to separate by nibbles for improved readability. 
        if ((bit+1) % 4 == 0 and bit !=31): 
            result +=" "
        currBit = 2**bit
        if (value>=currBit):
            result += "1"
            value -=currBit
        else:
            result += "0"
        bit -= 1
    return result
#Currently not woring. E.G. value = -10. 
def twos_complement(value: str) -> str:
    bit = 36
    result = ""
    count = 0

    while (count<=bit):
        if value[count] != " ":
            result += "0" if value[count] == "1" else "1"
        else: 
            result += " "
        count += 1        

    if value[31] == "1":
        result+= "10"
    else: 
        result+= "01"

    return result

def make_hex(value: str) -> str:
    pass



        
if (int(user_value) < 0):
    print(f"Twos-compliment Binary: {twos_complement(make_binary(user_value))}")
else: 
    print(f"Binary: {make_binary(user_value)}")
