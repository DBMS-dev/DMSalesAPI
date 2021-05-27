import responses
import json

@responses.activate
def test_add_custom_event(test_dmsales_api):
    responses.add(
        method=responses.POST,
        url=test_dmsales_api.api_host + '/api/events/add-custom-event',
        status=200,
        json='ok'
    )

    assert test_dmsales_api.add_custom_event(
        project_id='1234',
        type='testevent',
        custom={'custom_field': 'custom_data'},
        base_key='bazaMR_0000000000'
    ) == 'ok'

    assert len(responses.calls) == 1
    assert responses.calls[0].request.body == json.dumps({
        'project_uuid': '1234',
        'type': 'testevent',
        'base_key': 'bazaMR_0000000000',
        'custom': {'custom_field': 'custom_data'}
    }).encode('utf-8')

