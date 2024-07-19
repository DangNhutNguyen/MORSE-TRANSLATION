import pyfiglet
class colors:
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    BLUE = '\033[34m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
text = "MORSE TRANSLATION"
ascii_art = pyfiglet.figlet_format(text)
print(colors.BLUE + ascii_art + colors.END)
# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' '
}

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('')  # Handle unsupported characters
    return ' '.join(morse_code)

def print_morse_with_spaces(morse_code):
    print(morse_code)

def text_to_morse_conversion():
    text = input("Enter your text here: ")
    morse_code = text_to_morse(text)
    print_morse_with_spaces(morse_code)

def morse_to_text_conversion():
    # Reverse Morse code dictionary
    REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

    def morse_to_text(morse_code):
        words = morse_code.split('  ')  # Split by double spaces to separate words
        decoded_message = []
        for word in words:
            letters = word.split(' ')  # Split by single space to separate letters
            decoded_word = []
            for letter in letters:
                if letter in REVERSE_MORSE_CODE_DICT:
                    decoded_word.append(REVERSE_MORSE_CODE_DICT[letter])
                else:
                    decoded_word.append('?')  # Handle unsupported Morse code sequences
            decoded_message.append(''.join(decoded_word))
        return ' '.join(decoded_message)

    # Example usage
    morse_code = input("Enter Morse code: ")
    decoded_text = morse_to_text(morse_code)
    print(decoded_text)

def main():
    while True:
        try:
            lang = int(input("Morse to Text: 1 - Text to Morse: 2 (Enter 0 to exit): "))
            if lang == 1:
                morse_to_text_conversion()
            elif lang == 2:
                text_to_morse_conversion()
            elif lang == 0:
                break
            else:
                print("Invalid input. Please enter 1 for Morse to Text or 2 for Text to Morse.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
