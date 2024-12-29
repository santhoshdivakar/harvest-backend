from models import db, Item, Image
import PIL
from io import BytesIO

def get_all_items():
    return [item.to_dict() for item in Item.query.all()]

def get_item(item_id):
    item = Item.query.get(item_id)
    if item:
        return item
    return None

def create_item(request):
    item = Item(
        name=request.form.get('name'),
        description=request.form.get('description'),
        category=request.form.get('category'),
        buyingPrice=request.form.get('buyingPrice'),
        bidPrice=request.form.get('bidPrice'),
        quantity=request.form.get('quantity')
    )
    db.session.add(item)
    db.session.commit()

    photos = request.files.getlist('photos')

    for photo in photos:
        image = PIL.Image.open(photo)
        image.thumbnail((500, 500))
        image_io = BytesIO()
        image.save(image_io, format='JPEG')
        image_content = image_io.getvalue()
        image = Image(image=image_content, itemId=item.id)
        db.session.add(image)

    db.session.commit()
    return item.id

def delete_item(item_id):
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return True
    return False
