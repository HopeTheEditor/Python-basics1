# Student Profile Application - Python Assessment

## Overview

This project is a Python assessment designed to test your understanding of fundamental programming concepts. You will complete a series of functions that could be used in a real-world "Student Profile" application. Each task is defined in the `assessment.py` file.

Your goal is to implement the logic for each function according to the requirements described in its docstring.

## Project Structure

*   `assessment.py`: This is the file where you will write your code. Do not change the function names or their parameters.
*   `unittest_assessment.py`: This file contains a suite of tests to help you check if your code is working correctly. Do not modify this file.

## Instructions

1.  Open the `assessment.py` file.
2.  Read the docstring for each function carefully. It explains what the function should do and provides examples.
3.  Write your implementation for each of the five functions directly below its definition.

The five required functions are:

1.  **`create_profile_greeting`**: Creates a formatted welcome message for a student.
2.  **`calculate_total_score`**: Calculates the total of only the positive scores from a list.
3.  **`analyze_score_status`**: Categorizes a given score into predefined labels.
4.  **`generate_study_reminders`**: Generates a list of reminder days based on a start day, end day, and interval.
5.  **`analyze_feedback_text`**: Counts the number of vowels and consonants in a string of feedback text.

## Running the Tests

To check your work, you can run the provided unit tests from your terminal. This will execute the tests in `unittest_assessment.py` against your code in `assessment.py`.

Navigate to the project directory in your terminal and run the following command:

```
python -m unittest unittest_assessment.py
```

For a more detailed output, you can use the verbose flag:

```
python -m unittest -v unittest_assessment.py
```

Your assignment is complete when all tests pass without any errors.