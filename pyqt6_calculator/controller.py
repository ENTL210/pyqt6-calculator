def down_amount_calculation(principal_amount, down_percent):
    """Calculate the down amount with given loan amount and down percent..."""
    return principal_amount * (down_percent / 100)

def down_percent_calculation(down_amount, principal_amount):
    """Calculate the down percent with given loan amount and down amount..."""
    return round((down_amount / principal_amount) * 100, 2)

def output_calculation(principal_amount, down_amount, interest_rate, loan_duration_comboBox_currentIndex):
    """Calculate the monthly mortgage payment..."""
    total_loan_amount = principal_amount - down_amount
    monthly_interest_rate = interest_rate / 100 / 12
    number_of_payments_arr = [120, 180, 240, 360]
    number_of_payments = number_of_payments_arr[loan_duration_comboBox_currentIndex]
    monthly_mortgage_payment = total_loan_amount * ((monthly_interest_rate * ((1 + monthly_interest_rate) ** number_of_payments)) / (((1 + monthly_interest_rate) ** number_of_payments) - 1))
    return monthly_mortgage_payment

def convertToStringOutput(float_output):
    """Convert and round the output to a readable string value..."""
    return f"${round(float_output, 2)}"