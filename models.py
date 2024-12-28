from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bid(db.Model):
    __tablename__ = 'bids'
    id = db.Column(db.Integer(), primary_key=True)
    amount = db.Column(db.Integer(), nullable=False, default=0)
    itemId = db.Column(db.Integer(), db.ForeignKey('items.id'), nullable=True, default=None)

    def __repr__(self):
        return f"<Image {self.image}>"

    
class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer(), primary_key=True)
    image = db.Column(db.LargeBinary())
    itemId = db.Column(db.Integer(), db.ForeignKey('items.id'), nullable=True, default=None)

    def __repr__(self):
        return f"<Image {self.image}>"
    
class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    category = db.Column(db.String())
    buyingPrice = db.Column(db.Integer())
    bidPrice = db.Column(db.Integer())
    quantity = db.Column(db.Integer())
    userId = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=True, default=None)

    def __repr__(self):
        return f"<Item {self.name}, price {self.buyingPrice}>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "buyingPrice": self.buyingPrice,
            "bidPrice": self.bidPrice,
            "quantity": self.quantity,
            "userId": self.userId
        }

class user(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    email = db.Column(db.String(), nullable=True, default=None)
    phone = db.Column(db.String(), unique=True, nullable=False, default=None)
    #items = db.relationship('Item', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.username}, phone: {self.phone}>"