import datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app import db

if TYPE_CHECKING:
    from app.models.auth import User

class Article(db.Model):
    __tablename__ = "article"

    id: Mapped[int] = mapped_column(sa.Integer(), primary_key=True)
    title: Mapped[str] = mapped_column(
        sa.String(255),
        nullable=False
    )
    slug: Mapped[str] = mapped_column(
        sa.String(255),
        unique=True,
        nullable=False
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        sa.DateTime(),
        nullable=False
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        sa.DateTime(),
        nullable=True
    )
    content: Mapped[str] = mapped_column(
        sa.Text(),
        nullable=True
    )
 
    author_id: Mapped[int] = mapped_column(
        sa.ForeignKey("user.id"),
        nullable=False
    )
    author: Mapped["User"] = relationship(back_populates="articles")

    def __repr__(self):
        return f"<Article #{self.id} - {self.title}>"