# https://codeshare.io/QnBOoL

file = open('output.csv', "w")
file1 = open('data.txt')

data = file1.read()
row = data.splitlines()
row = [i[i.index('. ') + 2:].replace(': ', ',') for i in row]
row = sorted(row)
row1 = 'name,grade\n'
data = row1 + '\n'.join(row)

file.write(data)
file.close()



