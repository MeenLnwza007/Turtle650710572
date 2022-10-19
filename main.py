"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

for c in ['salmon', 'purple', 'blue', 'turquoise', 'pink', 'lightgreen', 'lavender']:
    t.color(c)
    t.forward(90)
    t.left(180)