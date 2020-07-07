def ConvertASCIIandBinary(words):
    list_word = list(words)
    list_ASCII = []
    binary = []
    for o in list_word:
        list_ASCII.append(ord(o))
    for data in list_ASCII:
        binary.append(format(data, "b").zfill(8))
    binary = "".join(binary)
    return DivideSixandEncodeBase64(binary)

def DivideSixandEncodeBase64(binaryValue):
    li = []
    res = []
    for x in range(len(binaryValue)):
        li.append(int(binaryValue[x]))
    for y in range(0,len(binaryValue),6) :
        divide = binaryValue[y:y+6]
        returnValue = int(binaryValue[y:y+6], 2)
        num = int(binaryValue[y:y+6], 2)
        if num <= 25:
            res.append(chr(num+65))
        elif num <= 51:
            res.append(chr(num+71))
        elif num <= 61:
            res.append(chr(num-4))
        elif num == 62:
            res.append(chr(0))
        elif num == 63:
            res.append(chr(47))
    res = "".join(res) 
    return res

if __name__ == "__main__":
    words = "abc"
    print(ConvertASCIIandBinary(words))
