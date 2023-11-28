from flask import Flask, render_template
import subprocess

app = Flask(__name__)

def run_python_script(script_name):
    try:
        result = subprocess.run(['python3', script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout if result.stderr == '' else result.stderr
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html', python_output='')

@app.route('/contact')
def contact():
    script_output = run_python_script('vulnerscanfirewall.py')
    return render_template('index.html', python_output=script_output)

@app.route('/home')
def home():
    script_output = run_python_script('vulnerscanports.py') 
    return render_template('index.html', python_output=script_output)
    
@app.route('/news')
def news():
    script_output = run_python_script('projectportscannerandservice.py') 
    return render_template('index.html', python_output=script_output)

if __name__ == '__main__':
    app.run(debug=True)
