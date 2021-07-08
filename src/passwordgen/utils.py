from random import randint, choice
import itertools
import csv

from passwordgen import forms


def str_to_bool(string: str = 'False') -> bool:
    """
    util function for smart conversion from str to bool,
    returns bool conversion result,
    returns False if not given params
    raises Valuerror when string cant be converted
    """

    true_values = ['true', 'True', '1', 'on', 'yes']
    false_values = ['false', 'False', '0', 'off', 'no']

    if string in true_values or string == True:
        return True
    elif string in false_values or string == False:
        return False
    else:
        raise ValueError(f"'{string}' is ambigious")


class PasswordGen:
    def __init__(self, path_to_word_list, more_symbols: bool = False) -> None:
        self.path_to_word_list = path_to_word_list
        self.symbols = ('!', '$', '#', '@')

        # this software is meant to create password that are easy to remeber,
        # therfore less/easier to remeber symbols are recommended
        if more_symbols:
            self.symbols = ('!', '$', '#', '&', '@', '?', '%',
                            '^', ':', '{', '}', '+', '~', '=')

        self.traits = None

    def set_password_traits(self, words: int = 3, symbols: bool = True) -> None:
        """
        input kwargs of traits password should have,
        return dict of traits
        """

        try:
            self.traits = {'words': words, 'symbols': symbols}
            self.is_valid_traits(self.traits)

        except Exception as e:
            raise e

    def is_valid_traits(self, traits: dict) -> bool:
        """
        check if given traits are valid,
        return bool: True if every check passed
        raise TypeError
        """

        # set a limit on amount of words, in case it's set to a very large number,
        max_words = 20

        try:
            if isinstance(traits['words'], int) == False:
                raise TypeError(
                    f"'Words' must be an int, not {type(traits['words'])}")

            if isinstance(traits['symbols'], bool) == False:
                raise TypeError(
                    f"'Symbols' must be a bool, not {type(traits['symbols'])}")

            if traits['words'] > max_words or traits['words'] <= 0:
                raise ValueError(
                    f"'Words' must be positive and not more than {max_words}, not {traits['words']}")

        except Exception as e:
            raise e

        return True

    def generate_password(self, traits: dict) -> str:
        """
        generate a password with given traits,
        traits parameter must be valid,
        return password: str
        """

        password = ''

        word_list = self.generate_word_list_csv(
            self.path_to_word_list, traits['words'])

        #checking whether word list was generated correctly
        assert(len(word_list) == traits['words'])

        if traits['symbols'] == True:
            for word in word_list:
                password += f"{word}{choice(self.symbols)}"
            #cut the last character, otherwise the symbol will be at the end
            password = password[:-1]
        else:
            password = ' '.join(word_list)

        return password

    def generate_word_list_csv(self, csv_path: str, num_of_words: int) -> list:
        """
        function that automates the process of gathering words for password generation
        return list
        """

        csv_len = self.get_length_csv(csv_path)

        # generate random word_indexes times num_of_words,
        # that correspond to literal values in a csv file
        word_indexes = [randint(0, csv_len-1) for x in range(num_of_words)]

        rv = self.get_words_from_csv(csv_path, word_indexes)
        return rv

    def get_length_csv(self, csv_path: str) -> int:
        """
        return int: amout of rows in a csv file
        """

        with open(csv_path, 'r') as f:
            return sum(1 for row in csv.reader(f))

    def get_words_from_csv(self, csv_path: str, word_indexes: list) -> list:
        """
        get words with specific indexes from csv word list,
        this func doesn't load the entire csv into memory,
        however the csv reader will start over for each word index given,
        note that indexes must be in valid range,
        return list
        """

        words = []

        for index in word_indexes:
            with open(csv_path, 'r') as f:
                word = next(itertools.islice(csv.reader(f), index, None))
                #the next method above generates a list like ['word', ''], so only the first value is needed
                words.append(word[0])

        return words

    def get_password(self) -> str:
        """
        master function,
        core functionality is implemented here, 
        return str: password
        """

        if self.traits == None:
            raise Exception("Password traits must be set beforehand")

        return self.generate_password(self.traits)


# if __name__ == '__main__':
#     gen = PasswordGen(
#         path_to_word_list='path')

#     gen.set_password_traits(words=4, symbols=True)
#     print(gen.get_password())

