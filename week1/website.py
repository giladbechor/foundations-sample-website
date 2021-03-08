from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/students.html')
def first_page():
    return render_template('students.html', page_title="First Template")


@app.route('/about.html')
def second_page():
    return render_template('about.html', page_title="Second Template")

# add additonal pages here using a similar format as above


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
