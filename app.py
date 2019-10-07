from flask import Flask, jsonify
from flask import abort

app = Flask(__name__)

#API description
apiDescription = [
    {
        'title': u'Show and Tell API',
        'description': u'Eyespace API hosted on a compute engine instance', 
        'Author': u'Team Eyespace'
    }
]

@app.route('/show-tell/api/v1.0/about', methods=['GET'])
def get_tasks():
    return jsonify({'Description': apiDescription[0]})

@app.route('/show-tell/api/v1.0/<string:image_code>', methods=['GET'])
def get_task(image_code):
    
    return_value = add_string(image_code)
    return jsonify({'return value': return_value})


# Helper Functions 

def add_string(input):
    return input + "yeeet"

if __name__ == '__main__':
    app.run(debug=True)
