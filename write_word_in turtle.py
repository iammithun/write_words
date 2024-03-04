# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:08:33 2024

@author: iamrs
"""

import turtle

def draw_letter(turtle, letter):
    # Define the drawing patterns for each letter
    patterns = {
        'A': [(0, 0), (50, 100), (100, 0), (75, 0), (50, 50), (25, 0), (0, 0)],
        'B': [(0, 0), (0, 100), (75, 100), (100, 75), (75, 50), (100, 25), (75, 0), (0, 0)],
        'C': [(100, 0), (0, 0), (0, 100), (100, 100)],
        'D': [(0, 0), (0, 100), (75, 100), (100, 75), (100, 25), (75, 0), (0, 0)],
        'E': [(100, 0), (0, 0), (0, 50), (75, 50), (0, 50), (0, 100), (100, 100)],
        'F': [(100, 0), (0, 0), (0, 50), (75, 50), (0, 50)],
        'G': [(100, 0), (0, 0), (0, 100), (100, 100), (100, 50), (75, 50)],
        'H': [(0, 0), (0, 100), (0, 50), (100, 50), (100, 100), (100, 0)],
        'I': [(0, 0), (100, 0), (50, 0), (50, 100), (0, 100), (100, 100)],
        'J': [(100, 0), (100, 100), (0, 100), (0, 50)],
        'K': [(0, 0), (0, 100), (0, 50), (100, 100), (0, 50), (100, 0)],
        'L': [(0, 0), (0, 100), (100, 100)],
        'M': [(0, 0), (0, 100), (50, 50), (100, 100), (100, 0)],
        'N': [(0, 0), (0, 100), (100, 0), (100, 100)],
        'O': [(0, 0), (0, 100), (100, 100), (100, 0), (0, 0)],
        'P': [(0, 0), (0, 100), (100, 100), (100, 50), (0, 50)],
        'Q': [(0, 0), (0, 100), (100, 100), (100, 0), (0, 0), (50, -50)],
        'R': [(0, 0), (0, 100), (100, 100), (100, 50), (0, 50), (100, 0)],
        'S': [(0, 0), (100, 0), (100, 50), (0, 50), (0, 100), (100, 100)],
        'T': [(0, 0), (100, 0), (50, 0), (50, 100)],
        'U': [(0, 100), (0, 0), (100, 0), (100, 100)],
        'V': [(0, 100), (50, 0), (100, 100)],
        'W': [(0, 100), (0, 0), (50, 50), (100, 0), (100, 100)],
        'X': [(0, 0), (100, 100), (0, 100), (100, 0)],
        'Y': [(0, 100), (50, 50), (100, 100), (50, 50), (50, 0)],
        'Z': [(0, 0), (100, 0), (0, 100), (100, 100)]
    }
    
    # Scale factor for letter size
    scale_factor = 2
    
    # Retrieve the drawing pattern for the given letter
    pattern = patterns.get(letter.upper())
    if pattern is None:
        return
    
    # Draw the letter using Turtle graphics
    for point in pattern:
        x, y = point
        turtle.goto(x * scale_factor, y * scale_factor)

def draw_word(turtle, word):
    # Set initial position for drawing
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    
    # Draw each letter in the word
    for letter in word:
        draw_letter(turtle, letter)
        turtle.penup()
        turtle.forward(50)  # Spacing between letters
        turtle.pendown()

# Initialize turtle and screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
tim = turtle.Turtle()

# Prompt user to input a word
word = input("Enter a word: ")

# Draw the input word using Turtle graphics
draw_word(tim, word)

# Keep the window open until manually closed
turtle.done()
