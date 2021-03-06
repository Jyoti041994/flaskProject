from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#Init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#setup database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir , 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Init DB
db = SQLAlchemy(app)

#Init MA
ma = Marshmallow(app)

#Product Model

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100) , unique = True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

def __init__(self,name,description,price,qty):
    self.name = name
    self.description = description
    self.price = price
    self.qty = qty


#Product Schema
class ProductSchema(ma.Schema):
    class Meta :
        fields = ('id','name','description','price','qty')

#Init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many= True)

#Create Product
@app.route('/product',methods= ['POST'])
def addProduct():
#  data = request.get_json()
 print("requesttttttttttt", request.is_json)
#  name = request.json['name']
#  description = request.json['description']
#  price = request.json['price']
#  qty = request.json['qty']

#  new_product = Product(name,description,price,qty)
#  db.session.add(new_product)
#  db.session.commit()

#  return product_schema.jsonify(new_product)



@app.route('/',methods=['GET'])
def getFunction():
    return jsonify({'msg' : 'Dummy route Success'})

#Run Server
if __name__ == '__main__':
    app.run(debug=True)