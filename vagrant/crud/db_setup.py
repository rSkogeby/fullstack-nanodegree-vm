import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

def main():
    pass


if __name__ == "__main__":
    main()

engine = create_engine(
    'sqlite://restaurantmenu.db'
)