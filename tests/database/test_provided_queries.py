import pytest
from tests_lib.helpers.json_loader import JSONLoader
from tests_lib.common.database_connection import DatabaseConnection

@pytest.fixture(scope="session")
def database_connection_setup():
    """Setup and tear down the database connection."""
    with DatabaseConnection.get_connection() as connection:
        yield connection

@pytest.fixture()
def cursor(database_connection_setup):
    with database_connection_setup.cursor() as cursor:
        yield cursor

@pytest.mark.parametrize(
    "test_database_queries",
    JSONLoader().load_data("test_data_database.json", "queries"),
)
def test_provided_queries(cursor, test_database_queries):
    cursor.execute(test_database_queries["query"])
    actual_results = cursor.fetchall()
    expected_results = [tuple(row) for row in test_database_queries["expected_results"]]

    assert actual_results == expected_results
