from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.tag import Tag
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)


@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags = tags)



@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template("tags/new.html")



@tags_blueprint.route("/tags", methods=["POST"])
def create_tag():
    name = request.form["name"]
    new_tag = Tag(name)
    tag_repository.save(new_tag)
    return redirect("/tags")



@tags_blueprint.route("/tags/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template('tags/edit.html', tag=tag)
