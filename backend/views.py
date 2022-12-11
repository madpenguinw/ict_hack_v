import logging
from http import HTTPStatus

from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

import app_logger
from backend.models import Company, Project, Student, Participants

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
    def get(self, request, id):
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


class GetOneStudent(APIView):
    def fill_participant_dict(self, participant):
        
        project_id = participant.project.id
        project_title = participant.project.title
        project_description = participant.project.description
        project_data_dict = {
            'id': project_id,
            'title': project_title,
            'description': project_description,
        }
        return project_data_dict

    def get(self, request, id):
        logger.info('Got request for student with id = %(id)s', {'id': id})
        try:
            student = get_object_or_404(Student, id=id)
            project_data_list = []
            try:
                participant = get_object_or_404(Participants, student=student)
                project_data_dict = self.fill_participant_dict(participant)
                project_data_list.append(project_data_dict)
            except Participants.MultipleObjectsReturned:
                participants_list = get_list_or_404(
                    Participants, student=student)
                for participant in participants_list:
                    project_data_dict = self.fill_participant_dict(participant)
                    project_data_list.append(project_data_dict)
            response = {
                'id': student.id,
                'username': student.username,
                'first_name': student.first_name,
                'last_name': student.last_name,
                'patronymic': student.patronymic,
                'birth_date': student.birth_date,
                'education': student.education,
                'project': project_data_list,
                'email': student.email,
                'phone': student.phone,
            }
            status = HTTPStatus.OK
        except Exception as error:
            logger.error(error)
            response = {}
            status = HTTPStatus.NOT_FOUND
        return Response(response, status)


class GetAllStudents(APIView):
    def get(self, request):
        logger.info('Got request for all students')
        try:
            students = Student.objects.all()
            data = []
            for student in students:
                one_student = {
                    'id': student.id,
                    'last_name': student.last_name,
                    'first_name': student.first_name,
                    'patronymic': student.patronymic,
                    'birth_date': student.birth_date,
                }
                data.append(one_student)
            response = {
                'students': data
            }
            status = HTTPStatus.OK
        except Exception as error:
            logger.error(error)
            response = {}
            status = HTTPStatus.NOT_FOUND
        return Response(response, status)


class GetOneCompany(APIView):
    def get(self, request, id):
        logger.info('Got request for company with id = %(id)s', {'id': id})
        try:
            company = get_object_or_404(Company, id=id)
            response = {
                'id': company.id,
                'username': company.username,
                'name': company.name,
                'activities': company.activities,
                'address': company.address,
            }
            status = HTTPStatus.OK
        except Exception as error:
            logger.error(error)
            response = {}
            status = HTTPStatus.NOT_FOUND
        return Response(response, status)


class GetAllCompanies(APIView):
    def get(self, request):
        logger.info('Got request for all Companies')
        try:
            Companies = Company.objects.all()
            data = []
            for company in Companies:
                one_company = {
                    'id': company.id,
                    'username': company.username,
                    'name': company.name,
                    'activities': company.activities,
                    'address': company.address,
                }
                data.append(one_company)
            response = {
                'Companies': data
            }
            status = HTTPStatus.OK
        except Exception as error:
            logger.error(error)
            response = {}
            status = HTTPStatus.NOT_FOUND
        return Response(response, status)
