from flask import Flask , request
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    conttext=db.all()
    return conttext



# view add grocery
@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    conttext=request.get_json()
    db.add(conttext)
    return conttext


# view all grocery by type
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    conttext=db.get_by_type(type=type)
    return conttext
            


# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    conttext=db.get_by_name(name=name)
    return conttext


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    conttext=db.get_by_price(price=price)
    return conttext



if __name__ == '__main__':
    app.run(debug=True)