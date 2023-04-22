str_1 = 'This is a string'
str_2 = 'This is also a string'
str_3 = 'I am a string'
str_4 = 'Do not print me'

f = open('strings.txt', 'w')
f.write(f'{str_1}\n{str_2}\n')
f.close()

f = open('strings.txt', 'a')
f.write(f'{str_3}\n{str_4}\n')
f.close()

f = open('strings.txt', 'r')
for row in f:
    print(row)
