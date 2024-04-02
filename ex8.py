class MorseMsg:
    """
    Class of decode Morse

    Attributes:
        encoded_msg: encoded message
        morse_eng: English dictionary of Morse
        morse_ru: Russian dictionary of Morse
    """

    def __init__(self, encoded_msg):
        """
        The function sets attributes for an instance of a class.
        :param encoded_msg: encoded message
        """
        self.encoded_msg = encoded_msg
        self.morse_eng = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..'
        }
        self.morse_rus = {
            "А": ".-", "Б": "-...", "В": ".--", "Г": "--.", "Д": "-..", "Е": ".", "Ё": ".",
            "Ж": "...-", "З": "--..", "И": "..", "Й": ".---", "К": "-.-", "Л": ".-..", "М": "--",
            "Н": "-.", "О": "---", "П": ".--.", "Р": ".-.", "С": "...", "Т": "-", "У": "..-",
            "Ф": "..-.", "Х": "....", "Ц": "-.-.", "Ч": "---.", "Ш": "----", "Щ": "--.-", "Ъ": "--.--",
            "Ы": "-.--", "Ь": "-..-", "Э": "..-..", "Ю": "..--", "Я": ".-.-"
        }

    def eng_decode(self):
        """
        The function decrypts the message in English.
        :return: the decrypted message in English
        """
        decoded_msg = ""

        words = self.encoded_msg.split()
        for word in words:
            for letter, code in self.morse_eng.items():
                if word == code:
                    decoded_msg += letter

        return decoded_msg

    def ru_decode(self):
        """
        The function decrypts the message in Russian.
        :return: the decrypted message in Russian
        """
        decoded_msg = ""

        words = self.encoded_msg.split()
        for word in words:
            for letter, code in self.morse_rus.items():
                if word == code:
                    decoded_msg += letter

        return decoded_msg

    def get_vowels(self, lang):
        """
        The function creates a list of vowel letters in the message in the order they follow.
        :param lang: language
        :return: list of vowel letters in the message
        """
        vowels = ""

        if lang == 'eng':
            vowels_eng = "AEIOU"
            for word in self.encoded_msg.split():
                for letter, code in self.morse_eng.items():
                    if word == code and letter in vowels_eng:
                        vowels += letter

        elif lang == 'ru':
            vowels_rus = "АЕЁИОУЫЭЮЯ"
            for word in self.encoded_msg.split():
                for letter, code in self.morse_rus.items():
                    if code == word and letter in vowels_rus:
                        vowels += letter

        return vowels

    def get_consonants(self, lang):
        """
        The function creates a list of consonant letters in the message in the order they follow
        :param lang: language
        :return: the list of consonant letters in the message
        """
        consonants = ""

        if lang == 'eng':
            for word in self.encoded_msg.split():
                for letter, code in self.morse_eng.items():
                    if code == word and letter not in "AEIOU":
                        consonants += letter

        elif lang == 'ru':
            for word in self.encoded_msg.split():
                for letter, code in self.morse_rus.items():
                    if code == word and letter not in 'АЕЁИОУЫЭЮЯ':
                        consonants += letter

        return consonants

    def __str__(self):
        """
        Outputs a string in a readable format.
        """
        return f'Сообщение для перевода: {self.encoded_msg}'

    def __repr__(self):
        """
        Creates a string representation of an object.
        """
        return self.__str__()
