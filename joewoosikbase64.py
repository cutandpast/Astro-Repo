encode = str(input())
strlen = len(encode)
strlen1 = ((strlen+2)//3)*4
strlen2 = ((strlen+2)//3)*3*8

x = 0
y = 6
resultstr = ""

for i in range(0,strlen):
    temp = str(bin(ord(encode[i]))[2:9].zfill(8))
    resultstr += temp

resultstr = resultstr.ljust(strlen2, "0")
# print(resultstr)
for i in range(0,strlen1):
    encode1 = resultstr[x:y]
    if resultstr[x:y] == "000000":
        print("=")
        x += 6
        y += 6
    elif int(encode1,2) < 26:
        encode2 = int(encode1, 2) + 65
        print(chr(encode2))
        x += 6
        y += 6
    elif int(encode1,2) > 51:
        encode2 = int(encode1, 2) - 4
        print(chr(encode2))
        x += 6
        y += 6
    else:
        encode2 = int(encode1, 2) + 71
        print(chr(encode2))
        x += 6
        y += 6
