from flask import Blueprint
from ..services.comments_services import *
import json


comment = Blueprint('comment', __name__)

@comment.route('/')
def home():
    return "Welcome to comment page"


@comment.route('/add', methods=['POST'])
def new_comment():
    result = add_comment()
    if result:
        return json.dumps({
            "message": "Comment added successfully",
            "status": True
        })
    else:
       return json.dumps({
            "message": "Error while adding comment",
            "status": False
        })

@comment.route('/vote', methods=['POST'])
def voting():
    result = add_vote()
    if result:
        return json.dumps({
            "message": "Vote added successfully",
            "status": True
        })
    else:
        return json.dumps({
            "message": "Error while adding vote",
            "status": False
        })


@comment.route('/view', methods=['GET'])
def show_comments():
    comment, up_vote, down_vote = view_comments()
    output = {}

    for row in comment:
        output['comment'] = row['comment']
        output['user'] = row['name']

    for row in up_vote:
        output['up_vote'] = row[0]

    for row in down_vote:
        output['down_vote'] = row[0]

    return json.dumps({
        "message": output,
        "status": True
    })
