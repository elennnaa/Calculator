# main.py
from flask import Flask, render_template, request
from dataclasses import dataclass
from functools import reduce

app = Flask(__name__)


# A1G: Eigenschaften von Funktionen beschreiben
# Hier wird der funktionale Ansatz mit einer dataclass verwendet, was eine Möglichkeit ist, immutable Werte zu erstellen.
@dataclass(frozen=True)
class CalculationInput:
    x: float
    y: float


def add(input_data):
    return input_data.x + input_data.y


def subtract(input_data):
    return input_data.x - input_data.y


def multiply(input_data):
    return input_data.x * input_data.y


def divide(input_data):
    if input_data.y != 0:
        return input_data.x / input_data.y
    else:
        return "Error: Division by zero"


OPERATIONS = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}


# Prozeduraler Ansatz
def add_procedural(x, y):
    result = x + y
    print(f"The result is: {result}")


# Objektorientierter Ansatz
class Calculator:
    def add(self, x, y):
        result = x + y
        print(f"The result is: {result}")


# B1G: Algorithmus erklären
# Die Funktionen add, subtract, multiply und divide implementieren verschiedene mathematische Operationen.
# Auch die calculate-Funktion setzt einen Algorithmus um, je nach ausgewählter Operation.

# B2G: Funktionen als Objekte behandeln
# Hier wird die apply_operation-Funktion verwendet, um eine Funktion als Argument zu übergeben und auszuführen.

# B3G: Einfache Lambda-Ausdrücke schreiben
square = lambda x: x ** 2
uppercase = lambda s: s.upper()


# B4G: Map, Filter und Reduce
# Hier werden map, filter und reduce verwendet, um verschiedene Aufgaben auf der Liste 'numbers' auszuführen.

# C1G: Refactoring-Techniken
# Der Refactoring-Teil zeigt, wie der Code verbessert wurde, indem Funktionen in einem Dictionary organisiert wurden.

# B1F: Algorithmen in funktionale Teilstücke aufteilen
# Die verschiedenen Funktionen (add, subtract, multiply, divide) sind in funktionale Teile aufgeteilt.

# B2F: Funktionen als Argumente verwenden
# Die calculate-Funktion verwendet eine Funktion (operation_func) als Argument.

# B3F: Lambda-Ausdrücke mit mehreren Argumenten
# Hier sind keine Lambda-Ausdrücke mit mehreren Argumenten, aber die calculate-Funktion akzeptiert mehrere Argumente.

# B4F: Map, Filter und Reduce kombiniert verwenden
# Die Kombination von map, filter und reduce wird in Bezug auf die Liste 'numbers' gezeigt.

# C1F: Refactoring-Techniken
# Der Refactoring-Teil zeigt, wie der Code lesbarer gemacht wurde.

# A1F: Konzept von immutable values
# Der funktionale Ansatz verwendet dataclasses, die immutable sind.

# A1E: Probleme in verschiedenen Konzepten lösen und vergleichen
# Die verschiedenen Berechnungsansätze (funktional, prozedural, objektorientiert) werden im Code verglichen.

# B2E: Funktionen als Objekte und Argumente verwenden, um komplexe Aufgaben
# Die apply_operation-Funktion zeigt, wie Funktionen als Argumente verwendet werden können.

# B3E: Lambda-Ausdrücke verwenden, um den Programmfluss zu steuern
# Die Lambda-Ausdrücke square und uppercase werden verwendet, um den Programmfluss zu steuern.

# B4E: Map, Filter und Reduce verwenden
# Hier werden map, filter und reduce verwendet, um komplexe Datenverarbeitungsaufgaben zu lösen.

# C1E: Auswirkungen des Refactorings auf das Verhalten des Codes einschätzen
# Der Refactoring-Teil zeigt, wie der Code verbessert wurde, und es wird darauf geachtet, dass das Verhalten des Codes nicht unerwünscht verändert wird.

# Berechnungsfunktion
def calculate(operation, x, y):
    operation_func = OPERATIONS.get(operation)

    if operation_func:
        input_data = CalculationInput(x, y)
        result = operation_func(input_data)
        return result
    else:
        return "Error: Invalid operation"


# Funktion, um eine Operation auf zwei Zahlen anzuwenden
def apply_operation(operation_func, x, y):
    return operation_func(x, y)


# Lambda-Ausdrücke und Map/Filter/Reduce
numbers = [1, 2, 3, 4, 5]

# Map: Quadrieren aller Zahlen
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Filter: Filtern der geraden Zahlen
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Reduce: Summieren aller Zahlen
sum_all = reduce(lambda x, y: x + y, numbers)


# C1E: Vor und nach dem Refactoring
# Vor dem Refactoring
def calculate_before_refactoring(operation, x, y):
    if operation == 'add':
        return add(x, y)
    elif operation == 'subtract':
        return subtract(x, y)
    elif operation == 'multiply':
        return multiply(x, y)
    elif operation == 'divide':
        return divide(x, y)
    else:
        return "Error: Invalid operation"


# Nach dem Refactoring
def calculate_after_refactoring(operation, x, y):
    operation_func = OPERATIONS.get(operation)

    if operation_func:
        input_data = CalculationInput(x, y)
        result = operation_func(input_data)
        return result
    else:
        return "Error: Invalid operation"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate_route():
    operation = request.form['operation']
    x = float(request.form['x'])
    y = float(request.form['y'])

    result = calculate(operation, x, y)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
