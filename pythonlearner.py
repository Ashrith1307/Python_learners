import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

# ==========================
# Load credentials from env
# ==========================
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER_EMAILS = os.getenv("RECEIVER_EMAILS", "").split(",")


PYTHON_CONCEPTS = [
    {
        "title": "Hello World",
        "description": "The simplest Python program prints text to the console.",
        "example": """print("Hello, World!")"""
    },
    {
        "title": "Variables and Data Types",
        "description": "Python supports various data types like int, float, str, and bool. Variables are dynamically typed.",
        "example": """x = 10
y = 3.14
name = "Python"
is_active = True

print(type(x), type(y), type(name), type(is_active))"""
    },
    {
        "title": "Type Casting",
        "description": "Convert between data types using int(), float(), str(), etc.",
        "example": """x = "100"
y = int(x)
print(y + 50)"""
    },
    {
        "title": "Strings and Formatting",
        "description": "Strings can be manipulated using methods and f-strings for formatting.",
        "example": """name = "Alice"
print(f"Hello, {name.upper()}!")"""
    },
    {
        "title": "Arithmetic Operators",
        "description": "Python supports +, -, *, /, %, //, ** for arithmetic operations.",
        "example": """a, b = 5, 2
print(a + b, a - b, a * b, a / b, a // b, a ** b)"""
    },
    {
        "title": "Comparison and Logical Operators",
        "description": "Use ==, !=, <, >, <=, >= and logical operators and/or/not.",
        "example": """x, y = 5, 10
print(x < y and y > 0)
print(not(x == y))"""
    },
    {
        "title": "Control Flow (if, elif, else)",
        "description": "Control flow statements help execute code based on conditions.",
        "example": """age = 18
if age >= 18:
    print("You are an adult.")
elif age > 12:
    print("You are a teenager.")
else:
    print("You are a child.")"""
    },
    {
        "title": "Loops (for, while)",
        "description": "Loops help repeat a block of code multiple times.",
        "example": """# For loop
for i in range(5):
    print("Iteration:", i)

# While loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1"""
    },
    {
        "title": "Break and Continue",
        "description": "Break exits a loop, continue skips to the next iteration.",
        "example": """for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)"""
    },
    {
        "title": "Functions",
        "description": "Functions allow you to group reusable code blocks.",
        "example": """def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))"""
    },
    {
        "title": "Default and Keyword Arguments",
        "description": "Functions can have default values and be called with named arguments.",
        "example": """def power(base, exp=2):
    return base ** exp

print(power(3))
print(power(base=2, exp=5))"""
    },
    {
        "title": "Lambda Functions",
        "description": "Lambda creates small anonymous functions in one line.",
        "example": """square = lambda x: x**2
print(square(5))"""
    },
    {
        "title": "Lists",
        "description": "Lists are ordered collections of elements.",
        "example": """fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)"""
    },
    {
        "title": "List Comprehensions",
        "description": "A concise way to create lists.",
        "example": """squares = [x**2 for x in range(5)]
print(squares)"""
    },
    {
        "title": "Tuples",
        "description": "Tuples are immutable ordered collections.",
        "example": """point = (3, 4)
print(point[0])"""
    },
    {
        "title": "Dictionaries",
        "description": "Dictionaries store key-value pairs.",
        "example": """person = {"name": "Alice", "age": 25}
print(person["name"])"""
    },
    {
        "title": "Sets",
        "description": "Sets store unique unordered values.",
        "example": """nums = {1, 2, 2, 3}
print(nums)"""
    },
    {
        "title": "Exception Handling",
        "description": "Handle runtime errors using try-except.",
        "example": """try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")"""
    },
    {
        "title": "Modules and Imports",
        "description": "Use import to include built-in or external modules.",
        "example": """import math
print(math.sqrt(16))"""
    },
    {
        "title": "File Handling",
        "description": "Read and write files in Python.",
        "example": """with open("data.txt", "w") as f:
    f.write("Hello file")"""
    },
    {
        "title": "Object-Oriented Programming",
        "description": "Classes let you define objects with attributes and methods.",
        "example": """class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(self.name, "says Woof!")

d = Dog("Buddy")
d.bark()"""
    },
    {
        "title": "Inheritance",
        "description": "A class can inherit properties and methods from another class.",
        "example": """class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

Dog().sound()"""
    },
    {
        "title": "Polymorphism",
        "description": "Different classes can define methods with the same name.",
        "example": """class Cat:
    def sound(self): print("Meow")

class Dog:
    def sound(self): print("Woof")

for animal in [Cat(), Dog()]:
    animal.sound()"""
    },
    {
        "title": "Encapsulation",
        "description": "Encapsulation hides internal object details.",
        "example": """class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance

acct = BankAccount(1000)
acct.deposit(500)
print(acct.get_balance())"""
    },
    {
        "title": "Decorators",
        "description": "Functions that modify other functions.",
        "example": """def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def hello():
    print("Hello!")

hello()"""
    },
    {
        "title": "Iterators",
        "description": "Iterators define __iter__ and __next__ for iteration.",
        "example": """class Counter:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n == 0: raise StopIteration
        self.n -= 1
        return self.n

for i in Counter(3):
    print(i)"""
    },
    {
        "title": "Generators",
        "description": "Use yield to create lazy iterators.",
        "example": """def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)"""
    },
    {
        "title": "Context Managers",
        "description": "Manage resources using with statements.",
        "example": """class MyContext:
    def __enter__(self):
        print("Enter")
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit")

with MyContext():
    print("Inside block")"""
    },
    {
        "title": "Comprehensions",
        "description": "Python supports dict and set comprehensions.",
        "example": """squares = {x: x**2 for x in range(5)}
print(squares)"""
    },
    {
        "title": "Collections Module",
        "description": "Special data structures like Counter, deque, defaultdict.",
        "example": """from collections import Counter
print(Counter("banana"))"""
    },
    {
        "title": "Regular Expressions",
        "description": "Use regex to match text patterns.",
        "example": """import re
pattern = r'\\d+'
print(re.findall(pattern, "Order 123, Item 456"))"""
    },
    {
        "title": "Functional Programming (map, filter, reduce)",
        "description": "map applies functions, filter selects items, reduce aggregates.",
        "example": """from functools import reduce
nums = [1,2,3,4]
print(list(map(lambda x: x*2, nums)))
print(list(filter(lambda x: x%2==0, nums)))
print(reduce(lambda x,y: x+y, nums))"""
    },
    {
        "title": "Async Programming",
        "description": "Use asyncio for concurrent tasks.",
        "example": """import asyncio

async def task():
    await asyncio.sleep(1)
    print("Done")

asyncio.run(task())"""
    },
    {
        "title": "Multithreading",
        "description": "Run tasks in parallel using threads.",
        "example": """import threading

def work():
    print("Working...")

t = threading.Thread(target=work)
t.start()
t.join()"""
    },
    {
        "title": "Multiprocessing",
        "description": "Run code across multiple processes for CPU-bound tasks.",
        "example": """from multiprocessing import Process

def work():
    print("Process working")

p = Process(target=work)
p.start()
p.join()"""
    },
    {
        "title": "Virtual Environments",
        "description": "Isolate Python environments with venv.",
        "example": """# In terminal
python -m venv env
source env/bin/activate  # Linux/macOS
env\\Scripts\\activate   # Windows"""
    },
    {
        "title": "Unit Testing",
        "description": "Test code using unittest or pytest.",
        "example": """import unittest

def add(a, b): return a+b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)

unittest.main()"""
    },
    {
        "title": "Type Hints",
        "description": "Add type annotations for readability and static analysis.",
        "example": """def greet(name: str) -> str:
    return f"Hello, {name}" """
    },
    {
        "title": "Metaclasses",
        "description": "Control class creation with metaclasses.",
        "example": """class Meta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creating {name}")
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=Meta):
    pass"""
    }
]


