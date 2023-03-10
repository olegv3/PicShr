from app.models import db, Comment, environment, SCHEMA

def seed_comments():
    comment1 = Comment(
        user_id=1, image_id=1, comment="Wow! I love this photo!"
    )
    comment2 = Comment(
        user_id=2, image_id=1, comment="Love this photo"
    )
    comment3 = Comment(
        user_id=3, image_id=1, comment="This is a great photo"
    )

    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)

    db.session.commit()

def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE TABLE {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM comments")

    db.session.commit()
