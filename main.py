from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time
from constants import DRIVER_PATH, BUTTONS

with open('words.txt', 'r') as f:
    lines = f.readlines()
all_words = []
for line in lines:
    all_words.append(line.strip())

possible_words = all_words.copy()


def remove_dup_let_words(my_list):
    temp_list = []
    for word in my_list:
        letter_list = []
        for let in range(5):
            if word[let] in letter_list:
                break
            else:
                letter_list.append(word[let])
        if len(letter_list) == 5:
            temp_list.append(word)
    return temp_list


impossible_words = remove_dup_let_words(all_words)  # get more info without dupes

safe_letters = []

scores = {'e': 1.23, 'a': 0.975, 'r': 0.897, 'o': 0.753, 't': 0.729, 'l': 0.716, 'i': 0.67, 's': 0.668, 'n': 0.573,
          'c': 0.475, 'u': 0.466, 'y': 0.424, 'd': 0.393, 'h': 0.387, 'p': 0.365, 'm': 0.316, 'g': 0.31, 'b': 0.28,
          'f': 0.229, 'k': 0.21, 'w': 0.194, 'v': 0.152, 'z': 0.04, 'x': 0.037, 'q': 0.029, 'j': 0.027}
# result from letter_frequency.py

s = Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=s)
driver.get('https://www.nytimes.com/games/wordle/index.html')

guess = 'trace'  # first guess


def wait_popup_close():
    is_true = True
    while is_true:
        try:
            temp = driver.find_element(By.XPATH, BUTTONS['BACK'])
            temp.click()
            is_true = False
        except ElementClickInterceptedException:
            time.sleep(1)


def guess_word(word):
    for let in word:
        let = let.upper()
        button = driver.find_element(By.XPATH, BUTTONS[let])
        button.click()
    button = driver.find_element(By.XPATH, BUTTONS['ENTER'])
    button.click()


def get_green_letters(row):
    green_letters = []
    for col in range(1, 6):
        cell = driver.find_element(By.XPATH, f'//*[@id="wordle-app-game"]/div[1]/div/div[{row}]/div[{col}]/div')
        if cell.get_attribute('data-state') == 'correct':
            green_letters.append(col - 1)
    return green_letters


def get_yellow_letters(row):
    yellow_letters = []
    for col in range(1, 6):
        cell = driver.find_element(By.XPATH, f'//*[@id="wordle-app-game"]/div[1]/div/div[{row}]/div[{col}]/div')
        if cell.get_attribute('data-state') == 'present':
            yellow_letters.append(col - 1)
    return yellow_letters


def get_grey_letters(row):
    grey_letters = []
    for col in range(1, 6):
        cell = driver.find_element(By.XPATH, f'//*[@id="wordle-app-game"]/div[1]/div/div[{row}]/div[{col}]/div')
        if cell.get_attribute('data-state') == 'absent':
            grey_letters.append(col - 1)
    return grey_letters


def get_new_possible_words(row):
    green_letters = get_green_letters(row)
    yellow_letters = get_yellow_letters(row)
    grey_letters = get_grey_letters(row)

    new_possible_words = []

    length = len(possible_words)
    for word_index in range(length):
        skip_outer = False
        test_word = possible_words[word_index]

        for index in green_letters:
            if guess[index] not in safe_letters:
                safe_letters.append(guess[index])
            if guess[index] != test_word[index]:
                skip_outer = True
                break
        if skip_outer is True:
            continue

        for index in yellow_letters:
            if guess[index] not in safe_letters:
                safe_letters.append(guess[index])
            if guess[index] not in test_word:
                skip_outer = True
                break
        if skip_outer is True:
            continue

        for index in grey_letters:
            if guess[index] in safe_letters:  # word has duplicate letters, one green and one gray
                continue
            elif guess[index] in test_word:
                skip_outer = True
                break
        if skip_outer is True:
            continue

        new_possible_words.append(test_word)

    if guess in new_possible_words:
        new_possible_words.remove(guess)  # word is 'power', guess is 'repro'

    return new_possible_words


def get_new_impossible_words():
    new_impossible_words = impossible_words.copy()

    for word in impossible_words:
        for i in range(5):
            if guess[i] in word:
                new_impossible_words.remove(word)
                break

    return new_impossible_words


def get_info_word(words):
    high_score = 0
    for word in words:
        score = 0
        for i in range(5):
            let = word[i]
            score += scores[let]
        if score > high_score:
            high_score = score
            best_word = word
    return best_word


def get_new_word(row):
    if len(possible_words) <= 6 - row:
        return get_info_word(possible_words)
        # return possible_words[0]
    else:
        try:
            return get_info_word(impossible_words)
        except UnboundLocalError:
            return get_info_word(possible_words)
            # return possible_words[0]


def is_complete(row):
    word = get_green_letters(row)
    if len(word) == 5:
        return True
    else:
        return False


def exit_game():
    input('Enter any key to exit: ')
    driver.quit()
    print('COMPLETE')
    raise SystemExit


wait_popup_close()  # must close popup manually

print()
print(f'First guess: {guess}')
print()

for attempt in range(1, 7):
    guess_word(guess)
    time.sleep(2)

    if is_complete(attempt):
        print(f'{guess} was correct')
        exit_game()

    possible_words = get_new_possible_words(attempt)
    impossible_words = get_new_impossible_words()
    print(f'AFTER ATTEMPT {attempt}')
    print(f'Possible words:\n\t {possible_words}')
    print(f'Test words:\n\t {impossible_words}')
    print(f'Safe letters:\n\t {safe_letters}')
    guess = get_new_word(attempt)
    print(f'Next guess: {guess}')
    print()

print(f'Remaining possible words: {possible_words}')
exit_game()

