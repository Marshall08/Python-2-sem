# https://codeshare.io/QnBOoL

file = open('output.txt', "w")
file1 = open('input.txt')
data = file1.read()

data = data.lower().replace('.', '').replace(',', '')
word = data.split()
words = dict.fromkeys(set(word), 0)

for i in word:
    words[i] += 1

sort = sorted(words.items(), key=lambda x: [x[1], x[0]], reverse=True)
res = sort[:10]
data = '\n'.join([f"{word},{count}" for word, count in res])

file.write(data)
file.close()
