import requests
import logging

from .endpoints import contacts, project

logger = logging.getLogger(__name__)

class DMSalesAPI(
    project.ProjectEndpoints,
    contacts.ContactsEndpoints
):
    
    api_host = 'https://app.dmsales.com'

    def __init__(self, api_key):
        self.api_key = api_key

        self.session = requests.Session()
        self.session.headers = {'Authorization': f'Bearer {api_key}'}
