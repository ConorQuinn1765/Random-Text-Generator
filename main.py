from rand_writer import RandWriter
import sys

if(len(sys.argv) == 2):
    with open(sys.argv[1], 'r') as textFile:
        text = textFile.read()
else:
    text = input('Enter text to train the model on: ')

length = int(input('How many characters do you want to generate: '))
word = input(f'Enter a word to seed the new text(must appear in sample text): ')
writer = RandWriter(text, len(word))

print()

print(writer.generate(word, length))
