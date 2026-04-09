# France Facts Program
# This program demonstrates basic Python concepts:
# variables, data types, conditionals, loops, functions, lambda, and more

print("=" * 50)
print("Welcome to the France Facts App!")
print("=" * 50)

# ----------------------------
# 1. VARIABLES AND DATA TYPES
# ----------------------------
country = "France"          # string
capital = "Paris"           # string
population_millions = 68    # int
area_km2 = 551695           # int
famous_for = ["croissants", "Eiffel Tower", "art", "cheese", "wine"]   # list

print("\nBasic info:")
print("Country:", country)
print("Capital:", capital)
print("Population (millions):", population_millions)
print("Area in km²:", area_km2)
print("Famous for:", famous_for)

# Dictionary with facts
facts = {
    "capital": "Paris is the capital of France.",
    "language": "The official language of France is French.",
    "landmark": "The Eiffel Tower is one of the most famous landmarks in the world.",
    "food": "France is famous for croissants, cheese, and baguettes.",
    "art": "The Louvre Museum in Paris is one of the largest museums in the world.",
    "coffee": "French Press is the popular way to create a coffee"
}

# ----------------------------
# 2. FUNCTION
# ----------------------------
def show_fact(topic):
    """Return a fact about France if the topic exists."""
    if topic in facts:
        return facts[topic]
    elif topic == "no_idea":
        return "Excuse me, I do not have idea for this."
    else:
        return "Sorry, I do not have a fact for that topic."

print("\nOne fact using a function:")
print(show_fact("no_idea"))

# ----------------------------
# 3. CONDITIONALS
# ----------------------------
print("\nConditional example:")
if population_millions > 60:
    print("France has a large population.")
else:
    print("France has a smaller population.")

# ----------------------------
# 4. FOR LOOP
# ----------------------------
print("\nThings France is famous for:")
for item in famous_for:
    print("-", item)

# ----------------------------
# 5. RANGE WITH FOR LOOP
# ----------------------------


quick_facts = [
    "Paris is known as the City of Light.",
    "France is one of the most visited countries in the world.",
    "French cuisine is famous worldwide."
]
facts_range = len(quick_facts)-2
print(f"\nTop {facts_range} quick France fact(s):")

for i in range(facts_range):
    print(i + 1, quick_facts[i])

# ----------------------------
# 6. WHILE LOOP
# ----------------------------
print("\nCountdown to visiting Paris:")
count = 14
while count > 0:
    print(count)
    count -= 1
print("Bon voyage!")

# ----------------------------
# 7. BREAK AND CONTINUE
# ----------------------------
print("\nLoop with continue and break:")
numbers = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13]

for number in numbers:
    if number % 2 == 0:
        continue   # skip even numbers
    if number > 10:
        break      # stop if number is greater than 5
    print("Interesting odd number:", number)

# ----------------------------
# 8. DEFAULT ARGUMENT
# ----------------------------
def greet_visitor(name="Student"):
    print(f"\nHello, {name}! Let's learn about France.")

greet_visitor()
greet_visitor("Anna")

# ----------------------------
# 9. RETURN VALUE
# ----------------------------
def count_famous_things(items):
    return len(items)

total = count_famous_things(famous_for)
print("\nNumber of famous things in the list:", total)

# ----------------------------
# 10. LAMBDA FUNCTION
# ----------------------------
word_length = lambda word: len(word)
sumOfNumbers = lambda a, b: a + b

print("Sum of numbers:", sumOfNumbers(5, 7))

print("\nLambda example:")
print("Length of 'Paris' =", word_length("Paris"))

# ----------------------------
# 11. *args EXAMPLE
# ----------------------------
def print_topics(*args):
    print("\nTopics you asked about:")
    for topic in args:
        print("-", topic)

print_topics("capital", "food", "art")

# ----------------------------
# 12. FINAL MINI QUIZ
# ----------------------------
def guess_capital(answer):
    if answer.lower() == "paris":
        return "Correct! Paris is the capital of France."
    else:
        return "Not quite. The correct answer is Paris."

print("\nMini quiz:")
user_answer = "Riga"   # change this value to test
print(guess_capital(user_answer))

print("\nProgram finished. Merci!")