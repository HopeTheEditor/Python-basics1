import unittest
from assessment import (
    create_profile_greeting,
    calculate_total_score,
    analyze_score_status,
    generate_study_reminders,
    analyze_feedback_text
)


class TestTask1(unittest.TestCase):
    """Test cases for Task 1: Create Profile Greeting"""

    def test_basic_greeting(self):
        self.assertEqual(create_profile_greeting("John", "Doe"), "Welcome, Doe, John!")

    def test_different_names(self):
        self.assertEqual(create_profile_greeting("Alice", "Smith"), "Welcome, Smith, Alice!")

    def test_single_letter_names(self):
        self.assertEqual(create_profile_greeting("A", "B"), "Welcome, B, A!")


class TestTask2(unittest.TestCase):
    """Test cases for Task 2: Calculate Total Score"""

    def test_mixed_scores(self):
        self.assertEqual(calculate_total_score([8, -2, 10, -5, 4]), 22)

    def test_all_positive_scores(self):
        self.assertEqual(calculate_total_score([10, 20, 30]), 60)

    def test_all_negative_scores(self):
        self.assertEqual(calculate_total_score([-3, -1, -12]), 0)

    def test_with_zero(self):
        self.assertEqual(calculate_total_score([10, 0, 5, -5]), 15)

    def test_empty_list(self):
        self.assertEqual(calculate_total_score([]), 0)


class TestTask3(unittest.TestCase):
    """Test cases for Task 3: Analyze Score Status"""

    def test_high_and_even(self):
        self.assertEqual(analyze_score_status(90), "High and Even")

    def test_high_and_odd(self):
        self.assertEqual(analyze_score_status(75), "High and Odd")

    def test_negative_score(self):
        self.assertEqual(analyze_score_status(-15), "Negative Score")

    def test_zero_score(self):
        self.assertEqual(analyze_score_status(0), "Zero")
    
    def test_large_positive_odd(self):
        self.assertEqual(analyze_score_status(999), "High and Odd")


class TestTask4(unittest.TestCase):
    """Test cases for Task 4: Generate Study Reminders"""

    def test_basic_case(self):
        self.assertEqual(generate_study_reminders(1, 20, 5), [5, 10, 15, 20])

    def test_different_interval(self):
        self.assertEqual(generate_study_reminders(10, 30, 4), [12, 16, 20, 24, 28])
    
    def test_start_is_a_multiple(self):
        self.assertEqual(generate_study_reminders(10, 25, 5), [10, 15, 20, 25])

    def test_no_multiples_in_range(self):
        self.assertEqual(generate_study_reminders(1, 3, 4), [])

    def test_end_is_not_a_multiple(self):
        self.assertEqual(generate_study_reminders(1, 19, 5), [5, 10, 15])


class TestTask5(unittest.TestCase):
    """Test cases for Task 5: Analyze Feedback Text"""

    def test_with_punctuation_and_space(self):
        self.assertEqual(analyze_feedback_text("Great course!"), {'vowels': 4, 'consonants': 6})

    def test_with_numbers_and_mixed_case(self):
        self.assertEqual(analyze_feedback_text("Module 3 was fun."), {'vowels': 5, 'consonants': 7})

    def test_empty_string(self):
        self.assertEqual(analyze_feedback_text(""), {'vowels': 0, 'consonants': 0})

    def test_no_vowels(self):
        self.assertEqual(analyze_feedback_text("Rhythm fly gyps!"), {'vowels': 0, 'consonants': 11})

    def test_no_consonants(self):
        self.assertEqual(analyze_feedback_text("AeIoUaeiou"), {'vowels': 10, 'consonants': 0})

    def test_only_symbols_and_numbers(self):
        self.assertEqual(analyze_feedback_text("123-456!@#$%^"), {'vowels': 0, 'consonants': 0})


if __name__ == "__main__":
    unittest.main(verbosity=2)