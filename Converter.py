def convert_to_binary_from_decimal(n):
    '''Argument should be an integer'''
    arr = []
    while(n!=0 and n!=1):
        k= n%2
        arr.append(str(k))
        n = int(n/2)
    arr.append("1")
    arr.reverse()
    return str("".join(arr))


def convert_to_decimal_from_binary(n):
    '''Argument can be in both string or integer form'''
    n = str(n)
    sum = 0
    for i in range(len(n)):
        k = int(n[i])
        sum += (2**(len(n)-i-1))*k
    return sum

# utility function
def toCharacterArray(string):
    array = []
    for i in range(len(string)):
        array.append(string[i])
    return array


def convert_to_binary_from_string(string):
    array = toCharacterArray(string)
    arr = []
    for i in range(len(array)):
        arr.append(convert_to_binary_from_decimal(ord(array[i])))
    
    return " ".join(arr)


def convert_to_string_from_binary(n):
    '''Argument should be in string'''
    array = n.split(" ")
    string = []
    for i in range(len(array)):
        string.append(chr(convert_to_decimal_from_binary(array[i])))
    
    return ("".join(string))


def convert_to_octal_from_decimal(n):
    '''Argument should be an integer'''
    k = 0
    arr = []
    if n<8:
        return n
    while(n!=0 and n!=1 and n!=2 and n!=3 and n!=4 and n!=5  and n!=6 and n!=7):
        k = n%8
        arr.append(str(k))
        n = int(n/8)
    arr.append(f"{n}")
    arr.reverse()
    return str("".join(arr))


def convert_to_decimal_from_octal(n):
    '''Argument can be in both string or integer form'''
    n = str(n)
    sum = 0
    for i in range(len(n)):
        k = int(n[i])
        sum += (8**(len(n)-i-1))*k
    return sum


# Testing
if __name__ == '__main__':
    print(convert_to_binary_from_decimal(90))
    a = convert_to_binary_from_string("Paras Punjabi Program")
    print(a)
    p = convert_to_string_from_binary("1010000 1100001 1110010 1100001 1110011 100000 1010000 1110101 1101110 1101010 1100001 1100010 1101001 100000 1010000 1110010 1101111 1100111 1110010 1100001 1101101")
    print(p)
    print(convert_to_decimal_from_binary(100))
    print(convert_to_octal_from_decimal(2050))
    print(convert_to_decimal_from_octal(4002))