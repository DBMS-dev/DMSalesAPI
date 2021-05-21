import logging

from dmsales.api_operations import APIOperations

logger = logging.getLogger(__name__)

class UserEndpoints(APIOperations):
    
    def me(self):
        '''
        Returns user information
        '''
        return super().make_get_request(endpoint='/api/user/me')

    def my_points(self):
        '''
        Returns user points
        '''
        return super().make_get_request(endpoint='/api/user/wallet/points')
