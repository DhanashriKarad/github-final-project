# Simple Interest Calculator

A simple Python project that calculates simple interest using the formula:

`Simple Interest = (Principal × Rate × Time) / 100`

## Features
- Calculates simple interest from principal, rate, and time
- Computes total amount payable
- Includes a small test suite

## Usage

```bash
python3 simple_interest.py
```

You will be prompted to enter:
- principal amount
- annual interest rate (%)
- time period (years)

Example output:

```text
Enter principal amount: 1000
Enter annual interest rate (%): 5
Enter time in years: 2
Simple Interest: 100.0
Total Amount: 1100.0
```

## Run tests

```bash
python3 -m unittest discover -s tests
```
