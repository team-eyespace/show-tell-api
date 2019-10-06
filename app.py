from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


from flask import abort

@app.route('/show-tell/api/v1.0/<string:task_id>', methods=['GET'])
def get_task(task_id):
    
    return jsonify({'return value': task_id})
    

if __name__ == '__main__':
    app.run(debug=True)



# Archive

# task = [task for task in tasks if task['id'] == task_id]
    # if len(task) == 0:
    #     abort(404)
    # return jsonify({'task': task[0]})
    # if len(task_id) == 0:
    #     abort(404)
    # if (task_id == 1):
    #     return jsonify({'task': tasks[0]})
    # elif (task_id == 2):
    #     return jsonify({'task': tasks[1]})