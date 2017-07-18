# -*- coding: utf-8 -*-
"""
API helpers for SQLAlchemy.
"""
# Standard Library
from functools import partial

# Third-Party
from sqlalchemy import Column
from sqlalchemy import Integer

# Shorcuts for Primary Key columns
PK_Column = partial(Column, primary_key=True)
PK_Int_Column = partial(Column, Integer, primary_key=True)
PK_NN_AI_Int_Column = partial(
    Column,
    Integer,
    primary_key=True,
    nullable=False,
    autoincrement='auto',
)
