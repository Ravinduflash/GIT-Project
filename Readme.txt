# Basic Calculator - Business Application Development

## Introduction
This repository contains a basic calculator application developed as part of the **Business Application Development** module. The project aims to introduce fundamental programming concepts and the basics of version control with Git. This calculator performs simple arithmetic operations and serves as a foundation for understanding essential coding practices in Python.

## Project Description
The **Basic Calculator** is a Python script that performs four primary arithmetic operations:

- **Addition**: Sum of two numbers
- **Subtraction**: Difference between two numbers
- **Multiplication**: Product of two numbers
- **Division**: Quotient when one number is divided by another (with error handling for division by zero)

This project includes:
1. **Function Definitions**: Separate functions for each arithmetic operation.
2. **Basic Console Application**: A simple console-based calculator that outputs results.
3. **Error Handling**: Handles errors, such as division by zero, gracefully.
4. **Learning Exercise**: Demonstrates basic principles of software development and version control.

## Features

The calculator provides the following functions:

- **Addition** - `add(a, b)`: Returns the sum of `a` and `b`.
- **Subtraction** - `subtract(a, b)`: Returns the result of subtracting `b` from `a`.
- **Multiplication** - `multiply(a, b)`: Returns the product of `a` and `b`.
- **Division** - `divide(a, b)`: Returns the result of dividing `a` by `b`, with error handling for division by zero to prevent runtime errors.

These functions allow users to perform arithmetic operations easily and demonstrate function usage, return values, and basic error handling.

## How to Use

1. **Clone the Repository**:
   Clone this repository to your local machine to run the calculator.
   ```bash
   git clone https://github.com/yourusername/basic-calculator.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd basic-calculator
   ```
3. **Run the Python Script**:
   Open a terminal and execute the script using a Python interpreter.
   ```bash
   python basic_calculator.py
   ```
4. **View Results**:
   The script performs sample calculations using the predefined functions and displays the results in the console.

## Code Example

Here’s a quick example of how each function in the calculator works:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Sample calculations
print("Addition:", add(10, 5))          # Output: 15
print("Subtraction:", subtract(10, 5))  # Output: 5
print("Multiplication:", multiply(10, 5))  # Output: 50
print("Division:", divide(10, 5))       # Output: 2.0
```

## Learning Objectives

This project is designed to reinforce core skills, including:

- **Writing Basic Python Functions**: Practicing defining functions with return values.
- **Implementing Arithmetic Operations**: Using operators for addition, subtraction, multiplication, and division.
- **Basic Error Handling**: Managing division by zero errors with conditional statements.
- **Git Version Control**: Applying Git commands for repository management.
- **Documentation**: Creating a README file to summarize the project.

## Git and GitHub Practice

This repository was created as an introduction to Git and GitHub for version control in business applications. Key skills include:

- **Creating a Repository**: Initializing a new Git repository.
- **Making Commits**: Regularly committing changes to record project history.
- **Writing a README File**: Documenting project details and usage instructions.
- **Understanding Git Workflows**: Familiarity with branching, merging, and pushing changes to GitHub.

## Future Improvements

There are several ways to expand and improve this basic calculator:

1. **Add a User Interface**: Develop a graphical or web-based user interface to enhance usability.
2. **Advanced Mathematical Functions**: Introduce additional functions, such as exponentiation, square root, and trigonometry.
3. **Enhanced Error Handling**: Improve input validation and handle more error scenarios.
4. **Interactive Mode**: Allow users to input their own numbers for on-demand calculations.

## Conclusion

This project demonstrates basic programming skills using Python and version control practices essential in modern software development. The calculator application serves as a practical exercise in function implementation, error handling, and using Git for project management.

## License

This project is licensed under the MIT License. For more details, please see the [LICENSE](LICENSE) file.

## Author

- **Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: [youremail@example.com](mailto:youremail@example.com)

---

**Basic Calculator** - A learning project for Business Application Development.
```
