from django.urls import path
from . import views

app_name = 'test_data'

urlpatterns = [
    path('', views.tests_list, name='test_list'),
    path('running/<test_id>', views.tests_running, name='test_running'),
    path('success', views.success_page, name='success_page'),
    path('dashboard', views.dashboard_main, name='dashboard_main'),
    path('dashboard/tests/<test_id>', views.dashboard_test_result, name='dashboard_test_result'),
    # path('subjects/<subject_id>/tests', views.test_list, name='test_list'),
    # path('subjects/<subject_id>/test/<test_id>/passing', views.test_passing, name='test_passing'),
    # path('subjects/<subject_id>/test/<test_id>/result', views.test_result, name='test_result'),
    # path('subjects/<subject_id>/test/<test_id>/result/<result_id>', views.test_result, name='test_result'),
    # path('results', views.test_all_results, name='test_all_results'),
]