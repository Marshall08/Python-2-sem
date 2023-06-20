# https://codeshare.io/QnBOoL

file = open('output.txt', "w")
file1 = open('input.txt')
data = file1.read()

row = data.splitlines()
idx = [i[i.index('KP') + 2:i.index(' - ')].replace('-', '.').split('.') for i in row]
idx = [[int(k) for k in i] for i in idx]
row_index = list(zip(idx, row))
data = '\n'.join([i[1] for i in sorted(row_index)])

file.write(data)
file.close()




