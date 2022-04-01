from random import randint


class RandWriter:
    def __init__(self, text, order):
        """Creates a Markov chain using text with k_grams of size order

        Fills a dictionary with each k_gram of text, that is,
        it gets every substring of text that is order characters
        long, and it counts how many times that k_gram appears.
        Similarly, it creates a dictionary with every k_gram and keeps
        a list of every character that follows the k_gram in text.
        """

        self.text = text
        self.order = order
        self.table = {}
        self.next_char = {}
        size = len(self.text)

        try:
            assert(size > 0),\
                '__init__: Input size must be greater than 0'
            assert(size > self.order),\
                '__init__: Order must be less than size of text'
            assert(isinstance(self.text, str)),\
                '__init__: Text must be of type string'
            assert(isinstance(self.order, int)),\
                '__init__: Order must be of type int'
        except AssertionError as e:
            print(e)
            exit()
        else:
            for i in range(size):
                temp = self.text[i]

                j = 1
                for x in range(1, self.order):
                    if i + j < size:
                        temp += self.text[i + j]
                    else:
                        temp += self.text[abs(size - (i + j))]
                    j += 1

                if temp not in self.table:
                    self.table[temp] = 0

                self.table[temp] += 1
                if temp not in self.next_char:
                    self.next_char[temp] = []

                if i + j < size:
                    self.next_char[temp] += self.text[i + j]
                else:
                    self.next_char[temp] += self.text[abs(size - (i + j))]

    def k_rand(self, k_gram) -> str:
        """Returns a pseudorandom character

        A random character is chosen based on the probability that
        it follows k_gram. This is done by getting the character
        from a random index of next_char[k_gram].
        """

        try:
            assert(len(k_gram) == self.order),\
                f'k_rand: k_gram must be of length {self.order}'
            if self.order > 0:
                assert(k_gram in self.next_char),\
                    f'k_rand: k_gram \'{k_gram}\' is not in table'
        except AssertionError as e:
            print(e)
            return None
        else:
            if self.order == 0:
                return self.text[randint(0, len(self.text) - 1)]
            else:
                return self.next_char[k_gram][
                    randint(0, len(self.next_char[k_gram]) - 1)]

    def generate(self, k_gram, size) -> str:
        """Generates a pseudorandom string that is size characters long

        The string is seeded with k_gram and from there it calls k_rand
        to get a random character and the new character is appended to
        the new string, which is returned after the desired number of
        characters are generated.
        """

        try:
            assert(len(k_gram) == self.order),\
                f'generate: k_gram must be of length {self.order}'
            if self.order > 0:
                assert(k_gram in self.table),\
                    f'generate: \'{k_gram}\' not found in table'
        except AssertionError as e:
            print(e)
            return None

        result = k_gram
        for i in range(size - len(k_gram)):
            temp = result[len(result) - self.order:]
            result += self.k_rand(temp)

        return result
