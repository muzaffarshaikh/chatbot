filename = 'corpus/corpus.txt'

with open(filename, 'r') as file:
    data = file.read().replace('\n', '')
    file.close()
