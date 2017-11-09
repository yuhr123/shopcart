from shopcart import db
from datetime import datetime, timedelta, timezone

class Order(db.Model):
    # 由程序生成唯一的订单号
    id = db.Column(db.Integer, primary_key=True)
    buyer = db.Column(db.String(50), nullable=False)
    mobile = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100))
    # 订单状态 1-待支付，2-进行中，3-已完成，0-已关闭
    status = db.Column(db.Integer, default=1)
    # 快递单号
    express_id = db.Column(db.String(100), nullable=True)
    # 东8区时间
    time_utc_8 = datetime.now().astimezone(timezone(timedelta(hours=8)))
    created_at = db.Column(db.DateTime, nullable=False, default=time_utc_8)

    def __repr__(self):
        return '<订单编号 %r> <姓名 %r>' % (self.id, self.buyer)
    
