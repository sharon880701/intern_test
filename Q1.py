str = input('')
def Q1_1(str):
    print(str[::-1])
Q1_1(str)
str2 = input('')
def Q1_2(str):
    s_list = str.split( )
    outlist =[]
    for i in s_list:
        outlist.append(i[::-1])
    print(" ".join(outlist))

Q1_2(str2)