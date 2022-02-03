from .sig_code_translator import from_sig
from .sig_code_translator import to_sig


def main():
    user_input = input("1. [To English], 2. To Sig: ")
    if user_input.strip() == "2":
        user_input = input("Enter instructions: ")
        print(to_sig(user_input))
    else:
        user_input = input("Enter pharmacy sig: ")
        print(from_sig(user_input))
    print()


if __name__ == "__main__":
    print("Sig Code Translator")
    print("(square brackets denote default option)")
    while True:
        main()
