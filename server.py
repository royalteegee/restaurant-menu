from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
app = Flask(__name__)
import os
from dotenv import load_dotenv
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine(os.getenv('DB_URI'))
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def allRestaurant():
    list = session.query(Restaurant).all()
    return render_template('hp.html', list=list)

@app.route('/menu/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items=items)

@app.route('/menu/<int:restaurant_id>/new/', methods=['POST', 'GET'])
def newMenu(restaurant_id):
    if request.method == 'POST':
        newMenuItem = MenuItem(name=request.form['name'], 
                               description=request.form['description'], 
                               price=request.form['price'], restaurant_id=restaurant_id)
        
        session.add(newMenuItem)
        session.commit()
        flash('New Dish added successfully')
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('addmenu.html', restaurant_id=restaurant_id)

@app.route('/menu/<int:restaurant_id>/<int:menu_id>/edit', methods=['POST', 'GET'])  # Added methods
def editMenu(restaurant_id, menu_id):
    editedDish = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedDish.name = request.form['name']
        if request.form['description']:
            editedDish.description = request.form['description']
        if request.form['price']:
            editedDish.price = request.form['price']
        session.add(editedDish)
        session.commit()
        flash('Dish name edited successfully')
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenu.html', menu_id=menu_id, restaurant_id=restaurant_id, editedDish=editedDish)  # Corrected menu_idid

@app.route('/menu/<int:restaurant_id>/<int:menu_id>/delete', methods=['POST', 'GET'])  # Added route parameters and methods
def delMenu(restaurant_id, menu_id):
    delDish = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(delDish)
        session.commit()
        flash('Dish item deleted successfully')
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('delobject.html', restaurant_id=restaurant_id, menu_id=menu_id, delDish=delDish)
    
@app.route('/healthcheck', methods=['Get'])
def healthcheck():
    return jsonify({"status": "ok", "message": "Restaurant Menu is LIVE!!!"}), 200

if __name__ == '__main__':
    app.debug = True
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
