from src.main import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Quiz yourself on some Spanish")
    parser.add_argument("quiz_type", help="normal or notes")
    parser.add_argument("num_questions", help="The number of questions you want in your quiz")
    args = parser.parse_args()
    if args.quiz_type == "normal" and args.num_questions.isdigit():
        VocabQuiz(int(args.num_questions)).quiz()
    elif args.quiz_type == "notes" and args.num_questions.isdigit():
        NotesVocabQuiz(int(args.num_questions)).quiz()
    else:
        print("Please enter valid options for quiz type and number of questions")
