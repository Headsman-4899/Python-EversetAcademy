import string
#eng_alph = "abcdefghijklmnopqrstuvwxyz"
eng_alph = string.ascii_uppercase


class Alphabet:
    def __init__(self, language, letters):
        self.language = language
        self.letters = letters

    def print(self):
        return self.letters

    def letters_num(self):
        return len(self.letters)


class EnglishAlphabet(Alphabet):
    def __init__(self, language, letters):
        super().__init__(language, letters)

    @staticmethod
    def __letters_num():
        return 26

    def is_en_letter(self, letter):
        return letter in self.letters

    def letters_num(self):
        return len(self.letters)

    @staticmethod
    def example():
        return "Hello, World!"


ea = EnglishAlphabet("En", eng_alph)
print(ea.letters)
print(ea.letters_num())
print(ea.is_en_letter("F"))
print(ea.is_en_letter("Щ"))
print(ea.example())