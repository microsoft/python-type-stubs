from datetime import date as real_date
from datetime import datetime as real_datetime
from datetime import time
from typing import Any

class date(real_date):
    def strftime(self, fmt: str) -> str: ...

class datetime(real_datetime):
    def strftime(self, fmt: str) -> str: ...
    def combine(self, date: date, time: time) -> datetime: ...
    def date(self) -> date: ...

def new_date(d: real_date) -> date: ...
def new_datetime(d: real_datetime) -> datetime: ...
def strftime(dt: datetime, fmt: str) -> str: ...
