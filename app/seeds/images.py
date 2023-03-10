from app.models import db, Image, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_images():
    image1 = Image(
        user_id=1, url="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg", title='Photo 1')
    image2 = Image(
        user_id=2, url="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg", title='Photo 2')
    image3 = Image(
        user_id=3, url="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg", title='Photo 3')

    db.session.add(image1)
    db.session.add(image2)
    db.session.add(image3)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the images table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM images")

    db.session.commit()
