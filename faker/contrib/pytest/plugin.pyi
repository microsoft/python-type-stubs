from typing import Any

from pytest.fixtures import FixtureRequest

from faker import Faker as Faker
from faker.config import DEFAULT_LOCALE as DEFAULT_LOCALE

DEFAULT_SEED: int

def faker(request: FixtureRequest) -> Faker: ...
