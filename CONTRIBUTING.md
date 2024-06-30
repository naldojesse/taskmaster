# Contributing to TaskMaster AI

Thank you for considering contributing to TaskMaster AI! We welcome contributions from the community to help improve and expand the project. This document outlines the process for contributing to the project.

## Table of Contents
- [Contributing to TaskMaster AI](#contributing-to-taskmaster-ai)
  - [Table of Contents](#table-of-contents)
  - [How to Contribute](#how-to-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Features](#suggesting-features)
    - [Submitting Pull Requests](#submitting-pull-requests)
  - [Development Setup](#development-setup)
  - [Style Guide](#style-guide)
  - [Testing](#testing)
  - [License](#license)

## How to Contribute

### Reporting Bugs

If you find a bug, please report it by opening an issue on our [GitHub Issues](https://github.com/yourusername/taskmaster-ai/issues) page. Include as much detail as possible to help us understand and reproduce the issue.

### Suggesting Features

We welcome feature suggestions! To suggest a feature, please open an issue on our [GitHub Issues](https://github.com/yourusername/taskmaster-ai/issues) page and provide a detailed description of the feature and its benefits.

### Submitting Pull Requests

1. **Fork the repository:**
    ```bash
    git fork https://github.com/yourusername/taskmaster-ai.git
    ```

2. **Create a new branch:**
    ```bash
    git checkout -b feature/your-feature-name
    ```

3. **Make your changes and commit them:**
    ```bash
    git commit -m "Add some feature"
    ```

4. **Push to the branch:**
    ```bash
    git push origin feature/your-feature-name
    ```

5. **Create a pull request:**
    Go to the original repository on GitHub and open a pull request with a detailed description of your changes.

## Development Setup

To set up the development environment, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/taskmaster-ai.git
    cd taskmaster-ai
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the root directory and add necessary environment variables. Example:
    ```env
    API_KEY=your_api_key
    ```

5. **Run initial setup scripts (if any):**
    ```bash
    python setup.py
    ```

## Style Guide

Please follow the coding style guidelines outlined in our [Style Guide](https://github.com/yourusername/taskmaster-ai/blob/main/STYLE_GUIDE.md).

## Testing

To run tests, use the following commands:

- **Unit tests:**
    ```bash
    pytest tests/unit
    ```

- **Integration tests:**
    ```bash
    pytest tests/integration
    ```

- **Performance tests:**
    ```bash
    pytest tests/performance
    ```

## License

By contributing to TaskMaster AI, you agree that your contributions will be licensed under the MIT License.
