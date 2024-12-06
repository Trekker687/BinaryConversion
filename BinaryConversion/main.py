def decimaltobinary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal == decimal //2
    return binary if binary else '0'
decimal_num = int(input("Enter number: "))
binary_representation = decimaltobinary(decimal_num)
print("the binary representation of ", decimal_num,  "is" ,binary_representation )