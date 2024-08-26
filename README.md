# votee Wordle
## Introduction

This python script is an automated slover for a wordle-like game using an API provided by Votee.
The scipt simulates guessing a random word by analying response from each guess and filtering down possible word candidates until the correct word is found.

## Requirements
- **Python 3.x**
- **'requests' library** : To interact with the votee API
- **'english_words library** : For load a list of English words.

## Installation
1. clone the repository:
    '''bash
    git clone https://github.com/HK-JUN/votee.git
    cd wordle
    '''
2. install the required ptython packages:
    '''bash
    pip install requests english-words
    '''
## Usage
run the script by executing:
    '''bash
    python wordle.py

