from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
task_id_counter = 0

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global task_id_counter
    new_task = request.form.get('newTask')
    if new_task:
        tasks.append({'id': task_id_counter, 'task': new_task, 'completed': False})
        task_id_counter += 1
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            del tasks[i]
            break
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            if request.method == 'POST':
                new_task = request.form.get('newTask')
                task['task'] = new_task
                return redirect(url_for('index'))
            else:
                return render_template('edit.html', task=task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)