## Pre-requisites
- python 3.10.12 (any python3 version should do, but it was developed on 3.10.12)

## Set-up
- open terminal/powershell
- clone repository `git clone https://github.com/elijahdy/spanish_vocab_quiz`
- change directory to this project `cd <filepath_to_project>/spanish_vocab_quiz/`
- run command `pip install -r requirements.txt`

## Quiz yourself
- open a terminal/powershell
- change directory to this project `cd <filepath_to_project>/spanish_vocab_quiz/`
- To do a normal quiz with random words run: 
  - `python spanish_quiz.py normal <desired_number_of_questions>`
- Once you have saved some translations to notes you can also do a quiz with only words from your notes by running: 
  - `python spanish_quiz.py notes <desired_number_of_questions>`

## Study notes
- when you save questions to notes they can be found in `notes/saved_translations.txt` to study whenever you want

## Manually add words to your notes-quiz selection
If there's specific words you want to show up in your notes quiz, you can open `data/notes_word_bank.txt` 
and add enter any words you want on a their own line in the file
*MAKE SURE YOU LEAVE A NEW LINE AFTER THE LAST WORD IN THE FILE*