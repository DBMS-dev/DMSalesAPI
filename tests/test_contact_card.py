import json

import responses
import pytest

@pytest.fixture
def contact_details(tests_data_path):
    details_file_path = tests_data_path / 'contact_details.json'
    with open(details_file_path, 'r') as f:
        content = f.read()
        return json.loads(content)

@responses.activate
def test_contact_card_details(test_dmsales_api, contact_details):
    responses.add(
        method='GET',
        url=test_dmsales_api.api_host + '/api/contact-card/',
        status=200,
        json=contact_details
    )

    assert test_dmsales_api.contact_card_details(
        project_id='123',
        base_key='bazaMR_123'
    ) == contact_details

@responses.activate
def test_contact_card_add_note(test_dmsales_api):
    responses.add(
        method='POST',
        url=test_dmsales_api.api_host + '/api/contact-card/add-note',
        status=200,
        json='ok'
    )

    assert test_dmsales_api.contact_card_add_note(
        project_id='123',
        base_key='bazaMR_123',
        content='test message',
        tag='test tag'
    ) == 'ok'
