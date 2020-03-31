from django.http.response import JsonResponse
from api.models import Vacancy,Company

def vacancy_list(request):
    vacancies=Vacancy.objects.all()
    vacancies_json=[vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def company_list(request):
    companies=Company.objects.all()
    companies_json=[company.comp_to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)


def vacancy_detail(request,vacancy_id):
    try:
        vacancy=Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    return JsonResponse(vacancy.to_json())

def company_detail(request, company_id):
    try:
        company=Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(company.comp_to_json())

def vacancy_by_company(request,company_id):
    try:
        company=Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    vacancies=company.vacancy_set.all()
    vacancies_json=[v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def top_ten(request):
    array=[]
    k=0
    vacancies=Vacancy.objects.order_by('-salary')
    vacancies_json=[vacancy.to_json() for vacancy in vacancies]
    for i in vacancies_json:
        array.append(i)
        k=k+1
        if(k==10):
            break
    return JsonResponse(array, safe=False)
