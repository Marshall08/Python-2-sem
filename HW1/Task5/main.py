# https://codeshare.io/QnBOoL

strs = ["eat","tea","tan","ate","nat","bat"]

words = {}
for i in strs:
    sort = ''.join(sorted(i))
    if sort in words:
        words[sort].append(i)
    else:
        words[sort] = [i]

res = list(map(lambda x: sorted(x), list(words.values())))
print(res)