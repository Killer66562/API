from pydantic import BaseModel

from datetime import datetime


class BaseSchema(BaseModel):
    id_: int
    created_at: datetime


class CUMappingKeySchema(BaseModel):
    name: str


class MappingKeySchema(BaseSchema, CUMappingKeySchema): pass


class CUMappingValueSchema(BaseModel):
    name: str
    key_id: int


class MappingValueSchema(BaseSchema, CUMappingValueSchema): pass


class FullMappingKeySchema(MappingKeySchema):
    mapping_values: list[MappingValueSchema] = []


class FullMappingValueSchema(MappingValueSchema):
    mapping_key: MappingKeySchema