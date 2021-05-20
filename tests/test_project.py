import responses

@responses.activate
def test_project_list(test_dmsales_api):
    responses.add(
        method=responses.GET, 
        url=test_dmsales_api.api_host + '/api/project/list',
        status=200,
        json=[{'id': 'e3e32d9f-213s-4687-97e5-c9448958c9fd', 'name': 'Projekt STARTER', 'active': True}]
    )

    assert test_dmsales_api.project_list() == [{'id': 'e3e32d9f-213s-4687-97e5-c9448958c9fd', 'name': 'Projekt STARTER', 'active': True}]
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == test_dmsales_api.api_host + '/api/project/list'
    assert responses.calls[0].request.params == {}