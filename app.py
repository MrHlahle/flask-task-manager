from flask import Flask, render_template, redirect, request, url_for

#create flask app
app = Flask (__name__)

#create list of tasks 
tasks = []

#home route 
@app.route ('/')
def index():
    return render_template('index.html',tasks=tasks)

#add route 
@app.route ('/add', methods=['POST'])
def add_tasks():
    task_content = request.form['content']
    tasks.append({'content':task_content})
    return redirect(url_for('index'))

#delete route 
@app.route ('/delete/<int:task_id>')
def delete_tasks(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))

#run the server 
if __name__ == "__main__":
   app.run(debug=True) 

