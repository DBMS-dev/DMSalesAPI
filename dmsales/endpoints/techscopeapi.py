import logging

from dmsales.api_operations import APIOperations

logger = logging.getLogger(__name__)

import requests

class TechScopeApiEndpoints(APIOperations):
    
    def start_techscopeapi(self, www: str):
        '''
        Starts techscopeapi generation process

        :param www: WWW to start techscopeapi
        :type www: str
        '''
        return super().make_post_request(endpoint='/api/techscopeapi/generate', params={'www': www})
        
    
    def techscopeapi_result(self, task_id: str):
        '''
        Get techscopeapi result with state

        :param task_id: task ID to check result (from start_techscopeapi method)
        :type task_id: str
        '''
        return super().make_get_request(endpoint='/api/techscopeapi/result', task_id=task_id)
        