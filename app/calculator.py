"""
Advanced Calculator
A extensible calculator with support for basic operations, functions, and expression parsing
"""

import re
import math
from typing import Union, Callable, Dict
from dataclasses import dataclass


# Simple calculator functions for basic operations
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a"""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@dataclass
class CalculatorError(Exception):
    """Custom exception for calculator errors"""
    message: str


class Calculator:
    """
    Advanced calculator with operator precedence and function support.
    
    Think of this like a game engine - the core handles the rules (math operations),
    while you can mod it by adding new functions and operators.
    """
    
    def __init__(self):
        # Operator precedence (higher = evaluated first)
        self.operators = {
            '+': {'precedence': 1, 'func': lambda a, b: a + b},
            '-': {'precedence': 1, 'func': lambda a, b: a - b},
            '*': {'precedence': 2, 'func': lambda a, b: a * b},
            '/': {'precedence': 2, 'func': lambda a, b: a / b},
            '^': {'precedence': 3, 'func': lambda a, b: a ** b},
            '%': {'precedence': 2, 'func': lambda a, b: a % b},
        }
        
        # Built-in functions (easy to extend)
        self.functions: Dict[str, Callable] = {
            'sqrt': math.sqrt,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log10,
            'ln': math.log,
            'abs': abs,
            'round': round,
        }
        
        # Constants
        self.constants = {
            'pi': math.pi,
            'e': math.e,
        }
        
        # Variable storage (for future extensions)
        self.variables: Dict[str, float] = {}
    
    def tokenize(self, expression: str) -> list:
        """
        Break expression into tokens (numbers, operators, functions, parentheses).
        
        Why separate tokenizing? Same reason you prep ingredients before cooking—
        it makes the actual work cleaner and easier to debug.
        """
        # Remove whitespace
        expression = expression.replace(' ', '')
        
        # Token pattern: numbers, operators, functions, parens
        pattern = r'(\d+\.?\d*|[+\-*/%^()]|[a-zA-Z]+)'
        tokens = re.findall(pattern, expression)
        
        if not tokens:
            raise CalculatorError("Empty expression")
        
        return tokens
    
    def shunting_yard(self, tokens: list) -> list:
        """
        Convert infix notation (2 + 3) to postfix/RPN (2 3 +).
        
        Why? Postfix notation is easier to evaluate without parentheses.
        """
        # Implementation would go here
        pass