# ==========================
# Pick concept of the day
# ==========================
today = datetime.date.today()
index = (today.toordinal()) % len(PYTHON_CONCEPTS)
concept = PYTHON_CONCEPTS[index]


# ==========================
# Create colorful HTML email
# ==========================
html_content = f"""
<html>
<head>
  <style>
    body {{ font-family: Arial, sans-serif; background-color: #f4f4f9; padding: 20px; }}
    .card {{
      background: white; 
      border-radius: 12px; 
      padding: 20px; 
      box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }}
    h2 {{ color: #4CAF50; }}
    pre {{
      background: #272822; 
      color: #f8f8f2; 
      padding: 10px; 
      border-radius: 8px; 
      overflow-x: auto;
    }}
    p {{ font-size: 16px; }}
  </style>
</head>
<body>
  <div class="card">
    <h2>📘 Python Concept of the Day: {concept['title']}</h2>
    <p>{concept['description']}</p>
    <h3>💡 Example:</h3>
    <pre>{concept['example']}</pre>
    <p style="font-size:14px; color:gray;">Happy Learning! 🚀</p>
  </div>
</body>
</html>
"""

# ==========================
# Send Email
# ==========================
msg = MIMEMultipart("alternative")
msg["From"] = SENDER_EMAIL
msg["To"] = ", ".join(RECEIVER_EMAILS)
msg["Subject"] = f"🐍 Python Concept of the Day - {concept['title']}"

msg.attach(MIMEText(html_content, "html"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER_EMAIL, EMAIL_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAILS, msg.as_string())
    server.quit()
    print(f"✅ Email sent: {concept['title']}")
except Exception as e:
    print(f"❌ Error: {e}")
