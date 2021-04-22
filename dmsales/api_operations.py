import logging

logger = logging.getLogger(__name__)

class APIOperations:
    
    def make_get_request(self, endpoint, **query_args):
        try:
            logger.debug(f'Trying to make GET request to endpoint {endpoint} with query args {query_args}')
            response = self.session.get(self.api_host + endpoint, params=query_args)
        except Exception:
            logger.exception('Error occured when making GET request to DMSales API')
        else:
            logger.debug(f'DMSales API returned response {response}')
            return response.json()