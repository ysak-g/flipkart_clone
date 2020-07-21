from flask import Blueprint
from ..services.comments_services import add_comment


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
