# Billing System with Invoice Generation

This project is a billing system built using Python, Flask, and DoXcTPL for generating invoices in Word document format. The application allows users to enter customer details, list services, and automatically calculate totals, discounts, and balances. It generates a unique invoice number for each transaction and outputs a well-formatted invoice document.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Example Code Snippets](#example-code-snippets)
- [License](#license)

---

## Features

- Generate invoices with unique invoice numbers (e.g., `SCALE-12345`).
- Automatically fills in the billing date and time.
- Stores information about the biller, customer, and business.
- Input fields for service descriptions, costs, prices, and quantities.
- Calculates total amount, discount, advance payment, and balance payable.
- Exports invoices as `.docx` files with DoXcTPL templating.
- User-friendly web interface with input validation.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML/CSS, Jinja for templating
- **Document Generation**: DoXcTPL (for Word documents)
- **Other Libraries**: Regular expressions for generating unique invoice numbers

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/4TechSadiq/Scalable-Billing.git

