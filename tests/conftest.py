from pathlib import Path

import pytest

from dmsales import DMSalesAPI

@pytest.fixture
def test_dmsales_api():
    api = DMSalesAPI(api_key='test123', test=True)
    return api

@pytest.fixture
def tests_data_path():
    return Path('tests/data')