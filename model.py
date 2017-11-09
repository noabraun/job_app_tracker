"""Models and database functions for Bills Project."""
from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()

##############################################################################
# Model definitions

class Job(db.Model):
    """Job metadata"""

    __tablename__ = "jobs"

    job_id =  db.Column(db.Integer, autoincrement=True, primary_key=True)
    job_title = db.Column(db.Text, nullable=False)
    job_description = db.Column(db.Text, nullable=True)
    location = db.Column(db.Text, nullable=True) 
    notes = db.Column(db.Text, nullable=True) 
    link = db.Column(db.Text, nullable=True) 

    users = db.relationship("User", secondary='applications', backref='jobs')


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Job job_id=%s job_title=%s job_description=%s location=%s notes=%s link=%s>" % (self.job_id, 
                                                                                self.job_title, 
                                                                                self.job_description,
                                                                                self.location, 
                                                                                self.notes,
                                                                                self.link)


class Company(db.Model):
    """Company metadata"""

    __tablename__ = "companies"

    company_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.Text)
    website = db.Column(db.Text)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Company company_id=%s name=%s description=%s website=%s>" % (self.company_id, 
                                                                              self.name, 
                                                                              self.description, 
                                                                              self.website)

class User(db.Model):
    """User metadata"""

    __tablename__ = "companies"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    location = db.Column(db.String(64))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s name=%s email=%s location=%s>" % (self.user_id, self.name, 
                                                                   self.email, self.location)


class Application(db.Model):
    """Application metadata"""

    __tablename__ = "companies"

    application_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date_applied = db.Column(db.DateTime)
    job_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

    user = db.relationship('User', backref='applications')
    job = db.relationship('Job', backref='jobs')


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Application application_id=%s date_applied=%s job_id=%s user_id=%s>" % (self.application_id, 
                                                                                         self.date_applied, 
                                                                                         self.job_id, 
                                                                                         self.user_id)


class Status(db.Model):
    """Status metadata"""

    __tablename__ = "companies"

    status_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.String(128))
    application_id = db.Column(db.String(128))
    date = db.Column(db.String(64))
    notes = db.Column(db.Text)



    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User status_id=%s user_id=%s application_id=%s date=%s notes=%s>" % (self.status_id, 
                                                                                      self.user_id,
                                                                                      self.application_id, 
                                                                                      self.date, 
                                                                                      self.notes)

##############################################################################

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bills'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app

    connect_to_db(app)
    print "Connected to DB."