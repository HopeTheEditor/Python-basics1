def create_profile_greeting(first_name, last_name):
    """
    Task 1: Create Profile Greeting
    For the student's profile page, create a function that takes their first and last name
    and returns a formatted welcome message. The format should be: "Welcome, Last, First!"
    
    Example: create_profile_greeting("John", "Doe") should return "Welcome, Doe, John!"
    """
    pass


def calculate_total_score(scores):
    """
    Task 2: Calculate Total Score
    A student's scores are stored in a list, which may contain positive points for correct
    answers and negative points for penalties. Write a function that calculates the sum of only
    the positive scores. If the list of scores is empty, the function should return 0.
    
    Example: calculate_total_score([8, -2, 10, -5, 4]) should return 22
    Example: calculate_total_score([-3, -1, -12]) should return 0
    """
    pass


def analyze_score_status(score):
    """
    Task 3: Analyze Score Status
    To give students quick feedback, write a function that takes an integer 'score' and
    returns a string category for it.
    - "High and Even" if the score is positive and even.
    - "High and Odd" if the score is positive and odd.
    - "Negative Score" if the score is negative.
    - "Zero" if the score is zero.
    
    Example: analyze_score_status(90) should return "High and Even"
    Example: analyze_score_status(-15) should return "Negative Score"
    Example: analyze_score_status(0) should return "Zero"
    """
    pass


def generate_study_reminders(start_day, end_day, interval):
    """
    Task 4: Generate Study Reminders
    To help students plan, create a function that generates a list of days for them to study.
    The function should return a list of reminder days based on a given 'interval'
    within a range from 'start_day' to 'end_day' (inclusive).
    
    Example: generate_study_reminders(1, 20, 5) should return [5, 10, 15, 20]
    Example: generate_study_reminders(10, 30, 4) should return [12, 16, 20, 24, 28]
    """
    pass


def analyze_feedback_text(feedback):
    """
    Task 5: Analyze Feedback Text
    To analyze a student's written feedback, write a function that takes a string 'feedback'
    and returns a dictionary counting the vowels and consonants.
    The analysis should be case-insensitive and ignore spaces, numbers, and punctuation.
    Vowels are 'a', 'e', 'i', 'o', 'u'.
    
    Example: analyze_feedback_text("Great course!") should return {'vowels': 4, 'consonants': 6}
    Example: analyze_feedback_text("Module 3 was fun.") should return {'vowels': 5, 'consonants': 7}
    """
    pass