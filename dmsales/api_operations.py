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

    def make_post_request(self, endpoint, data):
        try:
            logger.debug(f'Trying to make POST request to endpoint {endpoint} with data {data}')
            response = self.session.post(self.api_host + endpoint, json=data)
        except Exception:
            logger.exception('Error occured when making POST request to DMSales API')
        else:
            logger.debug(f'DMSales API returned response {response}')
            logger.debug(f'Response message: {response.text}')
            return response.json()