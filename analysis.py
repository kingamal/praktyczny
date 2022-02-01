content = '''
5
15 

40
'''

# Jeśli chcemy wczytać wydatki z pliku, to wtedy stosujemy poniższy kod:
# with open('wydatki.txt') as stream:
#     content = stream.read()

lines = content.split('\n')
count = 0
sum = 0
for line in lines:
    if line != '':
        expense = int(line)
        print(expense)
        sum += expense
        count += 1
mean = sum/count
print('Liczba wydatków: ', count)
print('Suma wydatków: ', sum)
print('Średnia suma wydatków: ', mean)
