from app import app, lm
from pymongo import MongoClient
from flask import request, redirect, render_template, url_for, flash
from flask.ext.login import current_user, login_user, logout_user, login_required
from .forms import LoginForm, StoreForm, ProductForm
from .user import User
collection = MongoClient()['store']['store_collection']
prod_coll = MongoClient()['store']['product_collection']


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/store/new', methods=['GET', 'POST'])
@login_required
def new_store():
    form = StoreForm()
    if form.validate_on_submit():
        store = {"title":form.title.data,"description":form.description.data,"user_id":form.username.data}
        collection.insert(store)
        return redirect(url_for('home'))
    return render_template('store_form.html', form=form)

@app.route('/product/new', methods=['GET', 'POST'])
@login_required
def new_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = {"title":form.product_name.data,"description":form.description.data,"user_id":form.username.data}
        prod_coll.insert(product)
        return redirect(url_for('home'))
    return render_template('product_form.html', form=form)
