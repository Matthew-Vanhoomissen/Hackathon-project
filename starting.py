from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('Design.html')

@app.route('/route-script', methods=['POST'])
def run_script():
    result = subprocess.run(['python', 'python.py'], capture_output=True, text=True)
    return jsonify(output=result.stdout)

if __name__ == '__main__':
    app.run(debug=True)