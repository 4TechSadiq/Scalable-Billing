from flask import Flask, request, render_template


app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        # return render_template('index.html', data=request.form)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)