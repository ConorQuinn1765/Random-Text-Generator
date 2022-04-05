from rand_writer import RandWriter
import sys

if(len(sys.argv) == 2):
    with open(sys.argv[1], 'r') as textFile:
        text = textFile.read()
else:
    text = input('Enter text to train the model on: ')

k_gram_size = int(input('What size seed word do you want to use: '))
writer = RandWriter(text, k_gram_size)

length = int(input('How many characters do you want to generate: '))
word = input(f'Enter a {k_gram_size} letter word to seed the new text: ')
print()

print(writer.generate(word, length))
