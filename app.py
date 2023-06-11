from flask import Flask , request , jsonify
from covertor import convert_csv_to_json 
app = Flask(__name__)


@app.route('/convert', methods=['GET','POST'])
def App():
    try:
        if 'file' not in request.files:
                return jsonify({'error': 'No file found in the request'})

        file = request.files['file']
            
        # Convert data to JSON
        return convert_csv_to_json(file)
    except Exception as e:
        return jsonify({'error': 'Error converting CSV to JSON: {}'.format(str(e))})

 
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000, debug=True)