import json
from pathlib import Path

import responses
import pytest


@pytest.fixture
def project_list_data():
    tests_directory_path = Path('tests/data')
    file_path = tests_directory_path / 'project_list.json'
    with open(file_path, 'r') as file:
        data = file.read()
        return json.loads(data)

@responses.activate
def test_persons_list(test_dmsales_api, project_list_data):
    responses.add(
        method=responses.GET,
        url=test_dmsales_api.api_host + '/api/persons/list',
        status=200,
        json=project_list_data
    )

    assert test_dmsales_api.persons_list(
        page=1,
        limit=10,
        project_id='6fdeda41-89e5-41c3-a419-bca38b61b701'
    ) == project_list_data

