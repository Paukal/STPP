from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


@dataclass
class Users(Base):
	__tablename__ = "users"

	id: Integer.python_type = Column(Integer, primary_key=True, autoincrement=True)
	role: SmallInteger.python_type = Column(SmallInteger, nullable=False)
	login: Text.python_type = Column(Text, nullable=False, unique=True)
	name: Text.python_type = Column(Text, nullable=False)
	# passhash is excluded from dataclass autojson
	passhash = Column(Text, nullable=False)

	LOGIN_LENGTH_MIN = 1
	LOGIN_LENGTH_MAX = 31
	NAME_LENGTH_MIN = 1
	NAME_LENGTH_MAX = 15
	PASSWORD_LENGTH_MIN = 8
	PASSWORD_LENGTH_MAX = 255


@dataclass
class Rooms(Base):
	__tablename__ = "rooms"

	id: Integer.python_type = Column(Integer, primary_key=True)
	title: Text.python_type = Column(Text, nullable=False)


@dataclass
class RoomsUsers(Base):
	__tablename__ = "rooms_users"

	room_id: Integer.python_type = Column(ForeignKey(Rooms.id), primary_key=True)
	user_id: Integer.python_type = Column(ForeignKey(Users.id), primary_key=True)


@dataclass
class Posts(Base):
	__tablename__ = "posts"

	id: Integer.python_type = Column(Integer, primary_key=True)
	room_id: Integer.python_type = Column(ForeignKey(Rooms.id), nullable=False)
	date: DateTime.python_type = Column(DateTime, nullable=False)
	content: Text.python_type = Column(Text, nullable=False)
