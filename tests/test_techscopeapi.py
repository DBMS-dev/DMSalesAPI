import json
from pathlib import Path

import responses
import pytest

@pytest.fixture
def techscopeapi_result(tests_data_path):
    result_file_path = tests_data_path / 'techscopeapi_result.json'
    with open(result_file_path, 'r') as f:
        file_content = f.read()
        return json.loads(file_content)

@responses.activate
def test_start_techscopeapi(test_dmsales_api):
    responses.add(
        method=responses.POST,
        url=test_dmsales_api.api_host + '/api/techscopeapi/generate',
        status=201,
        json={'id': '4189397e-51fe-432d-9c4f-962642f27f9d'}
    )

    assert test_dmsales_api.start_techscopeapi(www='empik.com') == {'id': '4189397e-51fe-432d-9c4f-962642f27f9d'}
    assert len(responses.calls) == 1
    assert responses.calls[0].request.params == {'www': 'empik.com'}

@responses.activate
def test_techscopeapi_result(test_dmsales_api, techscopeapi_result):
    responses.add(
        method=responses.GET,
        url=test_dmsales_api.api_host + '/api/techscopeapi/result',
        status=200,
        json=techscopeapi_result
    )


    assert test_dmsales_api.techscopeapi_result(task_id='4189397e-51fe-432d-9c4f-962642f27f9d') == techscopeapi_result
    assert len(responses.calls) == 1
    assert responses.calls[0].request.params == {'task_id': '4189397e-51fe-432d-9c4f-962642f27f9d'}