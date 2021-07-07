from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG , format=f'%(asctime)s : %(message)s')

@app.route("/")
def hello():
    app.logger.debug('Hello Was reached')
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.debug('Status Was reached')
    return {"result": "OK - healthy"}, 200

@app.route("/metrics")
def metrics():
    app.logger.debug('Metrics Was reached')
    return {"data": {"UserCount": 140 ,"UserCountActive": 23}}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')


# @app.route('/status')
# def status():
#     response = app.response_class(
#             response=json.dumps({"result":"OK - healthy"}),
#             status=200,
#             mimetype='application/json'
#     )

#     return response

# @app.route('/metrics')
# def metrics():
#     response = app.response_class(
#             response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
#             status=200,
#             mimetype='application/json'
#     )

#     return response