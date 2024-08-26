import requests
from english_words import get_english_words_set
WORD_SIZE = 5

def get_random(guess):
    url = "https://wordle.votee.dev:8000/random"
    params = {
        "guess":guess,
        "seed":1237
    }
    response = requests.get(url,params=params)
    result = response.json()
    return result

def result_analyze(response): #analyzing response from random API to filter un-matched words
    correct_letter = [''] * WORD_SIZE
    present_letter = {} #use letter as a key and assign position of letter into value
    absent_letter = set() #to prevent duplication, use set.

    for content in response:
        slot = content["slot"]
        guess = content["guess"]
        result = content["result"]
        if result == "correct":
            correct_letter[slot] = guess
        elif result == "present":
            if guess not in present_letter:
                present_letter[guess] = []
            present_letter[guess].append(slot)
        else:#absent
            absent_letter.add(guess)

    return correct_letter,present_letter,absent_letter

def load_word(): #load word list
    words = get_english_words_set(['web2'], lower=True)
    word_list = []
    for word in words:
        if len(word) == WORD_SIZE:
            word_list.append(word)
    return word_list

def filterring_word(mwords,correct_letter,present_letter,absent_letter): #removed unmatched words from the word list
    filtered_word=[]
    for word in mwords:
        valid = True
        for pos,letter in enumerate(word):
            #check correct_letter
            if correct_letter[pos] and word[pos] != correct_letter[pos]:
                valid = False
                break

            #check absent_letter
            if letter in absent_letter:
                valid = False
                break

        #check prsent_letter
        for letter,slots in present_letter.items():
            if letter not in word: #if present letter not in the word
                valid = False
                break
            if any(word[i] == letter for i in slots): #if word contain present word at same position as previous
                valid = False
                break
        if valid:
            filtered_word.append(word)
    return filtered_word

def guess_word():
    word_list = load_word()
    attempts = 0

    while True:
        guess = word_list[0] #use just first word in the list
        print(f"attempts {attempts+1}, Guessing: '{guess}'")
        response = get_random(guess)
        correct_letter,present_letter,absent_letter = result_analyze(response)
        
        if all(correct_letter):
            print(f"The answer is '{guess}' in {attempts+1} attempts!")
            break

        word_list = filterring_word(word_list,correct_letter,present_letter,absent_letter)
        
        #print(f"ATTEMPT {attempts+1}")
        #print(f"correct: {correct_letter}")
        #print(f"prsent: {present_letter}")
        #print(f"absent: {absent_letter}")
        attempts += 1
        if not word_list:
            print("No words left to guess...")
            break
guess_word()