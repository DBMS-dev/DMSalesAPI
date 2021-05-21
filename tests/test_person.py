import responses

@responses.activate
def test_add_person(test_dmsales_api):
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
        person_dict={
            "id": "bazaMR_0000000000",
            "project_id": "b5faf3c9-2672-4cf0-b0aa-57ce8c2a8a21",
            "project_person": {
                "tags": [
                    "tag1",
                    "tag2"
                ],
                "type": "b2b",
                "address": {
                    "city": "Katowice",
                    "county": "Katowice",
                    "postal_code": "40-101",
                    "street": "Al. Piastów",
                    "street_number": "10",
                    "local_number": "35",
                    "voivodeship": "śląskie"
                },
                "personal_data": {
                    "name": "Nowy",
                    "surname": "Lead",
                    "company_name": "My Very First Company",
                    "position": "CEO"
                },
                "email": {
                    "raw": "exae-email@test.test"
                },
                "phone": {
                    "raw": "+48 123 456 678"
                },
                "sex": "kobieta"
            }
        }
    ) == {'code': 201, 'message': 'Created', 'details': 'Person added successfully.'}
    assert len(responses.calls) == 1

@responses.activate
def test_update_person(test_dmsales_api):
    responses.add(
        method='PUT',
        url=test_dmsales_api.api_host + '/api/persons/upsert',
        status=201,
        json={'code': 201, 'message': 'Created', 'details': 'Person added successfully.'}
    )

    assert test_dmsales_api.update_person(
        id='123',
        project_id='1234-898-000-999',
        person_dict={
            "id": "bazaMR_0000000000",
            "project_id": "b5faf3c9-2672-4cf0-b0aa-57ce8c2a8a21",
            "project_person": {
                "tags": [
                    "tag1",
                    "tag2"
                ],
                "type": "b2b",
                "address": {
                    "city": "Katowice",
                    "county": "Katowice",
                        "postal_code": "40-101",
                        "street": "Al. Piastów",
                        "street_number": "10",
                        "local_number": "35",
                        "voivodeship": "śląskie"
                },
                "personal_data": {
                    "name": "Nowy",
                    "surname": "Lead",
                    "company_name": "My Very First Company",
                    "position": "CEO"
                },
                "email": {
                    "raw": "exae-email@test.test"
                },
                "phone": {
                    "raw": "+48 123 456 678"
                },
                "sex": "kobieta"
            }
        }
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
