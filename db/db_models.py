from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base() 


class Curator(Base):
    __tablename__ = 'curators'
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_superuser = Column(Boolean, default=False)
    
    groups = relationship("Group", back_populates="curator")

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    curator_id = Column(Integer, ForeignKey('curators.id', ondelete='CASCADE'), nullable=False)
    name = Column(String, nullable=False) 
    semester = Column(Integer, nullable=False)
    institute_id = Column(Integer, ForeignKey('institutes.id', ondelete='CASCADE'), nullable=False)
    

    curator = relationship("Curator", back_populates="groups")
    students = relationship("Student", back_populates="group")

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey('groups.id', ondelete='CASCADE'), nullable=False)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    debts = Column(Integer, nullable=False, default=0)
    
    group = relationship("Group", back_populates="students")

class Institute(Base):
    __tablename__ = 'institutes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class ArchivedGroup(Base):
    __tablename__ = 'archived_groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    curator_id = Column(Integer, ForeignKey('curators.id', ondelete='CASCADE'), nullable=False)
    name = Column(String, nullable=False)
    semester = Column(Integer, nullable=False)
    institute_id = Column(Integer, ForeignKey('institutes.id', ondelete='CASCADE'), nullable=False)

class ArchivedStudent(Base):
    __tablename__ = 'archived_students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey('archived_groups.id', ondelete='CASCADE'), nullable=False)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    debts = Column(Integer, nullable=True)
    semester = Column(Integer, nullable=False)
