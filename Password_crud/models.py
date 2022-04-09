from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PasswordModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    password_id = db.Column(db.Integer(), unique=True)
    site = db.Column(db.String())
    login = db.Column(db.Integer())
    password = db.Column(db.String(80))

    def __init__(self, password_id, site, login, password):
        self.password_id = password_id
        self.site = site
        self.login = login
        self.password = password

    def __repr__(self):
        return f"{self.password_id} - {self.site} - {self.login} - {self.password}"
