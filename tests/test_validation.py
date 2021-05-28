import json

import responses
import pytest

@pytest.fixture
def validation_report(tests_data_path):
    validation_file_path = tests_data_path / 'validation_report.json'
    with open(validation_file_path, 'r') as f:
        content = f.read()
        return json.loads(content)

@responses.activate
def test_validation_start(test_dmsales_api):
    responses.add(
        method='POST',
        url=test_dmsales_api.api_host + '/api/validation/start',
        status=201,
        json={'task_id': '19a05d9d-27be-4a90-b7d8-29ced5bbadf9'}
    )

    assert test_dmsales_api.validation_start(
        name='Jan',
        phone='505684275',
        postal_code='90-001',
        email='jan.kowalski@dmsales.com'
    ) == {'task_id': '19a05d9d-27be-4a90-b7d8-29ced5bbadf9'}

@responses.activate
def test_validation_report(test_dmsales_api, validation_report):
    responses.add(
        method='GET',
        url=test_dmsales_api.api_host + '/api/validation/report',
        status=200,
        json = validation_report
    )

    assert test_dmsales_api.validation_report(
        task_id='19a05d9d-27be-4a90-b7d8-29ced5bbadf9'
    ) == validation_report

    