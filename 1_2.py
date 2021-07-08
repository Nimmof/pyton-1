ls = []
total = 0
total_17 = 0
index = 0
for i in range(1, 1001):
    if i % 2 != 0:
        ls.append(i ** 3)
        str_i = 0
        count = 0
        ls_str = str(ls[index])
        while str_i < len(ls_str):
            count = count + int(ls_str[str_i])
            str_i += 1
        if count % 7 == 0:
            total = total + ls[index]
        str_i_17 = 0
        count_17 = 0
        ls_17 = ls[index] + 17
        ls_17_str = str(ls_17)
        while str_i_17 < len(ls_17_str):
            count_17 = count_17 + int(ls_17_str[str_i_17])
            str_i_17 += 1
        if count_17 % 7 == 0:
            total_17 = total_17 + ls[index]
        index += 1
print(total)
print(total_17)
