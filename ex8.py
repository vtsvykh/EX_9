class MorseMsg:
    def __init__(self, encoded_msg):
        self.encoded_msg = encoded_msg
        self.morse_code = {
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
        decoded_msg = ""
        words = self.encoded_msg.split(' ')
        for word in words:
            for letter, code in self.morse_code.items():
                if code == word:
                    decoded_msg += letter
                    break
        return decoded_msg

    def ru_decode(self):
        decoded_msg = ""
        words = self.encoded_msg.split(' ')
        for word in words:
            for letter, code in self.morse_rus.items():
                if code == word:
                    decoded_msg += letter
                    break
        return decoded_msg

    def get_vowels(self, lang):
        vowels = ""
        if lang == 'eng':
            vowels_eng = "AEIOU"
            for word in self.encoded_msg.split(' '):
                for letter, code in self.morse_code.items():
                    if code == word and letter in vowels_eng:
                        vowels += letter
                        break
        elif lang == 'ru':
            vowels_rus = "АЕЁИОУЫЭЮЯ"
            for word in self.encoded_msg.split(' '):
                for letter, code in self.morse_rus.items():
                    if code == word and letter in vowels_rus:
                        vowels += letter
                        break
        return vowels

    def get_consonants(self, lang):
        consonants = ""
        if lang == 'eng':
            for word in self.encoded_msg.split(' '):
                for letter, code in self.morse_code.items():
                    if code == word and letter not in "AEIOU":
                        consonants += letter
                        break
        elif lang == 'ru':
            consonants_rus = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ"
            for word in self.encoded_msg.split(' '):
                for letter, code in self.morse_rus.items():
                    if code == word and letter in consonants_rus:
                        consonants += letter
                        break
        return consonants


