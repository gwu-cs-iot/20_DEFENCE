#!env/bin/python
from flask import Flask, jsonify
from tello import Tello

app = Flask(__name__)
tello = Tello()
tello.initialize()

@app.route('/drone/command/takeoff', methods=['POST'])
def drone_takeoff():
    print('Drone now taking off...')
    tello.takeoff()
    return jsonify({'status': 'OK'})


@app.route('/drone/command/land', methods=['POST'])
def drone_land():
    print('Drone now landing...')
    tello.land()
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run(debug=False, host='10.0.0.3')
    tello.end()

