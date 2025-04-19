# Test Configuration

# Test Environment Settings
TEST_ENV = {
    'base_url': 'http://localhost:5000',
    'timeout': 30,
    'retry_count': 3
}

# Database Test Settings
DB_TEST_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'test_db',
    'user': 'test_user',
    'password': 'test_password'
}

# API Test Settings
API_TEST_CONFIG = {
    'headers': {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    },
    'timeout': 10
}

# Test Categories
TEST_CATEGORIES = [
    'unit',
    'integration',
    'performance',
    'security'
] 