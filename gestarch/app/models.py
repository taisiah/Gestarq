# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class Usuario(UserMixin, db.Model):
    """
    Create an Usuario table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True)
    password_hash = db.Column(db.String(128))
    nome = db.Column(db.String(120), index=True)
    email = db.Column(db.String(60), index=True, unique=True)
    telefone = db.Column(db.String(11), index=True, unique=True)
    is_admin = db.Column(db.Boolean, default=False)
    
    
    #department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    #role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

