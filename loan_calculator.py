# write your code here
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--payment", type=float, help="This is the payment amount")
parser.add_argument("--principal", type=float, help="The amount of loan")
parser.add_argument("--periods", type=int, help="Denotes the number of months needed to repay the loan.")
parser.add_argument("--interest", type=float, help="Is specified without a percent sign.")
parser.add_argument("--type", type=str, help="Indicates the type of payment: 'annuity' or 'diff'")

args = parser.parse_args()

interest = args.interest
payment = args.payment
principal = args.principal
periods = args.periods
loan_type =  args.type

if (
    loan_type not in ["annuity", "diff"]
    or interest is None
    or interest < 0
    or (loan_type == "diff" and payment is not None)
    or sum(arg is not None for arg in [principal, payment, periods, interest]) < 3
    or any(x is not None and x < 0 for x in [principal, payment, periods])
):
    print("Incorrect parameters")
    exit()

#Calculate interest rate
i = interest / (12 * 100)


def calc_payment(principal, periods, i):
    payment = (principal * (i * (1 + i) ** periods)) / ((1 + i) ** periods - 1)
    payment = math.ceil(payment)
    overpayment = payment * periods - principal
    print(f"Your annuity payment = {payment}!")
    print(f"Overpayment = {overpayment}")

    
def calc_principal(payment, periods, i):
    principal = payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
    principal = math.floor(principal)
    overpayment = payment * periods - principal
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {overpayment}")


def calc_periods(payment, principal, i):
        periods = math.log(payment / (payment - i * principal)) / math.log(1 + i)
        return math.ceil(periods)

def calc_number_of_months(periods, payment, principal):    
    years = periods // 12
    months = periods % 12
    if years > 0 and months > 0:
        print(f"It will take {years} years and {months} months to repay this loan!")
    elif years > 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {months} months to repay this loan!")

    overpayment = payment * periods - principal
    print(f"Overpayment = {math.ceil(overpayment)}")

def calc_differentiated_payment(principal, periods, i):
    total_payment = 0
    for m in range(1, periods + 1):  
        diff_payment = math.ceil(principal / periods + i * (principal - (principal * (m - 1) / periods)))
        total_payment += diff_payment
        print(f"Month {m}: payment is {diff_payment}")
    overpayment = total_payment - principal
    print(f"Overpayment = {overpayment}")


if loan_type == "diff":
    if principal is None or periods is None:
        print("Principal and periods must be specified for differentiated payment calculation.")
        exit()
    calc_differentiated_payment(principal, periods, i)


elif loan_type == "annuity":
    if principal is None and payment is not None and periods is not None:
        calc_principal(payment, periods, i)

    elif principal is not None and payment is None and periods is not None:
        calc_payment(principal, periods, i)

    elif principal is not None and payment is not None and periods is None:
        calculated_periods = calc_periods(payment, principal, i)
        calc_number_of_months(calculated_periods, payment, principal)


