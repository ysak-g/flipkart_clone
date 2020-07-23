from ..models.CommentModel import CommentModel, CommentVoteModel, db
from flask import request
import json


def add_comment():
    comment = request.json['comment']
    user_id = request.json['user_id']
    product_id = request.json['product_id']
    comment = CommentModel(
        comment = comment,
        user_id = user_id,
        product_id = product_id
    )
    db.session.add(comment)
    db.session.commit()
    return True


def add_vote():
    comment_id = request.json['comment_id']
    up_votes = request.json['up_votes']
    down_votes = request.json['down_votes']
    vote = CommentVoteModel(
        comment_id = comment_id,
        up_votes = up_votes,
        down_votes = down_votes
    )
    db.session.add(vote)
    db.session.commit()
    return True


def view_comments():
    product_id = request.headers.get('product_id')
    comment_data = db.engine.execute(
        "SELECT comments.id,comment,name FROM comments JOIN users ON \
            comments.user_id=users.id WHERE product_id=%d" % (int(product_id))
    )

    query_comment = CommentModel.query.filter_by(product_id=product_id).first()
    comment_id = query_comment.id

    up_votes = db.engine.execute(
        "select count(*) from comment_votes where comment_id={0} and up_votes=1"\
            .format(comment_id)
    )

    down_votes = db.engine.execute(
        "select count(*) from comment_votes where comment_id={0} and down_votes=1"\
            .format(comment_id)
    )

    return comment_data, up_votes, down_votes
