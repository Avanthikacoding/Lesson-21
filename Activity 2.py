def words_match(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("List of words with first and last character same\n" , lst)
    return ctr
count = words_match(["abc" , "cfc" , "xyz" , "aba" , "1221"])
print("Number of words having first and last character same is" , count, "This might be boring but it fun!!!")
