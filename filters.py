from datetime import datetime
from typing import Tuple


class Filter:
    def __init__(self, **kwargs):
        self._filtered_field = {}
        for k, v in kwargs.items():
            self._filtered_field[k] = v
        super(Filter, self).__init__()

    def _prepare_value_for_query(self, k, v) -> Tuple[str, dict]:
        if k.endswith("min"):
            return k.replace("_min", ""), {'$gte': v}
        elif k.endswith("max"):
            return k.replace("_max", ""), {'$lte': v}
        return k, {'$regex': f".*{v}.*"}

    def get_filter(self) -> dict:
        output = {}
        for f, v in self._filtered_field.items():
            if v:
                prepared_f, prepared_v = self._prepare_value_for_query(f, v)
                output[prepared_f] = prepared_v
        return output


class EmployeeFilter(Filter):
    def __init__(self, name: str = None, email: str = None, age_min: int = None, age_max: int = None,
                 company: str = None, join_date_min: datetime = None, join_date_max: datetime = None,
                 job_title: str = None, gender: str = None, salary_min: int = None, salary_max: int = None):
        kwargs = {k: v for k, v in locals().items() if not k.startswith("_") and k != "self"}
        super(EmployeeFilter, self).__init__(**kwargs)
