import pytest
from tests_lib.common.database_connection import DatabaseConnection
from tests_lib.database.config.database_config import DatabaseConfig
from tests_lib.web_ui.helpers.log_manager import LogManager


class TestProvidedQueries:
    """Test class for validating provided database queries."""
    
    @pytest.fixture(autouse=True)
    def setup_logger(self, request):
        """Setup method to initialize the logger."""
        log_manager = LogManager()
        logger = log_manager.get_logger(DatabaseConfig.LOGGER_NAME, DatabaseConfig.LOG_LEVEL)
        test_name = f"{request.cls.__name__}.{request.node.name}"
        logger.info(f"=== Starting test: {test_name} ===")
        yield logger
        logger.info(f"=== Completed test: {test_name} ===\n")
        for handler in logger.handlers[:]:
            handler.close()
            logger.removeHandler(handler)

    @pytest.fixture(scope="session")
    def database_connection(self):
        """Database connection fixture."""
        try:
            with DatabaseConnection.get_connection() as connection:
                yield connection
        except Exception as e:
            pytest.fail(f"Failed to establish database connection: {str(e)}")

    @pytest.mark.parametrize("query_data", DatabaseConfig.QUERIES)
    def test_provided_queries(self, database_connection, query_data, setup_logger):
        """Test database queries against expected results."""
        logger = setup_logger
        try:
            with database_connection.cursor() as cursor:
                cursor.execute(query_data["query"])
                actual_results = cursor.fetchall()
                expected_results = [tuple(row) for row in query_data["expected_results"]]
                
                assert actual_results == expected_results, (
                    f"Query results don't match.\n"
                    f"Expected: {expected_results}\n"
                    f"Actual: {actual_results}"
                )
                logger.info("Query execution successful")
                
        except Exception as e:
            logger.error(f"Query execution failed: {str(e)}")
            raise