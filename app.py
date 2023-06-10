from flask import Flask, render_template, request

app = Flask(__name__)

# List of items for the first container
items = ['Item 1', 'Item 2', 'Item 3', 'Item 4']

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/reset', methods=['POST'])
def reset():
    # Clear the second container and reset the first container
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
