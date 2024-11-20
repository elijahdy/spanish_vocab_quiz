## Set-up
- install python 3.10.12 (any python3 version should do, but it was developed on 3.10.12)
- clone repository `git clone https://github.com/elijahdy/spanish_vocab_quiz`
- open project directory in terminal (`spanish_vocab_quiz/`)
- run command `pip install -r requirements.txt`

## Quiz yourself
- open a terminal and change directory (`cd`) to `spanish_vocab/vocab_quiz/`
- To do a normal quiz with random words run: 
  - `python spanish_quiz.py normal <desired_number_of_questions>`
- Once you have saved some translations to notes you can also do a quiz with only words from your notes by running: 
  - `python spanish_quiz.py notes <desired_number_of_questions>`