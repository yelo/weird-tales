import random


class WeirdTales(object):

    def __init__(self, input_path='input.txt', ngram=3):
        self._ngram = ngram
        self._parsed_input = self._read_input(input_path)

    def _read_input(self, path):
        with open(path, encoding='utf8') as input_data:
            return self._parse_input(' '.join(input_data.read().splitlines()))

    def _parse_input(self, input_data):
        splitted = input_data.split()

        parsed = {}

        ngram = self._ngram
        for nr in range(len(splitted)):
            if ngram < len(splitted):
                combo = ' '.join(splitted[nr:ngram])
                if combo not in parsed:
                    parsed[combo] = []
                parsed[combo].append(splitted[ngram])
                ngram += 1

        return parsed

    def _get_random_start(self):
        return random.choice([x for x in list(self._parsed_input) if x[0].istitle()])

    def _get_next_word(self, chain):
        chain_splits = ' '.join(chain).split()
        chain_last = ' '.join(chain_splits[len(chain_splits) - self._ngram:])
        if chain_last in self._parsed_input.keys():
            next_word = random.choice(self._parsed_input[chain_last])
            chain.append(next_word)

    def generate_output(self, rounds):
        chain = [self._get_random_start()]

        for _ in range(rounds):
            self._get_next_word(chain)

        while chain[-1][-1] is not '.':
            self._get_next_word(chain)

        return ' '.join(chain)
