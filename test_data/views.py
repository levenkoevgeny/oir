from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import TestData, Subdivision, Faculty, Course, QuestionaryData, EmployeeKind, TestResult, Answer


def tests_list(request):
    all_tests_list = TestData.objects.all()
    return render(request, 'test_data/test_list.html', {'all_tests_list': all_tests_list})


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
            employee_kind=employee_kind,
            subdivision=subdivision,
            faculty=faculty,
            course=course,
        )
        new_questionary_data.save()

        current_test = get_object_or_404(TestData, pk=test_id)
        for question in current_test.question_set.all():
            if question.has_multiple_choice:
                for i in range(question.answer_set.all().count()):
                    if 'question_' + str(question.id) + '_checkbox_' + str(i) in request.POST:
                        new_test_result = TestResult(
                            questionary_data=new_questionary_data,
                            question=question,
                            answer=get_object_or_404(Answer, pk=request.POST[
                                'question_' + str(question.id) + '_checkbox_' + str(i)])
                        )
                        new_test_result.save()
            else:
                if 'question_' + str(question.id) + '_radio' in request.POST:
                    new_test_result = TestResult(
                        questionary_data=new_questionary_data,
                        question=question,
                        answer=get_object_or_404(Answer, pk=request.POST[
                            'question_' + str(question.id) + '_radio'])
                    )
                    new_test_result.save()
        return HttpResponseRedirect(reverse('test_data:success_page'))

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
    faculties_list = Faculty.objects.all()
    subdivision_list = Subdivision.objects.all()

    cadet_results = TestResult.objects.filter(questionary_data__employee_kind_id=1)
    pps_results = TestResult.objects.filter(questionary_data__employee_kind_id=2)

    cadet_results_dict = {}
    pps_results_dict = {}

    for question in current_test.question_set.all():
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
        'pps_results_dict': pps_results_dict,
        'current_test': current_test,
        'faculties_list': faculties_list,
        'subdivision_list': subdivision_list,
    })
