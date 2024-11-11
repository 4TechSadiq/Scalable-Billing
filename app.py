from flask import Flask, request, render_template
from invoice_number import generate_invoice_number


app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        billed_date = request.form.get('billed_date')
        billed_time = request.form.get('billed_time')
        biller_name = request.form.get('billed_by')
        invoice_no = generate_invoice_number()
        customer_name = request.form.get('customer_name')
        customer_address = request.form.get('customer_address')
        business_name = request.form.get('business_name')
        mode_of_payment = request.form.get('payment_mode')
        service_desc = request.form.getlist('service')
        service_price = request.form.getlist('price')
        service_quantity = request.form.getlist('quantity')
        advance_pay = request.form.get('advance')
        discount = request.form.get('discount')
        total_price = request.form.get('total_price')
        discounted_price = request.form.get('discounted_price')
        balance_payable = request.form.get('balance_payable')

        context ={
            'billing_date': billed_date,
            'billing_time': billed_time,
            'invoice_no': invoice_no,
            'biller_name': biller_name,
            'business_name': business_name,
            'customer_name': customer_name,
            'customer_address': customer_address,
            'mode_of_payment': mode_of_payment,
            'service_desc': service_desc,
            'service_price': service_price,
            'service_quantity': service_quantity,
            'discount': discount,
            'total_price': total_price,
            'advance_pay': advance_pay,
            'balance_payable': balance_payable,
            'discounted_price': discounted_price,
        }
        print(context)

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)