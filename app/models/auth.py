from flask_login import UserMixin

import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app import db, login

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(sa.Integer(), primary_key=True)
    username: Mapped[str] = mapped_column(sa.String(64), unique=True, nullable=False)
    display_name: Mapped[str] = mapped_column(sa.String(64))
    email: Mapped[str] = mapped_column(sa.String(256), unique=True)
    password_hash: Mapped[str] = mapped_column(sa.String(256))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User #{self.id} - {self.display_name or self.username} - {self.email}>"
    
@login.user_loader
def load_user(id: str) -> User:
    return User.query.get(id)