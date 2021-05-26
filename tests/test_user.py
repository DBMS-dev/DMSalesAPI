import responses

@responses.activate
def test_me(test_dmsales_api):
    responses.add(
        method=responses.GET,
        url=test_dmsales_api.api_host + '/api/user/me',
        status=200,
        json={'uuid': '50cc92de-da24-4d7c-af12-fdc9d1776af9', 'name': None, 'surname': None, 'company_name': 'DBMS SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ', 'email': 'test@dmsales.com'}
    )
    
    assert test_dmsales_api.me() == {'uuid': '50cc92de-da24-4d7c-af12-fdc9d1776af9', 'name': None, 'surname': None, 'company_name': 'DBMS SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ', 'email': 'test@dmsales.com'}
    assert len(responses.calls) == 1
    assert responses.calls[0].request.params == {}

@responses.activate
def test_my_points(test_dmsales_api):
    responses.add(
        method=responses.GET,
        url=test_dmsales_api.api_host + '/api/user/wallet/points',
        status=200,
        json={'points': {'starter': 3200, 'pro': 9980}, 'isItMine': True}
    )

    assert test_dmsales_api.my_points() == {'points': {'starter': 3200, 'pro': 9980}, 'isItMine': True}
    assert len(responses.calls) == 1
    assert responses.calls[0].request.params == {}