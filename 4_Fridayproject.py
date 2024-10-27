# Define a dictionary with questions as keys and answers as values
trivia_questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the largest planet in our solar system?": "Jupiter",
    "What element does 'O' represent on the periodic table?": "Oxygen",
    "In which year did World War II end?": "1945"
}

# Greeting message
print("Welcome to the Trivia Study Program! Let's test your knowledge.")

# Loop through each question in the dictionary
for question, correct_answer in trivia_questions.items():
    # Display the question to the user
    print("\n" + question)
    
    # Get user's answer
    user_answer = input("Your answer: ").strip()
    
    # Check if the user's answer is correct
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

# Farewell message
print("\nThanks for studying! Good luck on your test!")