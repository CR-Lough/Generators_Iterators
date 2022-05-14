import os as os
import pytest as pytest
import pytest_mock as pytest_mock
import pandas as pd
from peewee import *
from unittest import mock
from pytest_mock_resources import create_sqlite_fixture, Statements

import main, users, user_status, socialnetwork_model

statements = Statements(
    """
    CREATE TABLE UsersTable(
      user_id serial PRIMARY KEY,
      user_name VARCHAR (30) UNIQUE NOT NULL,
      user_last_name VARCHAR (100) NOT NULL,
      user_email VARCHAR (50) NOT NULL
    );
    """,
    """
    CREATE TABLE StatusTable(
      status_id VARCHAR (30) UNIQUE NOT NULL,
      user_id VARCHAR (100) NOT NULL,
      status_text VARCHAR (100) NOT NULL
    );
    """,
    """
    INSERT INTO UsersTable VALUES ('Brittaney.Gentry86',
      'Brittaney',
      'Gentry',
      'Brittaney.Gentry86@goodmail.com'
    );
    """,
)

sqlite = create_sqlite_fixture(
    statements,
)

def test_search_user(sqlite):
    execute = sqlite.execute("SELECT user_id FROM UsersTable")

    result = sorted([row[0] for row in execute])
    assert ["Brittaney.Gentry86"] == result



