from django.urls import path

from api.Views.views_fbv import vacancy_list, vacancy_detail, company_list,company_detail
from api.Views.views_cbv import CompanyDetailAPIView, CompanyListAPIView,VacancyByCategory,VacancyTopTen\
        ,VacancyDetailAPIView,VacancyListAPIView
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns= [
        path('login/', obtain_jwt_token),
        path('vacancies/',vacancy_list),
        path('vacancies/<int:vacancy_id>/',vacancy_detail),
        # path('companies/', company_list),
        # path('companies/<int:company_id>/', company_detail),
        # path('vacancies/', VacancyListAPIView.as_view()),
        # path('vacancies/<int:vacancy_id>/', VacancyDetailAPIView.as_view()),
        path('companies/', CompanyListAPIView.as_view()),
        path('companies/<int:company_id>/', CompanyDetailAPIView.as_view()),
        path('vacancies/top_ten/',VacancyTopTen.as_view()),
        path('companyvacancies/',VacancyByCategory.as_view()),
]