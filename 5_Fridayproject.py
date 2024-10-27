import random

# Define functions for changing text color
def redText(text):
    return f"\033[91m{text}\033[0m"  # ANSI code for red

def blueText(text):
    return f"\033[94m{text}\033[0m"  # ANSI code for blue

def greenText(text):
    return f"\033[92m{text}\033[0m"  # ANSI code for green

def yellowText(text):
    return f"\033[93m{text}\033[0m"  # ANSI code for yellow

def purpleText(text):
    return f"\033[95m{text}\033[0m"  # ANSI code for purple

# Optional: Define a function that applies a random color
def randomColor(text):
    color_functions = [redText, blueText, greenText, yellowText, purpleText]
    return random.choice(color_functions)(text)

# Main program logic
def main():
    print("Welcome to the Text Color Changer!")
    colors = {
        "red": redText,
        "blue": blueText,
        "green": greenText,
        "yellow": yellowText,
        "purple": purpleText,
        "random": randomColor
    }
    
    # Loop to continue allowing the user to color text
    while True:
        # Prompt user to select a color
        chosen_color = input("\nChoose a color (red, blue, green, yellow, purple, or random): ").strip().lower()
        
        # Check if the chosen color is valid
        if chosen_color in colors:
            # Get the text input from the user
            text = input("Enter the text you want to color: ")
            # Print the text in the chosen color
            print(colors[chosen_color](text))
        else:
            print("Invalid color choice. Please try again.")
        
        # Ask if the user wants to continue
        continue_choice = input("Do you want to color another text? (yes or no): ").strip().lower()
        if continue_choice != "yes":
            break
    
    # Farewell message
    print("Thanks for using the Text Color Changer! Goodbye.")

# Run the main program
main()