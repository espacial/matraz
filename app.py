import os

from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
from flask.ext.sqlalchemy import SQLAlchemy

from contact import get_contact
from utils import get_repo_info


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
socketio = SocketIO(app)


@app.route('/<owner>/<repo>')
def index(owner, repo):
    return render_template('form.html', owner=owner, repo=repo)


@socketio.on('get info', namespace="/badge")
def get_info(message):
    # Message contains repo, owner, token keys
    repo_info = get_repo_info(message["owner"], message["repo"])
    return_message = {
        "contact": get_contact(message["owner"], repo_info)
    }
    emit('info', return_message)


class Owner(db.Model):
    __tablename__ = 'owner'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    repos = db.relationship('Repo', backref='owner')

    def __init__(self, name):
        self.name = name


class Repo(db.Model):
    __tablename__ = 'repo'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    name = db.Column(db.String())
    doi = db.Column(db.String())
    contact_info = db.Column(db.String())
    license = db.Column(db.Enum("agpl-3.0", "apache-2.0", "artistic-2.0",
                                "bsd-2-clause", "bsd-3-clause", "cc0-1.0",
                                "epl-1.0", "gpl-2.0", "gpl-3.0", "isc",
                                "lgpl-2.1", "lgpl-3.0", "mit", "mpl-2.0",
                                "unlicense", name="license_type"))

    def __init__(self, name, doi, contact_info, license):
        self.name = name
        self.doi = doi
        self.contact_info = contact_info
        self.license = license


if __name__ == '__main__':
    socketio.run(app);
