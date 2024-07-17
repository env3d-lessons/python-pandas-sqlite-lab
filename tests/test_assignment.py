import pathlib
import pytest
import os
import sys
import re
import sqlite3
import pandas

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)
import main


def test_exists_main_py():
    assert pathlib.Path('main.py').is_file()

def test_title_basics_tsv():
    with open('./main.py') as f:
        assert 'title.basics.tsv' in f.read(), "Must use title.basics.tsv in your code"

def test_read_csv():
    with open('./main.py') as f:
        assert 'read_csv' in f.read(), "Must use pandas.read_csv in your code"

def test_chunksize():
    with open('./main.py') as f:
        assert 'chunksize' in f.read(), "Must use chunksize in your code"

def test_quote_char():
    with open('./main.py') as f:
        assert 'quoting' in f.read(), "Ignore quoute character when calling read_csv: i.e. quoting=csv.QUOTE_NONE"


fake_data="""tconst\ttitleType\tprimaryTitle\toriginalTitle\tisAdult\tstartYear\tendYear\truntimeMinutes\tgenres
tt0000001\tshort\tCarmencita\tCarmencita\t0\t2000\t\\N\t1\tDocumentary,Short
tt0000002\tshort\tCarmencita\tCarmencita\t0\t2000\t\\N\t2\tDocumentary,Short
tt0000003\tshort\tCarmencita\tCarmencita\t0\t2000\t\\N\t3\tDocumentary,Short
tt0000004\tshort\tCarmencita\tCarmencita\t0\t2000\t\\N\t4\tDocumentary,Short
tt0000005\tshort\tCarmencita\tCarmencita\t0\t2000\t\\N\t5\tDocumentary,Short
tt0000006\tmovie\tCarmencita\tCarmencita\t0\t1999\t\\N\t2\tDocumentary,Short
tt0000006\tmovie\tCarmencita\tCarmencita\t0\t1999\t\\N\t4\tDocumentary,Short
tt0000006\tmovie\tCarmencita\tCarmencita\t0\t1999\t\\N\t6\tDocumentary,Short
"""

def test_calculate_average_runtime_1(mocker):
    mock_open = mocker.patch('builtins.open', mocker.mock_open(read_data=fake_data))    
    assert main.calculate_average_runtime('short', 2000) == 3
    
def test_calculate_average_runtime_2(mocker):
    mock_open = mocker.patch('builtins.open', mocker.mock_open(read_data=fake_data))    
    assert main.calculate_average_runtime('movie', 1999) == 4

@pytest.fixture
def write_to_sql(mocker):
    mock_open = mocker.patch('builtins.open', mocker.mock_open(read_data=fake_data))    
    mocker.patch('sqlite3.connect', return_value=sqlite3.connect('_test.db'))
    main.write_to_sqlite()    
    yield None
    os.popen('rm _test.db')

def test_valid_db(write_to_sql):
    assert pathlib.Path('./_test.db').is_file()
    assert '8' in os.popen("sqlite3 _test.db  'select count(*)  from titles'").read()

def test_calculate_average_db(write_to_sql, mocker):
    mocker.patch('sqlite3.connect', return_value=sqlite3.connect('_test.db'))
    assert main.calculate_average_runtime_db('movie', 1999) == 4
    assert main.calculate_average_runtime_db('short', 2000) == 3

    


