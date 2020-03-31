from django.urls import path

from api.views import vacancy_list, company_list, vacancy_detail,  company_detail, vacancy_by_company,top_ten

urlpatterns= [
        path('vacancies/',vacancy_list),
        path('vacancies/<int:vacancy_id>/',vacancy_detail),
        path('vacancies/top_ten/',top_ten),
        path('companies/',company_list),
        path('companies/<int:company_id>/',company_detail),
        path('companies/<int:company_id>/vacancies/',vacancy_by_company)
]