import logging

logger = logging.getLogger(__name__)

class APIOperations:
    
    def make_get_request(self, endpoint, **kwargs):
        try:
            logger.debug(f'Trying to make GET request to endpoint {endpoint} with query kwargs {kwargs}')
            response = self.session.get(self.api_host + endpoint, **kwargs)
        except Exception:
            logger.exception('Error occured when making GET request to DMSales API')
        else:
            logger.debug(f'DMSales API returned response {response}')
            return response.json()

    def make_post_request(self, endpoint, **kwargs):
        try:
            logger.debug(f'Trying to make POST request to endpoint {endpoint} with kwargs {kwargs}')
            response = self.session.post(self.api_host + endpoint, **kwargs)
        except Exception:
            logger.exception('Error occured when making POST request to DMSales API')
        else:
            logger.debug(f'DMSales API returned response {response}')
            logger.debug(f'Response message: {response.text}')
            return response.json()