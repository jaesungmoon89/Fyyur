import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from sqlalchemy.sql import text, or_, and_
from sqlalchemy.dialects import postgresql

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
#to be removed later
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
db = SQLAlchemy(app)

migrate = Migrate(app, db)

Show = db.Table('Show',
    db.Column('start_time',db.DateTime),
    db.Column('artist_id',db.Integer, db.ForeignKey('Artist.id'), primary_key=True),
    db.Column('venue_id',db.Integer, db.ForeignKey('Venue.id'), primary_key=True)
)

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(postgresql.ARRAY(db.String(120)))
    #genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    artists = db.relationship('Artist', secondary=Show, backref=db.backref('venues', lazy=True))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    #genres = db.Column(db.String(120))
    genres = db.Column(postgresql.ARRAY(db.String(120)))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
