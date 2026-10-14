def simple_interest(principal, rate, time):
    """Return the simple interest for a principal amount."""
    return (principal * rate * time) / 100


def total_amount(principal, rate, time):
    """Return the total amount after adding simple interest."""
    return principal + simple_interest(principal, rate, time)


def main():
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter time in years: "))

        interest = simple_interest(principal, rate, time)
        amount = total_amount(principal, rate, time)

        print(f"Simple Interest: {interest}")
        print(f"Total Amount: {amount}")
    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()
