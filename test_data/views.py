from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import TestData, Subdivision, Faculty, Course, QuestionaryData, EmployeeKind, TestResult, Answer
from .models import SINGLE, MULTIPLE, TEXT
from django.db import transaction
from django.http import HttpResponse

EMPLOYEE_CADET_ID = 1
EMPLOYEE_PPS_ID = 2


def tests_list(request):
    if request.user_agent.browser.family == 'IE':
        return HttpResponse("Ваш браузер не поддерживается")
    else:
        all_tests_list = TestData.objects.all()
        return render(request, 'test_data/test_list.html', {'all_tests_list': all_tests_list})


@transaction.atomic
def tests_running(request, test_id):
    if request.method == "POST":
        employee_kind = get_object_or_404(EmployeeKind, pk=request.POST['employee_kind'])
        subdivision = get_object_or_404(Subdivision,
                                        pk=request.POST['subdivision']) if 'subdivision' in request.POST and \
                                                                           request.POST['subdivision'] != '' else None
        faculty = get_object_or_404(Faculty, pk=request.POST['faculty']) if 'faculty' in request.POST and request.POST[
            'faculty'] != '' else None
        course = get_object_or_404(Course, pk=request.POST['course']) if 'course' in request.POST and request.POST[
            'course'] != '' else None

        new_questionary_data = QuestionaryData(
            test=get_object_or_404(TestData, pk=test_id),
            employee_kind=employee_kind,
            subdivision=subdivision,
            faculty=faculty,
            course=course,
        )
        new_questionary_data.save()

        current_test = get_object_or_404(TestData, pk=test_id)
        for question in current_test.question_set.all():
            if question.question_type == MULTIPLE:
                for i in range(question.answer_set.all().count()):
                    if 'question_' + str(question.id) + '_checkbox_' + str(i) in request.POST:
                        answer = get_object_or_404(Answer, pk=request.POST[
                            'question_' + str(question.id) + '_checkbox_' + str(i)])
                        new_result = TestResult.objects.create(
                            questionary_data=new_questionary_data,
                            question=question,
                            answer=answer
                        )
                        if answer.has_extra_data:
                            if 'question_' + str(question.id) + '_checkbox_' + str(i) + '_extra_input' in request.POST:
                                new_result.extra_data = request.POST[
                                    'question_' + str(question.id) + '_checkbox_' + str(i) + '_extra_input']
                                new_result.save()

            elif question.question_type == SINGLE:
                if 'question_' + str(question.id) + '_radio' in request.POST:
                    answer = get_object_or_404(Answer, pk=request.POST[
                        'question_' + str(question.id) + '_radio'])
                    new_result = TestResult.objects.create(
                        questionary_data=new_questionary_data,
                        question=question,
                        answer=answer
                    )

                    if answer.has_extra_data:
                        if 'question_' + str(question.id) + '_radio_extra_input' in request.POST:
                            new_result.extra_data = request.POST['question_' + str(question.id) + '_radio_extra_input']
                            new_result.save()

            elif question.question_type == TEXT:
                if 'question_' + str(question.id) + '_text' in request.POST:
                    new_test_result = TestResult(
                        questionary_data=new_questionary_data,
                        question=question,
                        answer_text=request.POST['question_' + str(question.id) + '_text']
                    )
                    new_test_result.save()
            else:
                pass
        return HttpResponseRedirect(reverse('test_data:success_page'))
    else:
        if request.user_agent.browser.family == 'IE':
            return HttpResponse("Ваш браузер не поддерживается")
        else:

            current_test = get_object_or_404(TestData, pk=test_id)
            return render(request, 'test_data/test_running.html',
                          {
                              'current_test': current_test,
                              'employee_kinds': EmployeeKind.objects.all(),
                              'subdivision_list': Subdivision.objects.all(),
                              'faculties_list': Faculty.objects.all(),
                              'courses_list': Course.objects.all(),
                          })


def success_page(request):
    return render(request, 'test_data/success_page.html')


