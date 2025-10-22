def search_word (number, dic, position = 0):
    list_num = [int(x) for x in str(number)]
    print(list_num)
    new_dic = []
    pivot = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f']}
    for word in dic:
        if len(word) == len(list_num):
            for letter in pivot[list_num[position]]:
                if list(word)[position] == letter:
                    new_dic.append(word)
    if position == len(list_num)-1:
        return new_dic
    else:
        return search_word(number, new_dic, position + 1)

dic = ['ab', 'ad', 'be', 'cf', 'aa', 'a', 'b']
print(search_word(23, dic))