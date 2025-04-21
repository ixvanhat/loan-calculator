# loan-calculator

A simple command-line loan calculator written in python. Supports "annuity" and "differentiated" payment calculations based on user-provided arguments via CLI.

## Features
Calculates:
- Monthly annuity payments
- Loan principal
- Loan duration in months
- Differentiated monthly payments
- Overpayments in each case
- Handles invalid or incomplete parameter combinations

## Usage
Run the script with appropriate arguments. E.g.:

### Calculate annuity payment
python loan_calculator.py --type=annuity --principal=10000 --periods=12 --interest=10

### Calculate number of months needed to repay:
python loan_calculator.py --type=annuity --principal=10000 --payment=10464 --interest=10

### Calculate differentiated payments
python loan_calculator.py --type=diff --principal=100000 --periods=12 --interest=10

------------------------------------------------------------------------------------------------------------------------------------------

**This project was made as part of Hyperskill's Python Developer career path.**
