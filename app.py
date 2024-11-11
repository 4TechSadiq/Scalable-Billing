from flask import Flask, request, render_template


app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        billed_date = request.form.get('billed_date')
        billed_time = request.form.get('billed_time')
        biller_name = request.form.get('billed_by')
        invoice_no = request.form.get('invoice_no')
        
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)