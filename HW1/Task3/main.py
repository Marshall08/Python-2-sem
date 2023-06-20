# https://codeshare.io/QnBOoL

file = open('output.txt', "w")
file1 = open('input.txt')
data = file1.read()

words = data.split()
lines = []
line = ""
for word in words:
    if len(line + " " + word) <= 20:
        line += " " + word
    else:
        lines.append(line.strip())
        line = word
lines.append(line.strip())
data = "\n".join(lines)

file.write(data)
file.close()
