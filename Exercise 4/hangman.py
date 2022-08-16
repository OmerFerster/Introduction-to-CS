##################################################
# FILE : hangman.py
# WRITER : Omer Ferster , omerferster , 206893653
# EXERCISE : intro2cse ex4 2021
# DESCRIPTION: THE HANGMAN GAME PROGRAM
##################################################

import hangman_helper


def update_word_pattern(word, pattern, letter):
    """ The function updates the game pattern according to the given letter
        if the letter fits in pattern, the hidden '_' replaced by the letter.
        param word, pattern: The secret word & The current pattern
        param letter: The guessed letter to update in the pattern """
    updated_pattern = ''
    for i in range(len(pattern)):
        if pattern[i] == '_' and word[i] == letter:
            updated_pattern += letter  # letter fits
        elif pattern[i] == '_' and word[i] != letter:
            updated_pattern += '_'  # letter doesn't fits
        elif pattern[i] != '_':
            updated_pattern += pattern[i]  # already existing letter
    return updated_pattern


def game_over(pattern, score):
    """ The function checks if the game is over or not, occurs when the
        pattern has no hidden chars left ('_') and score is positive (WIN)
        or when the score reach 0 (LOST)
        param pattern, score: The current pattern & The current score """
    if (pattern.count('_') == 0 and score > 0) or score < 1:
        return True  # game over
    return False


def choose_letter(score, letter, wrong_guess_lst,
                  already_guess_lst, secret_word, pattern):
    """ The function returns the updated score & pattern and a fitting msg.
        param score, letter: The user current score & The user input letter
        param wrong_guess_lst: The wrong guess at current game until now
        param already_guess_lst: The letters that already had been guessed
        param secret_word, pattern: The secret word & The current pattern """
    if len(letter) > 1 or not letter.isalpha() or not letter.islower():
        msg = 'Your letter is NON-VALID'  # invalid LETTER
    elif letter in already_guess_lst:
        msg = 'You already guessed this letter'
    else:
        msg = ''  # valid LETTER
        score -= 1
        if letter in secret_word:
            pattern = update_word_pattern(secret_word, pattern, letter)
            appearances = secret_word.count(letter)
            score += (appearances * (appearances + 1)) // 2  # rewarded score
            already_guess_lst.append(letter)
        else:
            wrong_guess_lst.append(letter)  # LETTER not appears in word
            already_guess_lst.append(letter)
    return score, msg, wrong_guess_lst, already_guess_lst, pattern


def choose_word(score, word, secret_word, pattern):
    """ The function returns the updated score & pattern according the user
        input word, if the word equals secret word, the game has finished
        param score, word: The current score & The user input word
        param secret_word, pattern: The secret word & The current pattern """
    msg = ''
    score -= 1
    is_over = False
    if word == secret_word:
        appearances = pattern.count('_')
        score += (appearances * (appearances + 1)) // 2  # rewarded score
        pattern = word
        is_over = True  # user ended the game by guessing the correct word
    return msg, score, pattern, is_over


def choose_hint(score, words_list, wrong_guess_lst, pattern):
    """ The function returns the updated score & A hints list that fits the
        current pattern in the game according to HINT_LENGTH in helper file
        param score, words_list: The current score & The whole words list
        param wrong_guess_lst: The wrong guesses that the user chose
        param pattern: The current pattern in the game """
    msg = ''
    score -= 1
    hints_lst = filter_words_list(words_list, pattern, wrong_guess_lst)
    if len(hints_lst) > hangman_helper.HINT_LENGTH:
        short_hint_lst = []  # there is too much hints that fits
        for i in range(hangman_helper.HINT_LENGTH):
            short_hint_lst.append(hints_lst[(i * len(hints_lst)) //
                                            hangman_helper.HINT_LENGTH])
        return score, msg, short_hint_lst  # return shorter hint list
    else:
        return score, msg, hints_lst  # return original hint list


def run_single_game(words_list, score):
    """ The function runs a single game iteration and returns the player
        score after a single occasion of the game.
        param words_list, score: The whole words list & The current score """
    secret_word = hangman_helper.get_random_word(words_list)  # extract word
    wrong_guess_lst, already_guess_lst = [], []  # initial lists as empties
    msg, pattern = '', '_' * len(secret_word)  # initial pattern and msg
    while not game_over(pattern, score):
        hangman_helper.display_state(pattern, wrong_guess_lst, score, msg)
        input_type, user_input = hangman_helper.get_input()  # extract input
        if input_type == hangman_helper.LETTER:
            score, msg, wrong_guess_lst, already_guess_lst, pattern =\
                choose_letter(score, user_input, wrong_guess_lst,
                              already_guess_lst, secret_word, pattern)
        elif input_type == hangman_helper.WORD:
            msg, score, pattern, is_over = choose_word(score, user_input,
                                                       secret_word, pattern)
            if is_over:
                break  # The user found the correct secret word
        elif input_type == hangman_helper.HINT:
            score, msg, hints_list = choose_hint(score, words_list,
                                                 wrong_guess_lst, pattern)
            hangman_helper.show_suggestions(hints_list)
    if score < 1:
        msg = 'You LOST the game, your secret word was: ' + secret_word
    elif score > 0 and pattern.count('_') == 0:
        msg = 'You WON the game'
    hangman_helper.display_state(pattern, wrong_guess_lst, score, msg)
    return score  # returns the current score of any iteration


def filter_words_list(words, pattern, wrong_guess_lst):
    """ The function returns a list with all words that fits the current
        pattern and not have any chars from wrong guesses list (HINT WORDS)
        param words, pattern: The whole words list & The current pattern
        param wrong_guess_lst: The wrong chars that had been guessed """
    hint_words = []  # The result hint words list, initial as empty
    same_len = []  # only words with same length like pattern list
    valid_chars = []  # only valid patterns words list
    for word in words:
        if len(word) == len(pattern):
            same_len.append(word)  # same length words
    for word in same_len:
        appears_wrong = False
        for char in word:
            if char in wrong_guess_lst:
                appears_wrong = True  # invalid word, appears in wrong guess
        if not appears_wrong:
            valid_chars.append(word)  # there is no wrong chars in word
    for word in valid_chars:
        same_pattern = True
        for i in range(len(word)):
            if word[i] != pattern[i] and pattern[i] != '_':
                same_pattern = False  # not the same pattern
            elif word[i] == pattern[i] and \
                    word.count(word[i]) != pattern.count(word[i]):
                same_pattern = False  # not the same pattern
        if same_pattern:
            hint_words.append(word)  # word fits exactly the pattern and guess
    return hint_words


def main():
    """ The main function that runs and control the game progress """
    words_lst = hangman_helper.load_words()  # extract words list
    user_score = run_single_game(words_lst, hangman_helper.POINTS_INITIAL)
    games_played = 1  # index for how many games has played
    while True:
        if user_score > 0:
            msg = 'Games played: ' + str(games_played) + \
                  ', current SCORE: ' + str(user_score) + ', Start a new game?'
            if hangman_helper.play_again(msg):
                games_played += 1  # user choose to play another round
                user_score = run_single_game(words_lst, user_score)
            else:
                break  # user choose to stop playing
        elif user_score < 1:
            msg = 'Games played until LOSS: ' + str(games_played) + \
                  ', Start a new game?'
            if hangman_helper.play_again(msg):
                games_played = 1  # user choose to restart the game
                user_score = run_single_game(words_lst,
                                             hangman_helper.POINTS_INITIAL)
            else:
                break  # user choose to stop playing


if __name__ == "__main__":
    main()
