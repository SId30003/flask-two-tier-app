from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Greeting page
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    return render_template('greet.html', name=name)

# API route (extra cool)
@app.route('/api')
def api():
    return {
        "message": "Flask CI/CD is working 🚀",
        "status": "success"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
