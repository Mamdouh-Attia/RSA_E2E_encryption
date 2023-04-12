#This is a mapping function to encode a message character into a number
def alphabet_encoder(msg):
    if msg == " ":
        return 36
    if ord(msg) >= 48 and ord(msg) <= 57:
        return int(msg)
    if ord(msg) >= 97 and ord(msg) <= 122:
        return ord(msg) - 87
    else:
        return 36
#This is a mapping function to decode a number into a message character
def alphabet_decoder(msg):
    if msg == 36:
        return " "
    if msg >= 0 and msg <= 9:
        return str(msg)
    if msg >= 10 and msg <= 35:
        return chr(msg + 87)
    else:
        return " "
#providing test for alphabet_encoder
def test_alphabet_encoder():
    assert alphabet_encoder(" ") == 36
    assert alphabet_encoder("a") == 10
    assert alphabet_encoder("b") == 11
    assert alphabet_encoder("c") == 12
    assert alphabet_encoder("z") == 35
    assert alphabet_encoder("0") == 0
    assert alphabet_encoder("5") == 5
    assert alphabet_encoder("9") == 9
    print ("Excellent!")
# test_alphabet_encoder()

# Req2: must encode an input message as a number.
# We will use the following scheme to convert plaintext (input) messages to numbers:
# Convert any extra characters to spaces using alphabet_encoder,
# Group the plaintext into sets of five characters per group.
# Each group must have five characters,Convert each group into a separate number
# If the grouping is [c4,c3,c2,c1,c0] then the number is sum(c4*36^4 + c3*36^3 + c2*36^2 + c1*36^1 + c0*36^0)
def encode(msg):
    #convert to list
    msg = list(msg)
    #convert to numbers
    msg = [alphabet_encoder(i) for i in msg]
    #split into groups of 5, sum them up and return a list of numbers
    msg = [msg[i:i+5] for i in range(0, len(msg), 5)] #split into groups of 5
    if len(msg[-1]) < 5:
        for i in range(5 - len(msg[-1])):
            msg[-1].append(36)
    numbers = [sum([msg[i][j] * 37 ** (4 - j) for j in range(5)]) for i in range(len(msg))] #sum up the groups
    return numbers

# print(encode("hi s7"))
#now for function of reverse operation
def decode(numbers):
    #convert each number into a group of 5 numbers
    groups = []
    for number in numbers:
        group = []
        for i in range(5):
            digit = number // (37 ** (4 - i))
            group.append(digit)
            number -= digit * 37 ** (4 - i)
        groups.append(group)
    #convert each number in the group back to letters
    msg = []
    for group in groups:
        for digit in group:
                msg.append(alphabet_decoder(digit))
    return ''.join(msg)

#function to test the encode and decode functions together as an interface
# print(decode(encode("hi s7123848484351556844")))