from dmsales import DMSalesAPI

import pytest

@pytest.fixture
def test_dmsales_api():
    api = DMSalesAPI(api_key='test123', test=True)
    return api
