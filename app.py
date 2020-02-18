from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_restplus import Api, Resource, fields

flask_app = Flask(__name__)
app = Api(app = flask_app,
    version = "1.0", 
    title = "Web Service API", 
    description = "Mock example of API DATA"
)

name_space = app.namespace('Flask API', description='Mock Example')

@name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	# def post(self):
	# 	return {
	# 		"status": "Posted new data"
	# 	}

if __name__ == '__main__':
    flask_app.run(debug=True)
