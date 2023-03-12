from flask import Flask, jsonify, request
from flask_cors import CORS
from userProfile import userProfile

app = Flask(__name__)
CORS(app)

profile = userProfile()


#Accepts value from React
@app.route('/api', methods=['POST', 'GET'])
def api():
    
    if request.method == 'POST':
        nameData = request.get_json()
        profile.setName(nameData)
        return 'done'   #Idk how to process this in react

    #Sends value to React
    elif request.method =='GET':
        data = profile.startProcess()
        return (jsonify(data))

if __name__ == '__main__':
    app.run(debug=True)