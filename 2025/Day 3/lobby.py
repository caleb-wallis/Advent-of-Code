
input : str = "23423423478"

pointer : int = 2

tens : int = int(input[0])
ones : int = int(input[1])

total : int = 0

for i, ch in enumerate(input[2:], start=2):
    num = int(ch)

    if num > tens and i != len(input) - 1:   # not last char
        tens = num
    elif num > ones:
        ones = num

total = total + tens * 10 + ones

#print(tens, ones)
print(total)