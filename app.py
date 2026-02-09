from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/service.html')
def service():
    return render_template('service.html')

@app.route('/team.html')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run()