import responses

@responses.activate
def test_segment_list(test_dmsales_api):
    responses.add(
        method=responses.GET,
        url=test_dmsales_api.api_host + '/api/segment/list',
        json=[{'id': 'c51sea53-d8fe-4417-bf81-e0625842af57', 'name': 'Twoje kontakty'}]
    )

    assert test_dmsales_api.segment_list(project_id='1234') == [{'id': 'c51sea53-d8fe-4417-bf81-e0625842af57', 'name': 'Twoje kontakty'}]
    assert len(responses.calls) == 1
    assert responses.calls[0].request.params == {'project_id': '1234'}