# Glossary

## Core Language Concepts & Data Model

### Everything is an Object
In Python, **first-class objects** are fundamental: **everything is an object**, including numbers, strings, functions, classes, and modules.

* Every object in memory has three core properties:
  1. **Identity (`id()`):** The object's memory address.
  2. **Type (`type()`):** What kind of data structure it is.
  3. **Value:** The actual data held within the object.

```python
x = 42

print(type(x))  # <class 'int'>
print(id(x))    # Memory address integer (e.g., 140725283921872)

# Functions are objects too—they can be assigned to variables or passed to other functions:
def greet():
    return "Hi"

my_func = greet
print(my_func())  # Returns "Hi"
```

### Variables in Python
In Python, variables are **labels (pointers) attached to objects in memory**, not "boxes" that hold values directly.

* **Declaration:** Created the moment you assign a value using `=`.
* **Reassignment:** Assigning a new value changes what object the variable points to; it does not overwrite the old object in memory.

```python
x = [1, 2, 3]  # x points to a list object in memory
y = x          # y now points to the EXACT same list object
```

### Constants in Python
A **constant** is a variable whose value is intended to remain unchanged throughout the lifecycle of a program.

* **No Language Enforcement:** Unlike languages like C++ (`const`) or Java (`final`), Python does not have built-in runtime enforcement for constants. Variables declared as constants can technically still be reassigned.
* **Convention-Based:** Constants are designated entirely by convention using `SCREAMING_SNAKE_CASE` to signal to other developers that the value should not be modified.
* **Type Guard Enforcement:** Tools like `mypy` can enforce immutability statically using the `Final` type hint from the `typing` module.

```python
from typing import Final

# Convention only:
DATABASE_PORT = 5432

# Enforced by static type checkers (mypy will throw an error if reassigned):
MAX_CONNECTIONS: Final[int] = 100
```

### Functions, Calls, and Parameters
In Python, functions are first-class objects defined using the `def` keyword.

* **Function Call:** Executing a function by appending parentheses `()` to its name, passing any required arguments.
* **Parameters vs. Arguments:**
  * **Parameters:** The variables declared in the function's definition signature.
  * **Arguments:** The actual values passed into the function when it is called.
* **Positional vs. Keyword Arguments:** Arguments can be passed by position or explicitly named (`key=value`).

```python
def greet(name, greeting="Hello"):  # 'name' and 'greeting' are parameters
    return f"{greeting}, {name}!"

# 'Alice' is a positional argument; 'greeting' is a keyword argument
greet("Alice", greeting="Hi")  # Function call
```

### The `None` Object
`None` is a built-in constant in Python used to represent the **absence of a value** or a null state.

* **Singleton:** `None` is the sole instance of the `NoneType` class.
* **Default Returns:** Functions that do not explicitly execute a `return` statement return `None` by default.
* **Identity Check:** Always test for `None` using the `is` or `is not` identity operators, not equality (`==`).

```python
result = print("Hello")
if result is None:
    print("print() returns None by default")
```

### Modules
A **module** is simply a Python file (`.py`) containing runnable code, function definitions, and classes meant to be reused across different program files.

* **Importing:** Modules are loaded using the `import` statement.
* **Namespace Protection:** Importing a module creates its own separate namespace, preventing variable name collisions.

```python
import math

print(math.sqrt(16))  # Accesses sqrt from the math module namespace
```

---

## Type Systems & Typing Paradigms

### Dynamic vs. Static Typing
> **Core Question:** *WHEN is the type checked?*

#### Dynamic Typing (e.g., Python, JavaScript)
Types are checked **at runtime** (while the code is running). Variables do not have fixed types—they are just labels pointing to values in memory. A variable can easily hold an integer and later be reassigned to a string.

```python
x = 10       # x points to an integer
x = "hello"  # Allowed! x now points to a string
```

