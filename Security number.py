# 14th project - Security number
# Description: Automatic data masking for social security number | Purpose: To practice str indexing
# TIL: List can be modified but string can't. To modify string, need to convert it to list

def number_masking (number):
    str_to_list =[]
    for i in range(len(number)):
        str_to_list.append(number[i])
    for i in range(len(str_to_list)-4, len(str_to_list)):
        str_to_list[i] = "*"
    masked_number = ""
    for i in range (len(str_to_list)):
        masked_number += str_to_list[i]
    return masked_number

print(number_masking ("980505-1234567"))

#TIL: can also change str to list as below:
#(line 6~8): str_to_list = ****list(number)**** (But this will put number/alphabet/symbol one by one in the list as an individual element)

#TIL: join method // "seperator".join(list)

def number_masking2 (number2):
    strtolist = []
    strtolist = list(number2)
    for i in range(len(strtolist)-4, len(strtolist)):
        strtolist[i] = "*"
    return ''.join(strtolist)

print(number_masking2("980505-1234567"))

#TIL: Can also use str indexing

def number_masking3 (number3):
    return number3[:-4] + "****"

print(number_masking3 ("980505-1234567"))