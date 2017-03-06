# coding: utf-8
from flask import render_template, Blueprint
bp = Blueprint('site', __name__)
from ..models.product import Product


@bp.route('/')
def index():
    """Index page."""
    products = Product.query.all()
    return render_template('site/index/index.html', products=products)




@bp.route('/about')
def about():
    """About page."""
    return render_template('site/about/about.html')