#### Static Typing (e.g., C++, Java, Rust)
Types are checked **at compile time** (before the code runs). You must explicitly declare a variable's type when you create it, and that variable can never hold a different data type.

```cpp
int x = 10;   // Explicitly defined as an integer
x = "hello";  // ERROR: Compiler stops you before the code can run
```

### Strong vs. Weak Typing
> **Core Question:** *HOW STRICT is the language when mixing different types?*

#### Strong Typing (e.g., Python, Java)
The language **refuses to implicitly convert types**. It will crash with an error rather than guessing what you intended. You must perform explicit type conversions.

```python
"5" + 2  # ERROR: TypeError

# Must explicitly convert:
int("5") + 2  # Returns 7
```

#### Weak Typing (e.g., JavaScript, C, Perl)
The language tries to be "helpful" by **implicitly coercing (guessing) types** behind the scenes when operations involve mixed types.

```javascript
"5" + 2  // Returns "52" (Silently converts 2 to a string)
"5" - 2  // Returns 3    (Silently converts "5" to a number)
```

### Duck Typing vs. Nominal Typing

#### Duck Typing (Python's Philosophy)
Python operates on the principle: *"If it walks like a duck and quacks like a duck, it's a duck."* 

Python doesn't check an object's actual class or type—it only checks if the object has the required **methods or behaviors** (attributes) when called. If an object supports the operation, Python allows it.

```python
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm pretending to be a duck!"

def make_it_quack(duck_like_object):
    # Doesn't care if it's a Duck or Person class, as long as it has .quack()
    print(duck_like_object.quack())

make_it_quack(Duck())    # Works
make_it_quack(Person())  # Works
```

#### Nominal Typing (The Opposite)
In **Nominal (Name-based) Typing** (e.g., Java, C++), the language cares strictly about the **explicit name of the class or interface**, not just its methods. Even if an object has the exact same methods, it is rejected unless it explicitly inherits from or implements the required type.

```java
// Java Example of Nominal Typing
class Person {
    public String quack() { return "I'm pretending!"; }
}

// This function strictly requires an object explicitly declared as a "Duck"
public void makeItQuack(Duck d) { 
    System.out.println(d.quack()); 
}

// makeItQuack(new Person()); 
// ERROR! Even though Person has a quack() method, it is not explicitly a Duck.
```

### Gradual Typing vs. Pure Typing

#### Gradual Typing (The Hybrid)
Gradual typing allows a language to combine **dynamic** and **static** typing behaviors. You can leave most code dynamic, but selectively add static type assertions (Type Hints) where safety or clarity is needed.

* Python is dynamic by default, but supports gradual typing via **type hints**.
* The standard Python interpreter (`CPython`) completely ignores these hints at runtime, but external tools (like IDEs or `mypy`) can analyze them statically to catch bugs before execution.

#### Pure Static & Pure Dynamic Typing (The Opposites)
* **Strict Static Typing (e.g., Haskell, Java, C++):** You *must* define a type for everything, or the compiler will deduce it strictly before execution. There is no option to opt out.
* **Pure Dynamic Typing (e.g., Python 2, Ruby, early JavaScript):** There is *no* static type checking system built-in at all. Types are strictly resolved while the program is actively running.

---

## Python Style & Syntax Conventions

### PEP 8 & PEP 257 Guidelines

#### PEP 8 – Python's Style Guide for Code
**PEP (Python Enhancement Proposal) 8** is the official style guide for writing readable Python code.

* **Indentation:** Use **4 spaces** per indentation level (never tabs).
* **Line Length:** Limit lines to a maximum of **79 characters**.
* **Imports:** Put imports at the top of the file, on separate lines (`import os`, not `import os, sys`). Group them in order:
  1. Standard library imports
  2. Third-party imports
  3. Local application/library imports
* **Whitespace:** Avoid unnecessary whitespace around brackets, commas, or colons.

