import pytest as pytest
import pytest_mock as pytest_mock
import pandas as pd
import os as os
from unittest import mock
import unittest as unittest

import main, users, user_status


@pytest.mark.parametrize(
                         "status_id, user_id, status_text",
                         [
                             ("evmiles97_00001","evmiles97","Code is finally compiling"),
                             ("dave03_00001","dave03","Sunny in Seattle this morning"),
                         ]
                        )
def test_add_status(status_id, user_id, status_text):
    status_collection = user_status.UserStatusCollection()
    new_status = user_status.UserStatus(status_id, user_id, status_text)
    assert status_id not in status_collection.database

    status_collection.database[status_id] = new_status
    
    assert status_id in status_collection.database


@pytest.mark.parametrize(
                         "status_id, user_id, status_text, new_status_text",
                         [
                             ("evmiles97_00001","evmiles97","Code is finally compiling","Code compiled"),
                             ("dave03_00001","dave03","Sunny in Seattle this morning", "Have you seen the forecast?"),
                         ]
                        )
def test_modify_status(status_id, user_id, status_text, new_status_text):
    status_collection = user_status.UserStatusCollection()
    new_status = user_status.UserStatus(status_id, user_id, status_text)
    status_collection.database[status_id] = new_status
    
    assert status_id in status_collection.database

    status_collection.modify_status(status_id, user_id, new_status_text)
    
    assert new_status_text in status_collection.database[status_id].status_text

@pytest.mark.parametrize(
                         "status_id, user_id, status_text",
                         [
                             ("evmiles97_00001","evmiles97","Code is finally compiling"),
                             ("dave03_00001","dave03","Sunny in Seattle this morning"),
                         ]
                        )
def test_delete_status(status_id, user_id, status_text):
    status_collection = user_status.UserStatusCollection()
    new_status = user_status.UserStatus(status_id, user_id, status_text)
    status_collection.database[status_id] = new_status
    status_collection.delete_status(status_id)

    assert status_id not in status_collection.database

@pytest.mark.parametrize(
                         "status_id, user_id, status_text",
                         [
                             ("evmiles97_00001","evmiles97","Code is finally compiling"),
                             ("dave03_00001","dave03","Sunny in Seattle this morning"),
                         ]
                        )
def test_search_status(status_id, user_id, status_text):
    status_collection = user_status.UserStatusCollection()
    new_status = user_status.UserStatus(status_id, user_id, status_text)
    
    assert status_collection.search_status(status_id).user_id is None
    assert status_collection.search_status(status_id).status_id is None
    assert status_collection.search_status(status_id).status_text is None

    status_collection.database[status_id] = new_status

    assert status_collection.search_status(status_id).user_id is not None
    assert status_collection.search_status(status_id).status_id is not None
    assert status_collection.search_status(status_id).status_text is not None   


@pytest.mark.parametrize(
                         "user_id, email, user_name, user_last_name",
                         [
                             ("evmiles97","eve.miles@uw.edu","Eve","Miles"),
                             ("dave03","david.yuen@gmail.com","David","Yuen"),
                         ]
                        )
def test_add_user(user_id, email, user_name, user_last_name):
    user_collection = users.UserCollection()
    new_user = users.Users(user_id, email, user_name, user_last_name)
    assert user_id not in user_collection.database

    user_collection.database[user_id] = new_user
    
    assert user_id in user_collection.database

@pytest.mark.parametrize(
                         "user_id, email, user_name, user_last_name, new_email",
                         [
                             ("evmiles97","eve.miles@uw.edu","Eve","Miles","eve.miles@live.com"),
                             ("dave03","david.yuen@gmail.com","David","Yuen","david.yuen@gmail.net"),
                         ]
                        )
def test_modify_user(user_id, email, user_name, user_last_name, new_email):
    user_collection = users.UserCollection()
    new_user = users.Users(user_id, email, user_name, user_last_name)
    user_collection.database[user_id] = new_user
    
    assert user_id in user_collection.database

    user_collection.modify_user(user_id, new_email, user_name, user_last_name)
    
    assert new_email in user_collection.database[user_id].email

@pytest.mark.parametrize(
                         "user_id, email, user_name, user_last_name",
                         [
                             ("evmiles97","eve.miles@uw.edu","Eve","Miles"),
                             ("dave03","david.yuen@gmail.com","David","Yuen"),
                         ]
                        )
