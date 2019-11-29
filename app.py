#Server Dependencies 
from flask import Flask, jsonify
from flask import abort

#Computer Vision Dependencies


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
    return jsonify({'description': apiDescription[0]})

@app.route('/show-tell/api/v1.0/<string:test_code>', methods=['GET'])
def get_task(test_code):
    
    return_value = add_string(test_code)
    return jsonify({'description': return_value})


@app.route('/show-tell/api/v2.0/<string:image_code>', methods=['GET'])
def get_task(image_code):
    
    return_value = add_string(image_code)
    return jsonify({'description': return_value})


# Helper Functions 

def evaluate(image):
    return true

def add_string(input):
    return input + "yeeet"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
