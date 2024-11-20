from random import sample, randint
import requests
import unicodedata

API_KEY = 'a9cad816-711c-42fa-a522-8354d46b2919'
API_URL = 'https://www.dictionaryapi.com/api/v3/references/spanish/json/'



class Question:
    def __init__(self, response, question_iteration, quiz_type):
        try:
            self.quiz_type = quiz_type
            definition = response[question_iteration-1]
            self.word = definition['hwi']['hw']
            self.word_type = definition['fl']
            self.answers = definition['shortdef']
            self.answers = [self.remove_accents(answer) for answer in self.answers]
            self.status = 'success'
        except Exception:
            self.status = 'failed'

    def ask(self):
        given_answer = input(f'Type a spanish translation for the {self.word_type} "{self.word}": ')
        correct = False
        for i,answer in enumerate(self.answers):
            if given_answer in answer and given_answer != '':
                correct = True
                break
        if correct:
            print(f'Correct! valid translations for the {self.word_type} "{self.word}" include:')
        else:
            print(f'Incorrect! valid translations for the {self.word_type} "{self.word}" include:')
        for answer in self.answers:
            print(f'- {answer}')

        if self.quiz_type == 'normal':
            save = input('Enter "s" to save to notes or anything else to continue: ')
            if save.lower() == 's':
                self.save_to_notes()


    def remove_accents(self, input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return ''.join(char for char in nfkd_form if not unicodedata.combining(char))

    def save_to_notes(self):
        with open('notes/saved_translations.txt','a') as f:
            f.write(f'{self.word_type}: {self.word}\n')
            for answer in self.answers:
                f.write(f'    - {answer}\n')
            f.write('-----------------------------------------------------------------------\n')
        with open('data/notes_word_bank.txt','a') as f:
            f.write(f'{self.word}\n')


class VocabQuiz:
    def __init__(self, num_questions):
        try:
            self.quiz_type
        except Exception:
            self.quiz_type = 'normal'
        self.import_words(num_questions)
        self.get_responses(self.words)
        self.questions = []
        for response in self.responses:
            response_questions = []
            question_iteration = 1
            question = Question(response, question_iteration, self.quiz_type)
            while question.status == 'success':
                response_questions.append(question)
                question_iteration += 1
                question = Question(response, question_iteration, self.quiz_type)
            self.questions.append(response_questions)

    def quiz(self):
        for response_questions in self.questions:
            next_definition = True if (len(response_questions) > 0) else False
            iteration = 1
            while next_definition:
                next_definition = self.ask_question(response_questions, iteration)
                iteration += 1

    def ask_question(self, response_questions, iteration):
            current_question = response_questions[iteration-1]
            current_question.ask()
            if len(response_questions) > iteration:
                next_iteration = input(f'Quiz yourself on another dictionary entry for {current_question.word} y/n ')
                if next_iteration.lower() == 'y':
                    return True
            return False

    def import_words(self, num_words):
        with open('data/word_bank.txt', 'r') as f:
            words = f.read().splitlines()
        self.words = sample(words, num_words)

    def get_responses(self, words):
        self.responses = []
        for word in words:
            response = requests.get(f'{API_URL}{word}\?key={API_KEY}')

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                self.responses.append(response.json())
            else:
                print(f"Error: Word:{word} Received status code {response.status_code}")

class NotesVocabQuiz(VocabQuiz):
    def __init__(self, num_questions):
        self.quiz_type = 'notes'
        super().__init__(num_questions)

    def import_words(self, num_words):
        with open('data/notes_word_bank.txt', 'r') as f:
            words = f.read().splitlines()
        if num_words > len(words):
            raise IOError('Given quiz size is larger than the number of words in notes')
        self.words = sample(words, num_words)


