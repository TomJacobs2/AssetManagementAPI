#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import TypeVar, Any, Dict, Union

from app.data.database_app import Base
from app.schema.type_schema import TypeCreate, TypeUpdate

ModelType = TypeVar("ModelType", bound=Base)


def get_all(db: Session, model: ModelType, include_retired: bool = True) -> ModelType:
    if include_retired:
        return db.query(model).all()
    else:
        return db.query(model).filter(model.retired is False).all()


def get_type_by_id(db: Session, model: ModelType, id: int):
    return db.query(model).filter(model.id == id).first()


def get_type_by_code(db: Session, model: ModelType, code: str):
    return db.query(model).filter(model.code == code).first()


def create(db: Session, model: ModelType, schema_in: TypeCreate) -> ModelType:
    model_data = jsonable_encoder(schema_in)
    db_model: ModelType = model(**model_data)
    db.add(db_model)
    db.commit()
    return db_model


def update(db: Session, model: ModelType, schema_in: Union[TypeUpdate, Dict[str, Any]]) -> ModelType:
    model_data = jsonable_encoder(schema_in)
    if isinstance(schema_in, dict):
        update_data = schema_in
    else:
        update_data = schema_in.dict(exclude_unset=True)

    for field in model_data:
        if field in update_data:
            setattr(model, field, update_data[field])

    db.add(model)
    db.commit()
    db.refresh()
    return model


def retire_type_by_id(db: Session, model: ModelType, id: int):
    db.execute(f"UPDATE {model} SET retired = 1 WHERE id = {id}")
    db.commit()


def retire_type_by_code(db: Session, model: ModelType, code: str):
    db.execute(f"UPDATE {model} SET retired = 1 WHERE id = {id}")
    db.commit()
