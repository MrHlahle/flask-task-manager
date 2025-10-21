from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_tasks():
    task_content = request.form['content']
    if task_content.strip():
        tasks.append({'content': task_content})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_tasks(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
