# Mini Smart Data Analyzer

A beginner-friendly Python project for Assignment 3. It accepts at least 10 numerical values, analyzes them with NumPy, and requests a short explanation from the Groq API.

## Features
- Validates user input and requires at least 10 finite numerical values.
- Stores the input in a Python list and converts it to a NumPy array.
- Calculates mean, median, maximum, minimum, and sum with NumPy.
- Displays the data in ascending order and values greater than the mean.
- Uses separate functions to organize the program.
- Sends the calculated statistics to Groq for a simple-English AI insight.
- Keeps the API key in `.env`, which is excluded from Git.

## Requirements
- Python 3.9 or newer
- A Groq API key

## Setup
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. (Recommended) Create and activate a virtual environment:
   - Windows: `python -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Copy `.env.example` to a file named `.env`.
6. Put your own Groq key in `.env`:
   ```env
   GROQ_API_KEY=your_actual_key
   ```
7. Run:
   ```bash
   python main.py
   ```

If no API key is configured, the numerical analysis still runs and the program displays a clear message explaining how to enable the AI insight.

## Example input
`12, 15, 18, 20, 22, 25, 28, 30, 32, 35`

## Project structure
```text
mini-smart-data-analyzer/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── screenshots/
    └── sample_output.png
```

## GitHub submission
Create a **public** GitHub repository, for example `mini-smart-data-analyzer`, then run these commands from this folder (replace the remote URL with your own repository URL):

```bash
git init
git add .
git commit -m "Complete Mini Smart Data Analyzer assignment"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/mini-smart-data-analyzer.git
git push -u origin main
```

**Important:** Never commit `.env` or paste your API key into source code. `.gitignore` already excludes `.env`. Before pushing, check the files staged with `git status`.

## Viva preparation
- **Why use NumPy?** It provides convenient numerical operations such as `mean`, `median`, `max`, `min`, `sum`, and sorting.
- **Why convert the list to an array?** NumPy functions operate efficiently on arrays and support boolean filtering.
- **How are values above the mean selected?** `data_array > mean` creates a Boolean mask; using it inside `data_array[...]` selects matching values.
- **Why use functions?** Functions divide the program into input, analysis, display, and AI tasks, making it easier to read and test.
- **How is the API key protected?** `python-dotenv` reads it from `.env`; `.gitignore` prevents that file from being committed.
- **What does the AI receive?** Only the five calculated statistics, not the original list or any personal information.
