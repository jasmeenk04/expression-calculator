# 🧮 Expression Calculator

A Python-based calculator that parses and evaluates mathematical expressions using infix-to-postfix conversion and a binary expression tree.

## 🚀 Features

- Supports standard arithmetic operations: `+`, `-`, `*`, `/`, `^`
- Converts infix expressions (e.g., `3 + 5 * 2`) to postfix notation
- Constructs a binary expression tree to evaluate expressions
- Handles parentheses and decimal numbers
- Simple command-line interface

## 📁 Project Structure

```
expression-calculator/
├── calculator.py     # Main CLI program
├── tree.py           # Expression tree with evaluation logic
└── stack.py          # Custom stack class used for parsing
```

## 🧠 Technologies Used

- Python 3
- Custom data structures (Stack, Binary Tree)
- Recursion and algorithmic parsing

## ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/jasmeenk04/expression-calculator.git
   cd expression-calculator
   ```

2. Run the calculator:
   ```bash
   python3 calculator.py
   ```

3. Example usage:
   ```
   Please enter your expression here. To quit enter 'quit' or 'q':
   (5 + 2) * 3
   21.0
   ```

## 📝 Sample Expressions

| Input             | Output |
|------------------|--------|
| `3 + 4 * 2`       | 11.0   |
| `(1 + 2) * (3+4)` | 21.0   |
| `3 + 4 * 2 / (1 - 5)^2` | 3.5 |

## 👩‍💻 Author

**Jasmeen Kaur**  
[LinkedIn](https://www.linkedin.com/in/jasmeenkaur101)
