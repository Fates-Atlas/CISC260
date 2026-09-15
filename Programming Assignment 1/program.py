def main():
    user_value = input("Please enter a value in base 10: ")

    if (int(user_value) < 0):
        print(f"Twos-compliment Binary: {twos_complement(make_binary(user_value))}")
        print(f"Hexadecimal: {make_hex(user_value)}")
    else: 
        print(f"Binary: {make_binary(user_value)}")
        print(f"Hexadecimal: {make_hex(user_value)}")

    val = input("Please enter a value in hexadecimal: ")
    print(f"Base 10: {hex_to_base10(val)}")

def make_binary(value: str) -> str:
    """
    This function takes a user's input (string) and coverts it to 
    32-bit binary, in the format of 8 nibbles. 
    Params: value (str) -> The user's input to be calculated
    Returns: (str) -> The value converted to 32-bit binary
    """
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

def twos_complement(value: str) -> str:
    """
    This function takes in a user's input (string) and inverts the binary
    values then adds 1 to the result, in the format of 8 nibbles. ONLY
    USED FOR NEGATIVE VALUES
    Params: Value (str) -> The user's input to be calculated
    Returns: (str) -> The inverted 32-bit binary + 1
    """
    result = []
    #Flip the values
    for char in value:
        if char != " ":
            result.append("0" if char == "1" else "1")
        else:
            result.append(" ")
    #Add one and carry over.
    carry = 1
    #Reverse list AND maintain the original index values
    for i, char in reversed(list(enumerate(result))):
        if char == " ":
            continue #ignore the rest if true
        if (char == "1" and carry):
            result[i] = "0"
            carry = 1
        elif (char == "0" and carry):
            result[i] = "1"
            carry = 0
            break #Nothing left to carry over. Exit loop
    return "".join(result)

def make_hex(value: str) -> str:
    """
    This function takes in a user's input, converts it to 
    32-bit binary, then converts it to 32-bit Hexadecimal. 
    Params: value (str) -> The user's input to be calculated
    Returns: (str) -> A string representation of the value in hexadecimal
    """
    result = ""
    chars = ["A", "B", "C", "D", "E", "F"]
    #Convert to binary or twos-complement (if negative)
    if (int(value) < 0):
        value = twos_complement(make_binary(int(value)))
    else:
        value = make_binary(int(value))
    #Split the string into 4 bits per section
    new_arr = value.split()
    for idx in new_arr:
        sum = 0
        #Convert each section into a new list
        int_list = [int(digit) for digit in idx]
        #Add the values in each section together
        for i, num in enumerate(int_list):
            if num == 1:
                sum += 2**(3-i)
        #Determine the hex value for the nibble
        result += str(sum) if (sum<10) else chars[sum%10]
    return result

def hex_to_base10(value: str) -> int:
    """
    This function takes a user's input in hexadecimal and converts
    it to base 10. Assume every number is positive. 
    Params: value (str) -> The user's input to be calculated
    Returns: (int) The value in base 10. 
    """
    sum = 0
    new_arr = list(value.replace(" ", "").upper())    
    hex_to_base10 = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    #Reverse list but restart index counting 
    for i, val in enumerate(reversed(new_arr)):
        multiply = 0
        if val in "0123456789":
            multiply = int(val)
        elif val in hex_to_base10:
            multiply =  hex_to_base10[val]
        #Calculate
        sum += multiply * (16**i)
    return sum

main()