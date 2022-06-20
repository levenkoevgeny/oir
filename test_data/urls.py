from django.urls import path
from . import views

app_name = 'test_data'

urlpatterns = [
    path('', views.tests_list, name='test_list'),
    path('running/<test_id>', views.tests_running, name='test_running'),
    path('success', views.success_page, name='success_page'),
    path('dashboard', views.dashboard_main, name='dashboard_main'),
    path('dashboard/tests/<test_id>', views.dashboard_test_result, name='dashboard_test_result'),
    path('dashboard/tests/<test_id>/charts', views.dashboard_test_charts, name='dashboard_test_charts'),
    path('dashboard/tests/<test_id>/full', views.dashboard_test_full, name='dashboard_test_full'),
]