from fastapi import Depends, APIRouter
from fastapi_contrib.pagination import Pagination
from filters import EmployeeFilter
from serializers import EmployeeSerializer

router = APIRouter()


@router.get("/employee")
async def employees_list(pagination: Pagination = Depends(), args: EmployeeFilter = Depends()):
    return await pagination.paginate(
        serializer_class=EmployeeSerializer, **args.get_filter()
    )