#### PEP 257 – Docstring Conventions
**PEP 257** defines the standards for writing **docstrings** (documentation strings placed directly inside modules, classes, functions, or methods).

* **One-Line Docstrings:** Used for simple functions. Must fit on one line with triple quotes (`"""`).
  ```python
  def add(a: int, b: int) -> int:
      """Return the sum of two integers."""
      return a + b
  ```
* **Multi-line Docstrings:** Consist of a summary line, a blank line, and an expanded description.
  ```python
  def calculate_average(numbers: list[float]) -> float:
      """Calculate the arithmetic mean of a list of numbers.

      Args:
          numbers: A list of integers or floats.

      Returns:
          The average of the numbers as a float.
      """
      return sum(numbers) / len(numbers)
  ```

### Naming Conventions & Case Styles

* **`snake_case` (Python standard):** Words are lowercased and separated by underscores.
  * *Used in Python for:* Variable names, function names, method names, and module/file names.
  * *Example:* `user_account_balance = 100`
* **`PascalCase` / `UpperCamelCase`:** Every word starts with a capital letter, no spaces or underscores.
  * *Used in Python for:* Class names (e.g., `class BankAccount:`).
  * *Example:* `class UserAccount:`
* **`camelCase` / `lowerCamelCase`:** First word is lowercase, subsequent words are capitalized.
  * *Used in:* JavaScript, Java, C#. Rare in standard Python.
  * *Example:* `userAccountBalance = 100`
* **`kebab-case`:** Words are lowercased and separated by hyphens.
  * *Used in:* HTML, CSS, URLs, and CLI tools (Invalid in Python syntax).
  * *Example:* `user-account-balance`
* **`SCREAMING_SNAKE_CASE`:** All uppercase with underscores.
  * *Used in Python for:* Constants (values that should not change).
  * *Example:* `MAX_LOGIN_ATTEMPTS = 5`

### Code Comments vs. Docstrings

#### Comments
Comments are written using `#` and are intended strictly for developers reading the code to explain **why** something was written a certain way, rather than *what* the code does. They are completely ignored by the interpreter.

```python
# Calculate line-item total after applying state sales tax
tax_rate = 0.075
```

#### Docstrings
Docstrings are string literals placed as the very first statement inside a module, function, class, or method. Unlike comments, docstrings are retained at runtime and attached to the object's `__doc__` attribute.

```python
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

print(add.__doc__)  # Outputs: Return the sum of two integers.
```

### Automated Testing & Documentation Tools

#### Doctest
`doctest` is a standard library module that searches docstrings for pieces of text that look like interactive Python sessions, executing those sessions to verify that the code behaves as documented.

```python
def double(x: int) -> int:
    """Return twice the input value.

    >>> double(3)
    6
    >>> double(-1)
    -2
    """
    return x * 2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

#### Sphinx
**Sphinx** is a build tool used to generate comprehensive documentation sites (HTML, PDF, ePub) for Python projects.

* It automatically extracts docstrings from codebases using the `autodoc` extension.
* Uses **reStructuredText (reST)** or Markdown (via MyST parser) as its markup format.
* Standard tool used to build official documentation for Python itself, as well as libraries like NumPy and Requests.

### Magic Numbers
A **magic number** is a direct, unexplained numerical value hardcoded directly into source code without context or named explanation.

* **The Problem:** Magic numbers reduce code readability, make future updates error-prone (if the number appears in multiple places), and obscure developer intent.
* **The Solution:** Replace magic numbers with named **constants** (`SCREAMING_SNAKE_CASE`) at the module level.

```python
# Bad (Uses a magic number):
def calculate_total(subtotal: float) -> float:
    return subtotal + (subtotal * 0.075)  # What is 0.075?

# Good (Replaced with a named constant):
SALES_TAX_RATE = 0.075

def calculate_total(subtotal: float) -> float:
    return subtotal + (subtotal * SALES_TAX_RATE)
```