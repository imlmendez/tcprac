#!/bin/python3

"""Methods to obtain the jedi combination."""

import sys


class LudusDeck():
    '''Deck'''

    def __init__(self):
        self.deck = []

    def read_file(self, file):
        """Init deck from a text file"""
        _file = open(file, "r")
        for line in _file.readlines():
            parsed_line = line.split()
            self.deck.append((parsed_line[0], int(parsed_line[1])))

    def read_from_input(self):
        """Init deck from a stdin"""
        deck = []
        print("Introdueix cartes (tipus, valor). Per finalitzar Control+D")
        inp = sys.stdin.readlines()
        for line in inp:
            parse = line.split()
            self.deck.append((parse[0], int(parse[1])))

        print("------------------------------------------------------------------")
        return deck


class Strategy():
    """Strategy """

    def __init__(self):
        self.combination = []

    def combo(self, deck, last_increase):
        '''combo'''
        raise NotImplementedError()

    def patch_out(self):
        '''Method to run to stdout with the right format'''
        for card in self.combination:
            print(card[0], card[1])


class RecursiveStrategy(Strategy):
    """Recursive function immplementation"""

    def inner_combo(self, deck, cur_seq, cur_i, result):

        """Recursive combo"""
        if len(deck) == cur_i:
            result.append(cur_seq)
            return result

        next_i = cur_i + 1
        if len(cur_seq) == 0 or deck[cur_i][1] > cur_seq[-1][1]:
            temp = cur_seq.copy()
            temp1 = cur_seq.copy()
            temp.append(deck[cur_i])
            return self.inner_combo(deck, temp, next_i, result) + self.inner_combo(deck, temp1, next_i, result)

        return self.inner_combo(deck, cur_seq.copy(), next_i, result)

    def combo(self, deck, last_increase=0):
        cur_seq = []

        result = self.inner_combo(deck, cur_seq, 0, [])

        max_seq = []
        for i in result:
            if len(i) > len(max_seq):
                max_seq = i
        return max_seq


class IterativeStrategy(Strategy):
    """Iterative function implementation"""

    def combo(self, deck, last_increase=0):
        num_apariciones = []
        i = 0
        while i < len(deck):
            num_apariciones.append(0)
            i = i + 1

        for indice_externo in range(len(deck) - 2, -1, -1):
            for indice_interno in range(len(deck) - 1, indice_externo, -1):
                if deck[indice_externo][1] < deck[indice_interno][1] and num_apariciones[indice_externo] <= num_apariciones[indice_interno]:
                    num_apariciones[indice_externo] += 1  # or use m[x] = m[y] + 1

        max_value = num_apariciones[0]
        for i in num_apariciones:
            if max_value < i:
                max_value = i

        result = []
        for i in range(len(num_apariciones)):
            if max_value == num_apariciones[i]:
                result.append(deck[i])
                max_value -= 1

        return result


if __name__ == '__main__':

    DECK = LudusDeck()
    if len(sys.argv) == 1:
        sys.exit()
    elif len(sys.argv) == 2:
        DECK.read_from_input()
    else:
        DECK.read_file(sys.argv[2])

    S = Strategy()

    if sys.argv[1] == 'r':
        S = RecursiveStrategy()
    elif sys.argv[1] == 'i':
        S = IterativeStrategy()
    else:
        sys.exit()

    S.combination = S.combo(DECK.deck)
    S.patch_out()
