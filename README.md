# Playwright Test Framework

Test framework for automating tests on the Gumroad.com website using Playwright.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Structure](#structure)
- [License](#license)

## Installation

### Prerequisites

- Python 3.7+ 

### Clone the Repository

```sh
git clone https://github.com/davidherrera83/playwright-test-framework.git
cd playwright-test-framework
```

### Install Python Dependencies
Create a virtual environment and activate it:
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required Python packages:
```sh
pip install -r requirements.txt
```

Install Playwright and the necessary browser binaries:
```sh
pip install playwright
playwright install
```

## Usage
### Opening the Project in VS Code
1. Open VS Code.
2. Go to File -> Open Folder and select the playwright-test-framework folder.
3. Open a terminal in VS Code (Terminal -> New Terminal).

### Running Tests
To run the tests, use the following command in the terminal:
```sh
pytest
```
> This will execute all tests in the tests directory.

### Running Specific Tests
To run a specific test, use:
```sh
pytest tests/test_gumroad.py::test_gumroad_search_by_store
```
> Replace test_gumroad_search_by_store with the name of the test you want to run.

## Structure

* gumroad/: Contains the application-specific classes and methods.
* gumroad.py: Contains the GumroadApp class with methods for interacting with the Gumroad site.
* tests/: Contains test cases.
    * test_gumroad.py: Contains test cases for the Gumroad site.
* conftest.py: Contains fixtures for the tests.
* requirements.txt: Lists the Python dependencies.
* README.md: This file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
