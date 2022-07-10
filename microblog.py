from app import app, db
from app.models import User, Post

# you can now call 'flask shell's and access db, User and Post straight away
@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post
    }
