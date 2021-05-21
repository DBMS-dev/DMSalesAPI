import json
from pathlib import Path

import responses
import pytest

@pytest.fixture
def person():
    test_data_path = Path('tests/data')
    person_file_path = test_data_path / 'person.json'
    with open(person_file_path, 'r') as f:
        content = f.read()
        return json.loads(content)


@responses.activate
def test_add_person(test_dmsales_api, person):
    responses.add(
        method='POST',
        url=test_dmsales_api.api_host + '/api/persons/upsert',
        status=201,
        json={'code': 201, 'message': 'Created',
              'details': 'Person added successfully.'}
    )

    assert test_dmsales_api.add_person(
        id='123',
        project_id='1234-898-000-999',
        person_dict=person
    ) == {'code': 201, 'message': 'Created', 'details': 'Person added successfully.'}
    assert len(responses.calls) == 1

@responses.activate
def test_update_person(test_dmsales_api, person):
    responses.add(
        method='PUT',
        url=test_dmsales_api.api_host + '/api/persons/upsert',
        status=201,
        json={'code': 201, 'message': 'Created', 'details': 'Person added successfully.'}
    )

    assert test_dmsales_api.update_person(
        id='123',
        project_id='1234-898-000-999',
        person_dict=person
    ) == {'code': 201, 'message': 'Created', 'details': 'Person added successfully.'}
    assert len(responses.calls) == 1

@responses.activate
def test_init_call(test_dmsales_api):
    responses.add(
        method=responses.POST,
        url=test_dmsales_api.api_host + '/api/persons/init-call',
        status=200,
        json={'call_id': 'e46d2484-fe89-1a37-af6f-2c3612773sf4'}
    )

    assert test_dmsales_api.init_call(project_id='1234', base_key='test1') == {'call_id': 'e46d2484-fe89-1a37-af6f-2c3612773sf4'}
    assert len(responses.calls) == 1
    assert responses.calls[0].request.params == {
        'project_id': '1234',
        'base_key': 'test1'
    }

@responses.activate
def test_check_call(test_dmsales_api):
    responses.add(
        method=responses.GET,
        url=test_dmsales_api.api_host + '/api/persons/check-call',
        status=200,
        json={'outcome': 'failed', 'status': 'failed', 'duration': None}
    )

    assert test_dmsales_api.check_call(project_id='1234', call_id='e46d2484-fe89-1a37-af6f-2c3612773sf4') == {'outcome': 'failed', 'status': 'failed', 'duration': None}
    assert len(responses.calls) == 1
    assert responses.calls[0].request.params == {
        'project_id': '1234',
        'call_id': 'e46d2484-fe89-1a37-af6f-2c3612773sf4'
    }
