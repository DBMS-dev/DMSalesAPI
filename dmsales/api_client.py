import requests
import logging

from .endpoints import contacts, project, segment, events, search, person

logger = logging.getLogger(__name__)

class DMSalesAPI(
    project.ProjectEndpoints,
    contacts.ContactsEndpoints,
    segment.SegmentEndpoints,
    events.EventsEndpoints,
    search.SearchEndpoints,
    person.PersonEndpoints
):
    
    api_host = 'https://app.dmsales.com'

    def __init__(self, api_key, test=False):
        self.api_key = api_key

        if test is True:
            self.api_host = 'http://dmsales.test.dmsales.com:8081'

        self.session = requests.Session()
        self.session.headers = {'Authorization': f'Bearer {api_key}'}
