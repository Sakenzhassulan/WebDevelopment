from rest_framework import serializers

from api.models import Vacancy, Company


class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(allow_blank=True)
    salary = serializers.FloatField()
    company_id_id = serializers.IntegerField()

    def create(self, validated_data):
        vacancy = Vacancy.objects.create(name=validated_data.get('name'), description=validated_data.get('description'),
        salary=validated_data.get('salary'), company_id_id=validated_data.get('company_id_id'))
        return vacancy

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description= validated_data.get('description',instance.description)
        instance.salary = validated_data.get('salary',instance.salary)
        instance.company_id_id= validated_data.get('company_id_id',instance.company_id_id)
        instance.save()
        return instance

class CompanySerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=200)
    description = serializers.CharField(allow_blank=True)
    class Meta:
        model = Company
        fields = ('id', 'name','description','city','address')

class CompanyWithVacancySerializer(serializers.ModelSerializer):
    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # products = serializers.StringRelatedField(many=True, read_only=True)
    vacancies = VacancySerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = ('id', 'name','description','city','address', 'vacancies')
