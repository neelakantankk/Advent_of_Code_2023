import re

def part_a(infile):

    result = 0
    
    for line in infile.readlines():
        digits = re.findall("\d{1}",line.strip())
        num = int(f"{digits[0]}{digits[-1]}")
        result += num

    return result


def part_b(infile):
    
    result = 0

    regex = re.compile(r"\d{1}|on(?=e)|tw(?=o)|thre(?=e)|four|fiv(?=e)|six|seve(?=n)|eigh(?=t)|nin(?=e)")

    imap = {
            "1":1,
            "on":1,
            "2":2,
            "tw":2,
            "3":3,
            "thre":3,
            "4":4,
            "four":4,
            "5":5,
            "fiv":5,
            "6":6,
            "six":6,
            "7":7,
            "seve":7,
            "eigh":8,
            "8":8,
            "9":9,
            "nin":9,
            "0":0
        }

    for line in infile.readlines():

        digits = regex.findall(line.strip())
        num = f"{imap[digits[0]]}{imap[digits[-1]]}"
        result+= int(num)

    return result
        

