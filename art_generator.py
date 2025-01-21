from art import text2art

def generate_ascii_art():
    print("Welcome to the ASCII Art Generator!")
    text = input("Enter your text: ")
    print("\nHere is your ASCII art:\n")
    ascii_art = text2art(text)
    print(ascii_art)

if __name__ == "__main__":
    generate_ascii_art()
