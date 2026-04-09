import unittest
from france_facts import FranceFacts


class TestFranceFacts(unittest.TestCase):

    def setUp(self):
        self.app = FranceFacts()

    def test_country_name(self):
        self.assertEqual(self.app.country, "France")

    def test_capital_name(self):
        self.assertEqual(self.app.capital, "Paris")

    def test_population(self):
        self.assertEqual(self.app.population_millions, 68)

    def test_show_fact_valid_topic(self):
        result = self.app.show_fact("capital")
        self.assertEqual(result, "Paris is the capital of France.")

    def test_show_fact_no_idea(self):
        result = self.app.show_fact("no_idea")
        self.assertEqual(result, "Excuse me, I do not have idea for this.")

    def test_show_fact_invalid_topic(self):
        result = self.app.show_fact("sports")
        self.assertEqual(result, "Sorry, I do not have a fact for that topic.")

    def test_count_famous_things(self):
        result = self.app.count_famous_things()
        self.assertEqual(result, 5)

    def test_guess_capital_correct(self):
        result = self.app.guess_capital("Paris")
        self.assertEqual(result, "Correct! Paris is the capital of France.")

    def test_guess_capital_correct_lowercase(self):
        result = self.app.guess_capital("paris")
        self.assertEqual(result, "Correct! Paris is the capital of France.")

    def test_guess_capital_wrong(self):
        result = self.app.guess_capital("Riga")
        self.assertEqual(result, "Not quite. The correct answer is Paris.")


if __name__ == "__main__":
    unittest.main()