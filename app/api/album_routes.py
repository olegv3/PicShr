from flask import Blueprint, request
from flask_login import current_user, login_required
from app.models import db, Album, Image
from app.forms import AlbumForm


album_routes = Blueprint('albums',__name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

@album_routes.route("", methods=["POST"])
@login_required
def create_album():

    # create a new album

    form = AlbumForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        new_album = Album(user=current_user, name=form.data["name"], description=form.data["description"])
        db.session.add(new_album)
        images = form.data['images'].split(',')
        image_details = []
        [image_details.append(Image.query.get(int(image))) for image in images]
        [new_album.images.append(image) for image in image_details]
        db.session.commit()
        return new_album.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@album_routes.route("/user/<int:id>", methods=["GET"])
def get_users_albums(id):

    # get all albums for a user

    albums = Album.query.filter_by(user_id=id).all()
    return {album.id: album.to_dict() for album in albums}


@album_routes.route('/<int:id>', methods=['GET'])
def get_single_album(id):
    album = Album.query.get(id)
    return album.to_dict()

@album_routes.route("/<int:id>", methods=["PUT"])
@login_required
def edit_album_details(id):

    # edit album details

    album = Album.query.get((id))

    form = AlbumForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        name = form.data["name"]
        description = form.data['description']


        album.name = name
        album.description = description

        if(form.data['images'] != ''):
            images = form.data['images'].split(',')
            image_details = []
            [image_details.append(Image.query.get(int(image))) for image in images]
            [album.images.remove(image) for image in image_details]

        db.session.commit()

    return album.to_dict()


@album_routes.route("/<int:id>", methods=['DELETE'])
@login_required
def delete_album(id):

    # delete an album

    album = Album.query.get(id)
    db.session.delete(album)
    db.session.commit()
    return {'message': 'Delete Successful'}
