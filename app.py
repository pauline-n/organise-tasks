from bottle import route, run, request, template, redirect, error
from myconnection import connect_to_mysql

db_config = {
    'host': 'localhost',
    'user': 'pola',
    'password': 'pola',
    'database': 'todos',
    'use_pure': False
}

cnx = connect_to_mysql(db_config, attempts=3)
cursor = cnx.cursor()
@route('/', method='GET')
def my_todos():
    
    if cnx and cnx.is_connected():
        cursor.execute("SELECT id, task, status FROM tasks")
        tasks = cursor.fetchall()
        # for row in rows:
        #     print(rows)
        cnx.close()
        return template('list.tpl', tasks=tasks)
    else:
        print('could not connect: ')
    

@route('/todo', method=["GET", "POST"])
def add_todo():
    task = request.forms.get('task')
    print(f"Task: {task}")
    
    if not task:
        return template('add_todo.tpl', error='Task field cannot be empty!')
    try:
        cursor.execute('INSERT INTO tasks (task) VALUES (%s)', (task,))
        cnx.commit()
    except Exception as e:
        return f"Error: {e}"
    
    redirect('/')
    return template('add_todo.tpl', task=task)
    # redirect('/')

@route('/todo/<task_id:int>', method=["PATCH"])
def single_todo(task_id):
    new_task = request.forms.get('task')
    print('my God')
    
    if not new_task:
        return template('edit_todo.tpl', error='Task field cant be empty')
    try:
        cursor.execute('UPDATE tasks SET task = %s WHERE id=%', (new_task, task_id))
        cnx.commit()
        print('hi u')
    except Exception as e:
        return f"Error: {e}"
        print('nooo')
    redirect('/')
    return template('edit_todo.tpl', task=new_task)

if __name__== '__main__':
    run(host='localhost', port=8080, reloader=True, debug=True)