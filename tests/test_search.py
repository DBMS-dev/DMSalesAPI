import responses

@responses.activate
def test_search_list(test_dmsales_api):
    responses.add(
        method=responses.GET,
        url=test_dmsales_api.api_host + '/api/search/list',
        status=200,
        json=[{'id': '01163eb1-61b5-4dc1-9550-f35e6274caf2', 'name': 'Twoje kontakty', 'type': 'profile'}, {'id': 'd510ws53-d8fe-4411-bf88-e0625842af57', 'name': 'Twoje kontakty', 'type': 'segment'}]
    )

    assert test_dmsales_api.search_list(project_id='1234') == [{'id': '01163eb1-61b5-4dc1-9550-f35e6274caf2', 'name': 'Twoje kontakty', 'type': 'profile'}, {'id': 'd510ws53-d8fe-4411-bf88-e0625842af57', 'name': 'Twoje kontakty', 'type': 'segment'}]
    assert len(responses.calls) == 1
    assert responses.calls[0].request.params == {'project_id': '1234'}