from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, validator

from dundie.utils.email import check_valid_email


# flake8: noqa
class InvalidEmailError(Exception):
    ...


class Person(BaseModel):
    pk: str
    name: str
    dept: str
    role: str

    @validator("pk")
    def validate_email(cls, v):  # cls e a instancia e v o valor
        if not check_valid_email(v):
            raise InvalidEmailError(f"Email is invalid for {v!r}")
        return v

    def __str__(self) -> str:
        return f"{self.name} - {self.role}"


class Balance(BaseModel):
    person: Person
    value: Decimal

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class Movement(BaseModel):
    person: Person
    date: datetime
    actor: str
    value: Decimal


import json

from dundie.database import connect

db = connect()

for pk, data in db["people"].items():
    p = Person(pk=pk, **data)


print(p)
print(json.dumps(p.dict()))

balance = Balance(person=p, value=Decimal(100))
print(balance)
print(balance.json(models_as_dict=False))
