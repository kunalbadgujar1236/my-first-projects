import re

def extract_numbers(text):
    # Find all numbers in the string, including floats
    matches = re.findall(r"[-+]?\d*\.\d+|\d+", text)
    return [float(match) for match in matches]

def calculate_percentage(total_amount, spent_amount):
    if total_amount == 0:
        raise ValueError("Total amount cannot be zero for percentage calculation.")
    percentage_spent = (spent_amount / total_amount) * 100
    return percentage_spent

def perform_calculation(text):
    # Extract numbers from the text
    numbers = extract_numbers(text)
    
    if len(numbers) < 2:
        raise ValueError("Not enough numbers found in the text to perform calculation.")

    # Assume the first number is the total amount and the second number is the spent amount
    total_amount = numbers[0]
    spent_amount = numbers[1]
    
    # Perform the percentage calculation
    percentage_spent = calculate_percentage(total_amount, spent_amount)
    
    return percentage_spent

# Example usage
text = "I have Rs 20 then I have spent Rs 5. How many percentage that I have spent out of
