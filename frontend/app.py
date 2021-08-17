from flask import Flask
from flask_restx import Api, Resource
#
from db import init_db, store_log, get_log
#
import logging
#
app = Flask(__name__)
api = Api(app)

class Model():
    def predict(self, x):
        return int(x**2 + 1)
# Create model instance (and maintains in ram)
model = Model()
#
@api.route('/predict/<int:input_x>')
class Prediction(Resource):
    def get(self, input_x):
        pred_y = model.predict(input_x)
        response = {'pred_y': pred_y}
        logging.warning(f'response: {response}')
        # escreve log do request em banco
        store_log({'input_x':input_x,'pred_y':pred_y}) 
        #
        return response
#
@api.route('/initdb/')
class DB(Resource):
    def get(self):   
        init_db()
        return 'Banco Inicializado'

#
@api.route('/logs/')
class Logs(Resource):
    def get(self):   
        return get_log()
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