def test_delete_user(user_id, email, user_name, user_last_name):
    user_collection = users.UserCollection()
    new_user = users.Users(user_id, email, user_name, user_last_name)
    user_collection.database[user_id] = new_user
    user_collection.delete_user(user_id)

    assert user_id not in user_collection.database

@pytest.mark.parametrize(
                         "user_id, email, user_name, user_last_name",
                         [
                             ("evmiles97","eve.miles@uw.edu","Eve","Miles"),
                             ("dave03","david.yuen@gmail.com","David","Yuen"),
                         ]
                        )
def test_search_user(user_id, email, user_name, user_last_name):
    user_collection = users.UserCollection()
    new_user = users.Users(user_id, email, user_name, user_last_name)
    
    assert user_collection.search_user(user_id).user_id is None
    assert user_collection.search_user(user_id).user_name is None
    assert user_collection.search_user(user_id).user_last_name is None
    assert user_collection.search_user(user_id).email is None

    user_collection.database[user_id] = new_user

    assert user_collection.search_user(user_id).user_id is not None
    assert user_collection.search_user(user_id).user_name is not None
    assert user_collection.search_user(user_id).user_last_name is not None
    assert user_collection.search_user(user_id).email is not None 


def test_init_user_collection():
    new_usercollection = main.init_user_collection()
    assert new_usercollection is not None

def test_init_status_collection():
    new_statuscollection = main.init_user_collection()
    assert new_statuscollection is not None

@pytest.fixture
def usercollection_init():
    user_collection_ex = users.UserCollection()
    new_user = users.Users("evmiles97","eve.miles@uw.edu","Eve","Miles")
    user_collection_ex.database["evmiles97"] = new_user
    new_user = users.Users("dave03","david.yuen@gmail.com","David","Yuen")
    user_collection_ex.database["dave03"] = new_user

    return user_collection_ex

@pytest.mark.usefixtures("usercollection_init")
def test_load_users(filename, user_collection):
    users_df = main.load_users(filename, user_collection)
    if len(users_df) > 0:
        users_df = users_df.drop_duplicates(subset=['user_id'])
        users_df_duplicated = users_df[users_df.duplicated()]
        assert users_df_duplicated.empty
        assert users_df
    else:
        assert not users_df
    
@pytest.mark.parametrize(
                         "status_id, user_id, status_text",
                         [
                             ("evmiles97_00001","evmiles97","Code is finally compiling"),
                             ("dave03_00001","dave03","Sunny in Seattle this morning")
                         ]
                        )


@pytest.fixture
def statuscollection_init():
    status_collection_ex = users.UserCollection()
    new_status = user_status.UserStatus("evmiles97_00001","evmiles97","Code is finally compiling")
    status_collection_ex.database["evmiles97"] = new_status
    new_status = user_status.UserStatus("dave03_00001","dave03","Sunny in Seattle this morning")
    status_collection_ex.database["dave03"] = new_status

    return status_collection_ex

@pytest.mark.parametrize(
                         "filename, user_collection",
                         [
                             ("data.csv"),
                             ("dave03.json")
                         ]
                        )
@pytest.mark.usefixtures("statuscollection_init")
def test_load_status_updates_filenotfounderror(filename):
    with pytest.raises(FileNotFoundError):
        user_collection_ex = statuscollection_init
        main.load_status_updates(filename, user_collection_ex)

@pytest.mark.parametrize(
                         "filename, user_collection",
                         [
                             ("user_status.csv")
                         ]
                        )
@pytest.mark.usefixtures("statuscollection_init")
def test_load_status_updates_duplicates(filename):
    status_collection_ex = statuscollection_init
    new_status_collection = main.load_status_updates(filename, status_collection_ex)
    assert len(new_status_collection) == len(status_collection_ex)


@pytest.mark.parametrize(
                         "user_id, email, user_name, user_last_name",
                         [
                             ("clough99","c.miles@uw.edu","Connor","Lough"),
                             ("yoma48","yoyo.ma@gmail.com","YoYo","Ma"),
                         ]
                        )
@pytest.mark.usefixtures("usercollection_init")
def test_add_user(user_id, email, user_name, user_last_name, usercollection_init):
    new_users = main.add_user(user_id, email, user_name, user_last_name, usercollection_init)
    assert user_id in new_users.database
