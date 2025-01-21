from art import text2art, FONT_NAMES

def generate_ascii_art():
    # Liste des styles disponibles
    print("\nAvailable styles:\n")
    for i, style in enumerate(FONT_NAMES[:10], 1):  # Affiche seulement les 10 premiers styles
        print(f"{i}. {style}")

    while True:
        try:
            style_choice = int(input("\nSelect the number of the style you want to use: "))
            if 1 <= style_choice <= len(FONT_NAMES[:10]):
                selected_style = FONT_NAMES[style_choice - 1]
                break
            else:
                print("Please enter a valid number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    text = input("\nEnter your text: ")

    print("\nHere is your ASCII art:\n")
    ascii_art = text2art(text, font=selected_style)
    print(ascii_art)

if __name__ == "__main__":
    generate_ascii_art()