def dashboard_main(request):
    all_tests_list = TestData.objects.all()
    return render(request, 'test_data/dashboard/dashboard_main.html', {
        'all_tests_list': all_tests_list,
    })


def dashboard_test_result(request, test_id):
    current_test = get_object_or_404(TestData, pk=test_id)
    question_set = current_test.question_set.filter(question_type__in=[SINGLE, MULTIPLE])
    faculties_list = Faculty.objects.all()
    courses_list = Course.objects.all()
    subdivision_list = Subdivision.objects.all()

    cadet_results = TestResult.objects.filter(questionary_data__employee_kind_id=EMPLOYEE_CADET_ID)
    pps_results = TestResult.objects.filter(questionary_data__employee_kind_id=EMPLOYEE_PPS_ID)

    cadet_results_dict = {}
    cadet_results_courses_dict = {}
    pps_results_dict = {}

    for question in question_set:
        answer_res_dict = {}
        for answer in question.answer_set.all():
            faculty_res_dict = {}
            for faculty in faculties_list:
                faculty_res_dict[str(faculty.id)] = cadet_results.filter(questionary_data__faculty=faculty,
                                                                         question=question, answer=answer).count()
            faculty_res_dict['all'] = cadet_results.filter(questionary_data__faculty__in=faculties_list,
                                                           question=question, answer=answer).count()
            answer_res_dict[str(answer.id)] = faculty_res_dict
        cadet_results_dict[str(question.id)] = answer_res_dict

    for question in current_test.question_set.all():
        answer_res_dict = {}
        for answer in question.answer_set.all():
            course_res_dict = {}
            for course in courses_list:
                course_res_dict[str(course.id)] = cadet_results.filter(questionary_data__course=course,
                                                                       question=question, answer=answer).count()
            course_res_dict['all'] = cadet_results.filter(questionary_data__course__in=courses_list,
                                                          question=question, answer=answer).count()
            answer_res_dict[str(answer.id)] = course_res_dict
        cadet_results_courses_dict[str(question.id)] = answer_res_dict

    for question in current_test.question_set.all():
        answer_res_dict = {}
        for answer in question.answer_set.all():
            subdivision_res_dict = {}
            for subdivision in subdivision_list:
                subdivision_res_dict[str(subdivision.id)] = pps_results.filter(
                    questionary_data__subdivision=subdivision,
                    question=question, answer=answer).count()
            subdivision_res_dict['all'] = pps_results.filter(questionary_data__subdivision__in=subdivision_list,
                                                             question=question, answer=answer).count()
            answer_res_dict[str(answer.id)] = subdivision_res_dict
        pps_results_dict[str(question.id)] = answer_res_dict

    return render(request, 'test_data/dashboard/dashboard_test_result.html', {
        'cadet_results_dict': cadet_results_dict,
        'cadet_results_courses_dict': cadet_results_courses_dict,
        'pps_results_dict': pps_results_dict,
        'current_test': current_test,
        'question_set': question_set,
        'faculties_list': faculties_list,
        'courses_list': courses_list,
        'subdivision_list': subdivision_list,
        'cadet_results_count': QuestionaryData.objects.filter(employee_kind=EMPLOYEE_CADET_ID, test_id=test_id).count(),
        'pps_results_count': QuestionaryData.objects.filter(employee_kind=EMPLOYEE_PPS_ID, test_id=test_id).count(),
        'all_results_count': QuestionaryData.objects.filter(test_id=test_id).count(),
    })


def dashboard_test_charts(request, test_id):
    return render(request, 'test_data/dashboard/dashboard_test_charts.html')


def dashboard_test_full(request, test_id):
    questionary_list = QuestionaryData.objects.all()
    current_test = get_object_or_404(TestData, pk=test_id)
    question_list = current_test.question_set.all()
    return render(request, 'test_data/dashboard/dashboard_test_full.html', {
        'questionary_list': questionary_list,
        'current_test': current_test,
        'question_list': question_list,
    })
