
# Setting Up Poetry with Playwright for Tests

This guide will walk you through setting up Poetry with Playwright to run tests using `pytest` on a new device after cloning the repository.

## Prerequisites

- Python installed (recommended version: 3.8+)
- Poetry installed ([Installation Guide](https://python-poetry.org/docs/#installation))

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/Martynas09/playwright_bet_test
cd playwright_bet_test
```

### 2. Create a `.env` File

Create a `.env` file in the root directory of the project and add the following line to set the `BETGAMES_URL`:

```
BETGAMES_URL=https://demo.betgames.tv/
```

You can replace `https://demo.betgames.tv/` with the appropriate URL if needed.

### 3. Install Dependencies

Run the following command to install dependencies using Poetry:

```sh
poetry install
```

### 4. Install Playwright Browsers

Install the required Playwright browsers:

```sh
poetry run playwright install
```

(Optional) Install Playwright dependencies for the OS:

```sh
poetry run playwright install-deps
```

### 5. Run Tests

To run the tests, use the following command:

```sh
poetry run python -m pytest
```

To run the tests with UI, use:

```sh
poetry run python -m pytest --headed
```

Now, your tests should work correctly with Poetry and Playwright!
