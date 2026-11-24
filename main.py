"""
Mini Smart Data Analyzer
Assignment 3 (15 Marks)

Run:
    pip install -r requirements.txt
    Copy .env.example to .env and add your Groq API key.
    python main.py
"""

import os
import numpy as np
import requests
from dotenv import load_dotenv

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "openai/gpt-oss-120b"


def get_user_data():
    """Read and validate at least 10 comma-separated numeric values."""
    while True:
        raw_data = input(
            "\nEnter at least 10 numbers, separated by commas:\n> "
        ).strip()

        try:
            # Convert the input string into a Python list of numbers.
            values = [float(item.strip()) for item in raw_data.split(",") if item.strip()]
            if len(values) < 10:
                print("Please enter at least 10 numerical values.")
                continue
            if not np.all(np.isfinite(values)):
                print("Please enter only finite numbers (no NaN or infinity).")
                continue
            return values
        except ValueError:
            print("Invalid input. Use numbers separated by commas, for example: 5, 8, 10.5")


def analyze_data(values):
    """Convert the list to a NumPy array and calculate the required results."""
    data_array = np.array(values, dtype=float)

    statistics = {
        "mean": float(np.mean(data_array)),
        "median": float(np.median(data_array)),
        "maximum": float(np.max(data_array)),
        "minimum": float(np.min(data_array)),
        "sum": float(np.sum(data_array)),
    }

    sorted_data = np.sort(data_array)
    above_mean = data_array[data_array > statistics["mean"]]

    return data_array, statistics, sorted_data, above_mean


def get_ai_insight(statistics):
    """Send calculated statistics to Groq and return a simple-English insight."""
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return (
            "AI insight unavailable: GROQ_API_KEY was not found. "
            "Add your key to the .env file and run the program again."
        )

    prompt = (
        "You are a friendly beginner-level data analysis tutor. Explain these "
        "statistics in simple English in 2-3 short sentences. Mention what the "
        "mean and median suggest and identify the range using minimum and maximum. "
        "Do not invent information.\n\n"
        f"Mean: {statistics['mean']}\n"
        f"Median: {statistics['median']}\n"
        f"Maximum: {statistics['maximum']}\n"
        f"Minimum: {statistics['minimum']}\n"
        f"Sum: {statistics['sum']}"
    )

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You explain numerical data clearly and simply."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.4,
        "max_tokens": 300,
    }

    try:
        response = requests.post(
            GROQ_API_URL, headers=headers, json=payload, timeout=30
        )
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as error:
        return f"Could not connect to Groq API: {error}"
    except (KeyError, IndexError, TypeError):
        return "Groq returned an unexpected response. Please try again."


def display_results(original_data, data_array, statistics, sorted_data, above_mean):
    """Display the original data, NumPy statistics, and array operations."""
    print("\n" + "=" * 52)
    print("             MINI SMART DATA ANALYZER")
    print("=" * 52)
    print("Entered data (Python list):", original_data)
    print("NumPy array:                ", data_array)

    print("\nSTATISTICS")
    print(f"Mean:    {statistics['mean']:.2f}")
    print(f"Median:  {statistics['median']:.2f}")
    print(f"Maximum: {statistics['maximum']:.2f}")
    print(f"Minimum: {statistics['minimum']:.2f}")
    print(f"Sum:     {statistics['sum']:.2f}")

    print("\nARRAY OPERATIONS")
    print("Ascending order:           ", sorted_data)
    print("Values greater than mean:  ", above_mean)


def main():
    """Control the complete program."""
    print("Welcome to the Mini Smart Data Analyzer!")
    values = get_user_data()
    data_array, statistics, sorted_data, above_mean = analyze_data(values)
    display_results(values, data_array, statistics, sorted_data, above_mean)

    print("\nAI-GENERATED INSIGHT")
    print(get_ai_insight(statistics))
    print("\nAnalysis complete. Thank you!")


if __name__ == "__main__":
    main()
