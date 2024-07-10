from flask import Flask, render_template
from flask import request
from analis import Genom


app = Flask(__name__)

number_level = ['1 уровень', '2 уровень', '3 уровень', '4 уровень']


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        levels = Genom().analis(request.form)
        if levels:
            return render_template(
                'index.html',
                levels=list(enumerate(levels)),
                number_level=number_level
            )
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
