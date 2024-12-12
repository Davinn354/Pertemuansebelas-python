from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        result = f"You submitted: {input_text}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
