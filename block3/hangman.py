import random


def check_win(secret_word, old_letters_guessed):
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    current_status = ""
    for char in secret_word:
        if char in old_letters_guessed:
            current_status += char + " "
        else:
            current_status += '_'
    return current_status


def check_valid_input(letter_guessed, old_letters_guessed):
    return len(letter_guessed) == 1 and letter_guessed.lower() not in old_letters_guessed and letter_guessed.isalpha()


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print("X")
    print("Previously Guessed Letters:", old_letters_guessed)
    return False

def remove_life(guess, word):
    return guess not in word


def choose_word(file_path, index):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
        target_index = (index - 1) % len(words)
        return words[target_index].lower()


def count_lines(file_path):
    try:
        with open(file_path, 'r') as f:
            return sum(1 for line in f)
    except FileNotFoundError:
        print("File is not found. Try again!")


def welcome_screen():
    logo = r"""
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/    
                                            
    """
    print(logo)


def winners_screen(secret_word):
    victory_banner = r"""
 __     __          __          ___       _ 
 \ \   / /          \ \        / (_)     | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| |
    | | (_) | |_| |    \  /\  /  | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)
    """

    print(victory_banner)
    print("--------------------------------------------------")
    print(f"Congratulations! You successfully guessed the word: {secret_word}")
    print("You survived!")
    print("--------------------------------------------------")


def losers_screen(secret_word):
    game_over_banner = r"""
   _____          __  __  ______    ____  _    _  ______  _____ 
  / ____|   /\   |  \/  ||  ____|  / __ \| |  | ||  ____||  __ \
 | |  __   /  \  | \  / || |__    | |  | | |  | || |__   | |__) |
 | | |_ | / /\ \ | |\/| ||  __|   | |  | | |  | ||  __|  |  _  / 
 | |__| |/ ____ \| |  | || |____  | |__| |\ \/ / | |____ | | \ \ 
  \_____/_/    \_\_|  |_||______|  \____/  \__/  |______||_|  \_\
    """

    print(game_over_banner)
    print("--------------------------------------------------")
    print(f"Oh no! The hangman was fully drawn.")
    print(f"The secret word you were looking for was: {secret_word}")
    print("Better luck next time!")
    print("--------------------------------------------------")


def start_engine(word, guess_remaining, hangman_options):
    old_letters_guessed = []
    while guess_remaining > 0:
        guess = input(f"Guesses Remaining {guess_remaining}\nEnter your guess: ")
        if try_update_letter_guessed(guess, old_letters_guessed):
            if remove_life(guess, word):
                guess_remaining -= 1
        if check_win(word, old_letters_guessed):
            winners_screen(word)
            return
        print(show_hidden_word(word, old_letters_guessed))
        print(f"Letters guessed so far: {old_letters_guessed}")
        print(hangman_options[6-guess_remaining])
    losers_screen(word)
    return


def start_game(hangman_options):
    guess_remaining = 6
    #file_path = input("Enter file path: ")
    file_path = "hangman_words.txt"
    total_lines = count_lines(file_path)
    word_index = random.randint(0, total_lines)
    word = choose_word(file_path, word_index)
    start_engine(word, guess_remaining, hangman_options)


def main():
    welcome_screen()
    print("Rules: \nYou have 6 lives to figure out the word. A guess that is not included in the word kills a life.\nPlease enter the word in lower case format. \nYou can't pick number or any special characters.\nGood Luck!\n")
    hangman_options = {
        0: r"""
        x-------x
        """,

        1: r"""
        x-------x
        |
        |
        |
        |
        |
        """,

        2: r"""
        x-------x
        |       |
        |       0
        |
        |
        |
        """,

        3: r"""
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """,

        4: r"""
        x-------x
        |       |
        |       0
        |      /|\
        |
        |
        """,

        5: r"""
        x-------x
        |       |
        |       0
        |      /|\
        |      /
        |
        """,

        6: r"""
        x-------x
        |       |
        |       0
        |      /|\
        |      / \
        |
        """
    }
    start_game(hangman_options)


if __name__ == '__main__':
    main()

