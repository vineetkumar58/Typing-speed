import time
import random

def get_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is fun and rewarding.",
        "Python is a versatile programming language.",
        "Practice makes perfect.",
        "Coding challenges improve your skills.",
        "It was a good thing they were going home tomorrow.",
        "He had done one good deed.",
        "It would do no good to ask him why.",
    ]
    return random.choice(sentences)

def typing_speed_test():
    print("Welcome to the Typing Speed Test!")
    input("Press Enter when you are ready to start...")

    sentence = get_random_sentence()
    print("\nYour typing challenge:")
    print(sentence)
    
    start_time = time.time()
    user_input = input("Type the above sentence: ")
    end_time = time.time()

    if user_input == sentence:
        time_taken = end_time - start_time
        words_per_minute = (len(sentence.split()) / time_taken) * 60
        print(f"\nCongratulations! You typed the sentence correctly.")
        print(f"Time taken: {time_taken:.2f} seconds")
        print(f"Words per minute: {words_per_minute:.2f}")
    else:
        print("\nOops! You made a mistake. Try again.")

if __name__ == "__main__":
    typing_speed_test()