from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    serialize_rules = ('-comments.post',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)

    # comments = db.relationship('Comment', backref='post')
    comments = db.relationship('Comment', back_populates='post')
    users = association_proxy('comments', 'user')

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-comments.user',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer)

    __table_args__ = (
        db.CheckConstraint('age > 12', name='old_enough'),
    )

    @validates('name')
    def validates_name(self, key, new_name):
        if len(new_name) > 2:
            return new_name
        raise ValueError('Name must be greater than 2 characters.')

    comments = db.relationship('Comment', back_populates='user')
    commented_posts = association_proxy('comments', 'post')

class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'

    serialize_rules = ('-post.comments', '-post_id', '-user.comments','-user_id')

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    post = db.relationship('Post', back_populates='comments')
    user = db.relationship('User', back_populates='comments')