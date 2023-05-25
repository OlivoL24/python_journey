def calculate_loan_payment(principal, interest_rate, num_payments):
    # Convert interest rate from percentage to decimal
    interest_rate_decimal = interest_rate / 100.0

    # Calculate monthly interest rate
    monthly_interest_rate = interest_rate_decimal / 12.0

    # Calculate monthly payment
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

    return monthly_payment

def calculate_interest_paid(principal, interest_rate, num_payments, payment_number):
    # Convert interest rate from percentage to decimal
    interest_rate_decimal = interest_rate / 100.0

    # Calculate monthly interest rate
    monthly_interest_rate = interest_rate_decimal / 12.0

    # Calculate interest paid for a specific payment
    interest_paid = principal * monthly_interest_rate * (1 - (1 + monthly_interest_rate) ** (payment_number - num_payments)) / (1 - (1 + monthly_interest_rate) ** -num_payments)

    return interest_paid

# Example usage




if __name__ == "__main__":
  # Get the user input.
  principal = float(input("Enter the principal amount: "))
  interest_rate = float(input("Enter the interest rate: "))
  num_payments = int(input("Enter the number of monthly payments: "))

  # Calculate the interest and principal payments.
#   principal = 10000  # Loan principal amount
#   interest_rate = 5.0  # Annual interest rate
#   num_payments = 36  # Number of monthly payments

  monthly_payment = calculate_loan_payment(principal, interest_rate, num_payments)
  print(f"Monthly payment: ${monthly_payment:.2f}")

  for payment_number in range(1, num_payments + 1):
      interest_paid = calculate_interest_paid(principal, interest_rate, num_payments, payment_number)
      print(f"Month {payment_number}: Interest paid: ${interest_paid:.2f}")
