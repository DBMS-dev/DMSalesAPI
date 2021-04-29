import logging

from dmsales.api_operations import APIOperations

logger = logging.getLogger(__name__)


class SegmentEndpoints(APIOperations):

    def segment_list(self, project_id: str):
        '''
        This call return segments from project

        :param project_id: ID from projects' list
        :type project_id: str
        :return: segments list
        :rtype: list
        '''
        endpoint = '/api/segment/list'
        args_dict = {
            'project_id': project_id
        }
        return super().make_get_request(endpoint, **args_dict)
        
    