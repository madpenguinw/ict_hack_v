import logging
from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

import app_logger

logger = logging.getLogger(__name__)


class ServerConnect(APIView):
    def __init__(self):
        pass

    def get(self, request):
        logger.info('Got request')
        return Response({'hello': 'bye', 'id': 1}, HTTPStatus.OK)
