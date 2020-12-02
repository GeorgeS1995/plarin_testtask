from fastapi_contrib.serializers.common import ModelSerializer
from models import EmployeeModel


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeModel
        exclude = {"id"}
