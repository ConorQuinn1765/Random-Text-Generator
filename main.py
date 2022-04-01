from rand_writer import RandWriter
import sys

if(len(sys.argv) == 2):
    with open(sys.argv[1], 'r') as textFile:
        text = textFile.read()
else:
    text = input('Enter text to train the model on: ')

k_gram_size = int(input('Size of k_gram: '))
writer = RandWriter(text, k_gram_size)

length = int(input('Characters to generate: '))
word = input(f'{k_gram_size} character word to seed text: ')
print()

print(writer.generate(word, length))
