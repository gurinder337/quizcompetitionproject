import random

# Define questions and answers (modify as needed)
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": 1,  # Index of the correct answer in options
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mars", "Jupiter", "Venus", "Earth"],
        "answer": 1,
    },
    {
        "question": "What is the world's longest river?", "options": ["Nile", "Amazon", "Yangtze", "Mississippi"], "answer": 0
    },
    {
        "question": "What is the name of the world wide web inventor?",
        "options": ["Tim Berners-Lee", "Mark Zuckerberg", "Bill Gates", "Larry Page"],
        "answer": 0,
    },
    {
        "question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Cu", "Fe"], "answer": 0
    },
    {
        "question": "What is the tallest building in the world?",
        "options": ["Burj Khalifa", "Shanghai Tower",", Abraj Al-Bait Clock Tower", "One World Trade Center"],
        "answer": 0
    },
    {
        "question": "What is the largest desert in the world?", "options": ["Sahara", "Gobi", "Kalahari", "Patagonia"], "answer": 0
    },
    {
        "question": "In which year did World War I begin?", "options": ["1914", "1939", "1941", "1918"], "answer": 0
    },
    {
        "question": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Perth"], "answer": 2
    },
    {
        "question": "What is the national animal of India?", "options": ["Tiger", "Lion", "Elephant", "Rhinoceros"], "answer": 0
    },
    {
        "question": "What is the currency of Japan?", "options": ["Yen", "Yuan", "Won", "Korean Won"], "answer": 0
    },
    {
        "question": "What mountain range separates Europe and Asia?", "options": ["Alps", "Himalayas", "Urals", "Carpathian"], "answer": 2
    },
    {
        "question": "What is the largest ocean on Earth?", "options": ["Pacific", "Atlantic", "Indian", "Arctic"], "answer": 0
    },
    {
        "question": "What is the biggest social media platform?", "options": ["Facebook", "Instagram", "Twitter", "YouTube"], "answer": 0
    },
    {
        "question": "What is the capital of Brazil?", "options": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"], "answer": 2
    },
]

def display_question(question):
  print(question["question"])
  for i, option in enumerate(question["options"]):
    print(f"{i+1}. {option}")

def check_answer(question, user_input):
  try:
    user_input = int(user_input) - 1  # Convert input to index (0-based)
    return 0 <= user_input < len(question["options"]) and user_input == question["answer"]
  except ValueError:
    return False  # Handle non-numeric input

def main():
  score = 0
  random.shuffle(questions)  # Shuffle question order

  for i, question in enumerate(questions):
    print(f"\nQuestion {i+1}:")
    display_question(question)
    user_input = input("Enter your answer (1, 2, 3, or 4): ")
    if check_answer(question, user_input):
      print("Correct!")
      score += 5
    else:
      print("Incorrect.")
      score -= 2

  print(f"\nYour final score is {score} out of 75.")

if __name__ == "__main__":
  main()
