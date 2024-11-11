import random
import re

def generate_invoice_number():
    # Generate a 5-digit random number
    random_number = random.randint(10000, 99999)
    invoice_number = f"SCALE-{random_number}"
    
    # Regular expression to match the required format
    pattern = r"^SCALE-\d{5}$"
    
    # Verify that the generated invoice number matches the pattern
    if re.match(pattern, invoice_number):
        return invoice_number
    else:
        raise ValueError("Generated invoice number does not match the required format.")

# Example usage
# print(generate_invoice_number())
