import math
from unittest.mock import Mock, patch

from dmsales import DMSalesAPI
from dmsales.helpers import person_generator

ALL_PERSONS_COUNT = 28

def load_persons_list_data(page: int, limit: int, **kwargs):
    '''
    Test helper function which generates dummy data in structure like in result of DMSalesAPI.persons_list method.
    Used to populate mocked method DMSalesAPI.persons_list with data

    :param page: same like in original method, describes which page you want to get
    :type page: int
    :param limit: same like in original method, describes how many data elements will apear on page
    :type limit: int
    :return: similar dict like in original method with data key containing only one "name" key with test value
    :rtype: dict
    '''
    pages_count = math.ceil(ALL_PERSONS_COUNT / limit) # count how many pages api would return
    data_objects_count = limit if limit <= ALL_PERSONS_COUNT else ALL_PERSONS_COUNT
    return {
        'all': ALL_PERSONS_COUNT,
        'total': ALL_PERSONS_COUNT, 
        'limit': limit, 
        'page': page, 
        'data': [
            {
                'name': {
                    'hidden': False,
                    'value': 'test-name'
                }
            } for i in range(data_objects_count)
        ] if page <= pages_count else []
    }
    

@patch.object(DMSalesAPI, 'persons_list')
def test_person_generator(mocked_persons_list):
    '''
    Tests person_generator if generates correct value of person objects
    '''
    dmsales_api = DMSalesAPI(api_key='1234')
    mocked_persons_list.side_effect = load_persons_list_data

    global ALL_PERSONS_COUNT
    assert len(list(person_generator(dmsales_api, segment_id='1234'))) == 28

    ALL_PERSONS_COUNT = 500
    assert len(list(person_generator(dmsales_api, segment_id='1234'))) == 500
