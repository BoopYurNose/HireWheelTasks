'''Challenge Overview
Score a multiple-choice quiz from an answer key and user answers.

Prompt for the answer key as a comma-separated list (A/B/C/D).
Prompt for the user's answers in the same format.
Compare answers position-by-position and count correct responses.
Output the score as a count and percent; handle mismatched lengths gracefully.'''

def PromptUser():
    print("Welcome to the Quiz Scorekeeper, please input the following:")

    