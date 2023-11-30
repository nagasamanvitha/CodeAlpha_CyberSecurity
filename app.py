from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    user_input = request.args.get('input_data')
    return render_template('index.html', input_data=user_input)

@app.route('/redirect')
def redirect_example():
    destination = request.args.get('destination')
    return redirect(url_for(destination))

if __name__ == '__main__':
    app.run(debug=True)
