class FranceFacts:
    def __init__(self):
        # Variables and data types
        self.country = "France"
        self.capital = "Paris"
        self.population_millions = 68
        self.area_km2 = 551695
        self.famous_for = ["croissants", "Eiffel Tower", "art", "cheese", "wine"]

        self.facts = {
            "capital": "Paris is the capital of France.",
            "language": "The official language of France is French.",
            "landmark": "The Eiffel Tower is one of the most famous landmarks in the world.",
            "food": "France is famous for croissants, cheese, and baguettes.",
            "art": "The Louvre Museum in Paris is one of the largest museums in the world.",
            "coffee": "French Press is the popular way to create a coffee"
        }

        self.quick_facts = [
            "Paris is known as the City of Light.",
            "France is one of the most visited countries in the world.",
            "French cuisine is famous worldwide."
        ]

        self.numbers = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13]

    def show_welcome(self):
        print("=" * 50)
        print("Welcome to the France Facts App!")
        print("=" * 50)

    def show_basic_info(self):
        print("\nBasic info:")
        print("Country:", self.country)
        print("Capital:", self.capital)
        print("Population (millions):", self.population_millions)
        print("Area in km²:", self.area_km2)
        print("Famous for:", self.famous_for)

    def show_fact(self, topic):
        if topic in self.facts:
            return self.facts[topic]
        elif topic == "no_idea":
            return "Excuse me, I do not have idea for this."
        else:
            return "Sorry, I do not have a fact for that topic."

    def check_population(self):
        print("\nConditional example:")
        if self.population_millions > 60:
            print("France has a large population.")
        else:
            print("France has a smaller population.")

    def show_famous_things(self):
        print("\nThings France is famous for:")
        for item in self.famous_for:
            print("-", item)

    def show_quick_facts(self):
        facts_range = len(self.quick_facts) - 2
        print(f"\nTop {facts_range} quick France fact(s):")

        for i in range(facts_range):
            print(i + 1, self.quick_facts[i])

    def countdown_to_paris(self):
        print("\nCountdown to visiting Paris:")
        count = 14
        while count > 0:
            print(count)
            count -= 1
        print("Bon voyage!")

    def loop_example(self):
        print("\nLoop with continue and break:")
        for number in self.numbers:
            if number % 2 == 0:
                continue
            if number > 10:
                break
            print("Interesting odd number:", number)

    def greet_visitor(self, name="Student"):
        print(f"\nHello, {name}! Let's learn about France.")

    def count_famous_things(self):
        return len(self.famous_for)

    def lambda_examples(self):
        word_length = lambda word: len(word)
        sum_of_numbers = lambda a, b: a + b

        print("\nLambda example:")
        print("Sum of numbers:", sum_of_numbers(5, 7))
        print("Length of 'Paris' =", word_length("Paris"))

    def print_topics(self, *args):
        print("\nTopics you asked about:")
        for topic in args:
            print("-", topic)

    def guess_capital(self, answer):
        if answer.lower() == "paris":
            return "Correct! Paris is the capital of France."
        else:
            return "Not quite. The correct answer is Paris."

    def run(self):
        self.show_welcome()
        self.show_basic_info()

        print("\nOne fact using a function:")
        print(self.show_fact("no_idea"))

        self.check_population()
        self.show_famous_things()
        self.show_quick_facts()
        self.countdown_to_paris()
        self.loop_example()

        self.greet_visitor()
        self.greet_visitor("Anna")

        total = self.count_famous_things()
        print("\nNumber of famous things in the list:", total)

        self.lambda_examples()

        self.print_topics("capital", "food", "art")

        print("\nMini quiz:")
        user_answer = "Riga"   # change this value to test
        print(self.guess_capital(user_answer))

        print("\nProgram finished. Merci!")


# Create object and run program
app = FranceFacts()
app.run()