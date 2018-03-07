"""."""


def calc_fixed_amount(balance, annualInterestRate):
    """."""
    monthly_ir = 1 + (annualInterestRate / 12.0)
    payment = 0
    updated_balance = balance

    while updated_balance > 0:
        updated_balance = balance
        payment += 10
        previous_balance = balance

        for i in range(0, 12):
            updated_balance = (updated_balance - payment) * monthly_ir

    print(payment)

# calc_fixed_amount(4773, 0.2)


def calc_bisect(balance, annualInterestRate):
    """."""
    # Paste your code into this box
    monthlyInterestRate = 1 + (annualInterestRate/12)
    lowerBound = balance/12
    upperBound = (balance * (1+monthlyInterestRate)**12)/12
    fixedPayment = (lowerBound + upperBound) / 2
    remainingBalance = balance

    while remainingBalance > 0.01 or remainingBalance < -0.01:
        remainingBalance = balance

        for i in range(12):
            remainingBalance = (remainingBalance - fixedPayment) * monthlyInterestRate
                

        if remainingBalance > 0.01:
            lowerBound = fixedPayment
            fixedPayment = (lowerBound + upperBound)/2

        elif remainingBalance < -0.01:
            upperBound = fixedPayment
            fixedPayment = (lowerBound + upperBound)/2

    print(fixedPayment)


calc_bisect(320000, 0.2)
