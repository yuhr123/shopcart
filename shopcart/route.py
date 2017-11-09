from shopcart import app, db
from flask import render_template, request
from datetime import datetime
from random import randrange
from shopcart.model.order import Order

@app.route('/test')
def test():
    return str(app.config["DEBUG"])

@app.route('/')
def index():
    orders = Order.query.all()
    return render_template('hello.html', title='模板', data=orders)


@app.route('/add', methods=['POST', 'GET'])
def add_order():
    gen_id = datetime.now().strftime('%y%m%d%H%m') + str(randrange(1000, 9999))
    order = Order()
    order.id = gen_id
    order.buyer = request.form['buyer']
    order.mobile = request.form['mobile']
    order.address = request.form['address']
    order.email = request.form['email']
    order.express_id = request.form['express_id']
    db.session.add(order)
    db.session.commit()
    return '订单：' + order.id + ' 已生成！'

@app.route('/del/<id>')
def del_order(id):
    order = Order.query.filter_by(id=id).first()
    db.session.delete(order)
    db.session.commit()
    return '订单：' + id + ' 已删除！'
