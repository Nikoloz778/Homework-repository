def string_capitalize(string):
    splited = string.split()
    sec_list=[]
    for i in splited:
        i=i.capitalize()
        sec_list.append(i)
    sec_list="".join(sec_list)
    return print(sec_list)

string_capitalize("i am georgian")




