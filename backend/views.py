import logging
from http import HTTPStatus

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

import app_logger

from backend.models import Project

logger = logging.getLogger(__name__)


class ServerConnect(APIView):
    def __init__(self):
        pass

    def get(self, request):
        logger.info('Got request')
        return Response({'hello': 'bye', 'id': 1}, HTTPStatus.OK)


class GetAllProjects(APIView):
    def get(self, request):
        logger.info('Got request for all projects')
        try:
            projects = Project.objects.all()
            data = []
            for project in projects:
                one_project = {
                    'id': project.id,
                    'title': project.title,
                    'description': project.description,
                }
                data.append(one_project)
            response = {
                'projects': data
            }
            status = HTTPStatus.OK
        except Exception as error:
            logger.error(error)
            response = {}
            status = HTTPStatus.NOT_FOUND
        return Response(response, status)


class GetOneProject(APIView):
    def get(self, request):
        logger.info('Got request for project with id = %(id)s', {'id': id})
        try:
            project = get_object_or_404(Project, id=id)
            response = {
                'id': project.id,
                'title': project.title,
                'description': project.description,
                'precondition': project.precondition,
                'result': project.result,
                'criterias': project.criterias,
                'host_company': project.host_company.name,
            }
            status = HTTPStatus.OK
        except Exception as error:
            logger.error(error)
            response = {}
            status = HTTPStatus.NOT_FOUND
        return Response(response, status)
