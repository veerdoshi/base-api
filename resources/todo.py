from flask_restful import Resource

class Todo(Resource):
  def get(self):
      return {'Fires': 1}
