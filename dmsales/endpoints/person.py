import logging
from typing import Union, Dict, TypedDict, List, Optional

from dmsales.api_operations import APIOperations

logger = logging.getLogger(__name__)


class ProjectPerson(TypedDict):
    tags: List[str]
    type: str
    address: Dict[str, str]
    postal_code: str
    street: str
    street_number: str
    local_number: str
    voivodeship: str
    personal_data: Dict[str, str]
    email: Dict[str, str]
    phone: Dict[str, str]
    '''
    Example Dict:
    {
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
    '''


class PersonEndpoints(APIOperations):

    def add_person(self, id: Optional[str], project_id: str, person_dict: ProjectPerson):
        '''
        Adds person to project

        :param id: person id
        :type id: Optional[str, None]
        :param project_id: project id where person will be added
        :type project_id: str
        :param person_dict: person data
        :type person_dict: ProjectPerson
        '''
        endpoint = '/api/persons/upsert'
        data = {
            'id': id,
            'project_id': project_id,
            'project_person': person_dict
        }
        return super().make_post_request(endpoint=endpoint, data=data)

    def update_person(self):
        pass
        # put request
