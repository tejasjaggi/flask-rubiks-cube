from flask import Flask
from rubik_solver import utils
from flask import request, jsonify, make_response
app = Flask(__name__)

@app.route("/solveCube", methods=['POST'])
def solveCube():  
  cube = request.json['cube']
  technique = "Beginner"
  if technique == 'Beginner':
    steps = utils.solve(cube, 'Beginner')
  elif technique == "CFOP":
    steps = utils.solve(cube, 'CFOP')
  elif technique == "Kociemba":
    steps = utils.solve(cube, 'Kociemba')
  output = [str(i) for i in steps]
  return jsonify({'result': output})

@app.route("/")
def hello():
  cube = 'oobywyywogbbogrgbgrbbyrgogrygwrbwggoryyrobboywowrywrww'
  step = utils.solve(str(cube), 'Beginner')
  return 'success'

# @app.errorhandler(Exception)
# def handle_exception(e):
#     # pass through HTTP errors
#     if isinstance(e, HTTPException):
#         return e

#     # now you're handling non-HTTP exceptions only
#     return ("Error incorrect colours"), 500

if __name__ == "__main__":
  app.run()
  