import random

def powerball_number_generator():
    # Greeting message
    print("Welcome to the PowerBall Number Generator! Let's pick your lucky numbers.")
    
    # Generate five numbers for the white balls (1-69)
    white_balls = [random.randint(1, 69) for _ in range(5)]
    
    # Generate one number for the red ball (1-26)
    red_ball = random.randint(1, 26)
    
    # Formatting the output with spaces: one space between white balls, three spaces before the red ball
    numbers_output = " ".join(map(str, white_balls)) + "   " + str(red_ball)
    
    # Print the generated numbers
    print(f"Your PowerBall numbers are: {numbers_output}")
    
    # Farewell message
    print("Good luck! Hope these numbers are winners!")

# Run the PowerBall number generator
powerball_number_generator()