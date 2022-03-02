from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.connections import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'<User(id={self.id}, name="{self.name}")>'


class Permission(Base):
    __tablename__ = 'permission'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'<User(id={self.id}, name="{self.name}")>'


class UserPermission(Base):
    __tablename__ = 'user_permission'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    permission_id = Column(Integer, ForeignKey('permission.id'))
