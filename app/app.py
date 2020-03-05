from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app = app,
    version = "1.0", 
    title = "Web Service Data API", 
    description = "Mock example of API DATA"
)

name_space = api.namespace('Flask API', description='Mock Example')

@name_space.route("/")
@name_space.param('ejemplo', 'desc')
@name_space.doc(params={'desc':'algo'})
class MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}

    # @api.response(403, 'Not Authorized')
    # def post(self, id):
    #     api.abort(403)

	# def post(self):
	# 	return {
	# 		"status": "Posted new data"
	# 	}

if __name__ == '__main__':
    app.run(debug=True)
