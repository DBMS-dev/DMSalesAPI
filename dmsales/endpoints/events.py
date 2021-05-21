import logging
import json

from dmsales.api_operations import APIOperations

logger = logging.getLogger(__name__)

class EventsEndpoints(APIOperations):
    
    def add_custom_event(self, project_id, type, custom: dict, base_key=None, 
                         email=None, phone=None, public_identifier_li=None):
        endpoint = '/api/events/add-custom-event'

        data = {
            'project_uuid': project_id,
            'type': type,
            'base_key': base_key,
            'email': email,
            'phone': phone,
            'public_identifier_li': public_identifier_li,
            'custom': custom
        }

        data = {k: v for k, v in data.items() if v} # exclude None args
        logger.debug('Calling add_custom_event method')
        return super().make_post_request(endpoint, json=data)