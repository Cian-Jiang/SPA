# Description: Schema for students  DTO (Data Transfer Object)
from pydantic import BaseModel
from typing import List


class StudentSchema(BaseModel):
    name: str
    username: str

    class Config:
        orm_mode = True


class StudentListSchema(BaseModel):
    __root__: List[StudentSchema]

    class Config:
        orm_mode = True

# class StudentListSchema(RootModel[List[StudentSchema]]):
#     root: List[StudentSchema]
#
#     def describe(self) -> str:
#         return f'Pets: {", ".join(self.root)}'
#
#     class Config:
#         orm_mode = True
