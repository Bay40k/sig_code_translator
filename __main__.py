from .sig_code_translator import convert_to_english_from_sig
from .sig_code_translator import convert_to_sig_from_english


def main():
    user_input = input("1. [To English], 2. To Sig: ")
    if user_input.strip() == "2":
        user_input = input("Enter instructions: ")
        print(convert_to_sig_from_english(user_input))
    else:
        user_input = input("Enter pharmacy sig: ")
        print(convert_to_english_from_sig(user_input))
    print()


if __name__ == "__main__":
    while True:
        main()
