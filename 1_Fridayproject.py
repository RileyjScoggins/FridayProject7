def get_user_inputs():
    inputs = {
        "large_object": input("Enter a large object (singular): "),
        "large_objects_plural": input("Enter large objects (plural): "),
        "adjective": input("Enter an adjective: "),
        "body_part": input("Enter a body part: "),
        "restaurant": input("Enter a restaurant: "),
        "first_food": input("Enter a food: "),
        "second_food": input("Enter another food: "),
    }
    return inputs

# Function to create the story using the user's inputs
def create_story(inputs):
    story = f"""
    I’ve had a very {inputs['adjective']} day.
    This morning, I dropped a box of {inputs['large_objects_plural']} on my {inputs['body_part']}.
    Then, at lunch, I went to {inputs['restaurant']} for their delicious {inputs['first_food']},
    But the waiter brought me {inputs['second_food']}, which I was not hungry for.
    Finally, on my way home, I was cut off by a van with a large {inputs['large_object']} strapped to the roof.
    """
    return story

# Main function to run the Mad Lib
def mad_lib_game(): 
    print("Welcome to the Mad Lib game!")
    user_inputs = get_user_inputs()
    story = create_story(user_inputs)
    print("\nHere is your Mad Lib story:")
    print(story)

# Run the game
mad_lib_game()
