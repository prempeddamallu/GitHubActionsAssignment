# Python Calculator

## Overview

The Python Calculator project is a simple calculator application implemented in Python. It provides basic arithmetic operations such as addition, subtraction, multiplication, and division. The project includes automated tests to ensure the correctness of these operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division

## Getting Started

To get started with the Python Calculator, follow these instructions to set up and run the project locally.

## Prerequisites

Ensure you have Python installed. This project supports Python versions 3.8, 3.9, 3.11, and 3.12.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/prempeddamallu/GitHubActionsAssignment.git
    cd GitHubActionsAssignment
    ```

2. **Install dependencies:**

    ```bash
    python -m pip install --upgrade pip
    pip install pytest
    ```

## Running the Project

1. **Navigate to the `src` directory:**

    ```bash
    cd src
    ```

2. **Run the Python script:**

    ```bash
    python calculator.py
    ```

## GitHub Actions

This repository uses GitHub Actions to automate testing and ensure code quality. The workflow configuration file is located at `.github/workflows/main.yml`.

### Workflow Details

- **Trigger Events**: The workflow is triggered on `push` and `pull_request` events to the `main` branch.
- **Jobs**:
  - **Build**: Runs on the latest Ubuntu environment and tests across multiple Python versions (3.8, 3.9, 3.11, and 3.12).
- **Steps**:
  - Checkout code
  - Set up Python
  - Install dependencies
  - Run tests

The GitHub Actions workflow will automatically run tests whenever changes are pushed to the repository or when a pull request is created.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. **Fork the repository** to your own GitHub account.
2. **Create a new branch** for your changes.
3. **Make your changes** and test them locally.
4. **Submit a pull request** describing your changes and why they are beneficial.

