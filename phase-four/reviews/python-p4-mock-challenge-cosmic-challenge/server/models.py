from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)


class Planet(db.Model, SerializerMixin):
    __tablename__ = 'planets'

    serialize_rules = ('-missions',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    distance_from_earth = db.Column(db.Integer)
    nearest_star = db.Column(db.String)

    # Add relationship
    missions = db.relationship('Mission', back_populates='planet', cascade='all, delete-orphan')
    scientists = association_proxy('missions', 'scientist')
    # Add serialization rules


class Scientist(db.Model, SerializerMixin):
    __tablename__ = 'scientists'

    serialize_rules = ('-missions.scientist',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    field_of_study = db.Column(db.String, nullable=False)

    # Add relationship
    missions = db.relationship('Mission', back_populates='scientist', cascade='all, delete-orphan')
    planets = association_proxy('missions', 'planet')

    # Add serialization rules

    # Add validation
    @validates('name')
    def validates_name(self, key, new_name):
        if new_name:
            return new_name
        raise ValueError('Name must be included.')
    
    @validates('field_of_study')
    def validates_field(self, key, new_field):
        if new_field:
            return new_field
        raise ValueError('Field of Study must be included.')


class Mission(db.Model, SerializerMixin):
    __tablename__ = 'missions'

    serialize_rules = ('-planet.missions', '-scientist.missions',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    scientist_id = db.Column(db.Integer, db.ForeignKey('scientists.id'))

    # Add relationships
    planet = db.relationship('Planet', back_populates='missions')
    scientist = db.relationship('Scientist', back_populates='missions')

    # Add serialization rules

    # Add validation
    @validates('name')
    def validates_name(self, key, new_name):
        if new_name:
            return new_name
        raise ValueError('Name must be included.')

    @validates('planet_id')
    def validates_planet_id(self, key, new_planet_id):
        if new_planet_id:
            return new_planet_id
        raise ValueError('planet_id must be included.')
    
    @validates('scientist_id')
    def validates_scientist_id(self, key, new_scientist_id):
        if new_scientist_id:
            return new_scientist_id
        raise ValueError('scientist_id must be included.')


# add any models you may need.
