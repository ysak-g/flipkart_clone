from ..models.CommentModel import CommentModel, db
from flask import request
import json


def add_comment():
    comment = request.json['comment']
    up_votes = request.json['up_votes']
    down_votes = request.json['down_votes']
    user_id = request.json['user_id']
    comment = CommentModel(
        comment = comment,
        up_votes = up_votes,
        down_votes = down_votes,
        user_id = user_id
    )
    db.session.add(comment)
    db.session.commit()
    return True
