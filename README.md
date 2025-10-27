# 🧮 Advanced Calculator

[![Python Application](https://github.com/StrayDogSyn/AISE-week05-d1/actions/workflows/python-app.yml/badge.svg)](https://github.com/StrayDogSyn/AISE-week05-d1/actions/workflows/python-app.yml)
[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code Style](https://img.shields.io/badge/code%20style-flake8-brightgreen.svg)](https://flake8.pycqa.org/)
[![Testing](https://img.shields.io/badge/testing-pytest-yellow.svg)](https://pytest.org/)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](LICENSE)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF.svg)](https://github.com/features/actions)

> A professional-grade calculator application with CI/CD automation

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Testing](#-testing) • [CI/CD](#-cicd-pipeline)

---

## 📋 Overview

This repository demonstrates professional software engineering practices through the implementation of an advanced calculator application with comprehensive CI/CD automation. Developed as part of the JTC Week 5 AISE curriculum, it showcases:

- **Clean Architecture**: Well-structured, maintainable Python code
- **Automated Testing**: Comprehensive test coverage with pytest
- **Continuous Integration**: Automated linting and testing on every commit
- **Code Quality**: Enforced coding standards with flake8
- **Documentation**: Professional technical documentation

## ✨ Features

### Core Functionality

- ✅ Basic arithmetic operations (add, subtract, multiply, divide)
- ✅ Advanced calculator class with operator precedence
- ✅ Expression parsing and tokenization
- ✅ Support for mathematical functions (sqrt, sin, cos, tan, log, etc.)
- ✅ Built-in mathematical constants (π, e)
- ✅ Extensible architecture for custom functions and operators

### Engineering Excellence

- 🔄 **Automated CI/CD Pipeline**: GitHub Actions workflow
- 🧪 **Comprehensive Testing**: Unit tests with pytest
- 📊 **Code Quality Checks**: Flake8 linting
- 🎯 **Type Hints**: Full type annotation support
- 📝 **Clean Code**: PEP 8 compliant
- 🏗️ **Modular Design**: Reusable components

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/StrayDogSyn/AISE-week05-d1.git
   cd AISE-week05-d1
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:

   ```bash
   pip install pytest flake8
   ```

## 💻 Usage

### Basic Calculator Functions

```python
from app.calculator import add, subtract, multiply, divide

# Basic arithmetic
result = add(10, 5)        # Returns: 15
result = subtract(10, 5)   # Returns: 5
result = multiply(10, 5)   # Returns: 50
result = divide(10, 5)     # Returns: 2.0
```

### Advanced Calculator Class

```python
from app.calculator import Calculator

calc = Calculator()

# Tokenize expressions
tokens = calc.tokenize("2 + 3 * 4")

# Access mathematical constants
pi_value = calc.constants['pi']
e_value = calc.constants['e']

# Use built-in functions
import math
result = calc.functions['sqrt'](16)  # Returns: 4.0
```

## 🧪 Testing

### Run All Tests

```bash
pytest app/test_calc_pass.py -v
```

### Run Specific Tests

```bash
pytest app/test_calc_pass.py::test_add -v
pytest app/test_calc_pass.py::test_subtract -v
pytest app/test_calc_pass.py::test_multiply -v
```

### Test Coverage

```bash
pytest app/test_calc_pass.py --cov=app --cov-report=html
```

### Expected Output

```text
================================= test session starts =================================
platform win32 -- Python 3.10+, pytest-8.4.2, pluggy-1.6.0
collected 3 items

app/test_calc_pass.py::test_add PASSED                                          [ 33%]
app/test_calc_pass.py::test_subtract PASSED                                     [ 66%]
app/test_calc_pass.py::test_multiply PASSED                                     [100%]

================================== 3 passed in 0.12s ==================================
```

## 🔄 CI/CD Pipeline

### Automated Workflow

Our GitHub Actions workflow automatically:

1. **Triggers** on every push and pull request to `main`
2. **Sets up** Python 3.10 environment
3. **Installs** all required dependencies
4. **Lints** code with flake8 for quality assurance
5. **Runs** comprehensive test suite with pytest

### Workflow Status

Check the current build status: [![Build Status](https://github.com/StrayDogSyn/AISE-week05-d1/actions/workflows/python-app.yml/badge.svg)](https://github.com/StrayDogSyn/AISE-week05-d1/actions/workflows/python-app.yml)

### Quality Gates

- ✅ All tests must pass
- ✅ No critical linting errors (E9, F63, F7, F82)
- ✅ Code complexity checks
- ✅ Maximum line length: 127 characters

## 📁 Project Structure

```text
AISE-week05-d1/
├── .github/
│   └── workflows/
│       └── python-app.yml      # CI/CD workflow configuration
├── app/
│   ├── __init__.py            # Package initialization
│   ├── calculator.py          # Core calculator implementation
│   └── test_calc_pass.py      # Comprehensive test suite
├── LICENSE                     # MIT License
└── README.md                   # Project documentation
```

## 🛠️ Development

### Code Quality

This project maintains high code quality standards:

- **Linting**: Enforced with flake8
- **Type Hints**: Full type annotation coverage
- **Documentation**: Comprehensive docstrings
- **Testing**: Unit tests for all functions

### Running Linting

```bash
# Check for critical errors
flake8 app --count --select=E9,F63,F7,F82 --show-source --statistics

# Full lint check
flake8 app --count --max-complexity=10 --max-line-length=127 --statistics
```

## 📚 Learning Objectives

This project demonstrates mastery of:

- ✅ Python programming fundamentals
- ✅ Object-oriented design principles
- ✅ Test-driven development (TDD)
- ✅ Continuous Integration/Continuous Deployment
- ✅ Git version control and GitHub workflows
- ✅ Code quality and linting practices
- ✅ Professional documentation standards

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

All contributions must:

- Pass the CI/CD pipeline
- Include appropriate tests
- Follow PEP 8 style guidelines
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Course Information

**Course**: AISE (AI Software Engineering)\
**Week**: 5 - Day 1\
**Institution**: JTC (Job Training Center)\
**Focus**: CI/CD Workflows and Automated Testing

## 🙏 Acknowledgments

- GitHub Actions for CI/CD infrastructure
- pytest for robust testing framework
- flake8 for code quality enforcement
- The Python community for excellent tooling

---

Built with ❤️ for learning and excellence

[⬆ Back to Top](#-advanced-calculator)
