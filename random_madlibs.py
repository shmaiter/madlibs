from sample_madlibs import hp, code, book_review
import random

if __name__ == "__main__":
    m = random.choice([hp, code, book_review])
    m.madlib()
