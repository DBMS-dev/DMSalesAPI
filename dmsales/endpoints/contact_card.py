import logging

from dmsales.api_operations import APIOperations

logger = logging.getLogger(__name__)


class CardEndpoints(APIOperations):

    def get_contact_card(self, project_id: str, base_key: str):
        '''
        Returns details about record for given base_key.

        :param project_id: project_id
        :type project_id: str
        :param base_key: base_key
        :type base_key: str
        :return: Details about record for given base_key
        :rtype: dict
        '''        
        endpoint = '/api/contact-card/'
        args_dict = {
            'project_id': project_id,
            'base_key': base_key
        }

        args_dict = {k: v for k, v in args_dict.items() if v} # exclude None args
        logger.debug('Calling contact_card method')
        return super().make_get_request(endpoint, **args_dict)