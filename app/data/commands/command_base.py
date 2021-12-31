from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Generic, TypeVar, Any, Dict, Union
from sqlalchemy.orm import Session

from app.data.database_app import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CommandBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: ModelType):
        self.model = model

    def get_one(self, db: Session, model_id: int) -> ModelType:
        return db.query(self.model).filter(self.model.id == model_id).first()

    def get_all(self, db: Session):
        db_results = db.query(self.model).all()
        return db_results

    def get_one_with_id(self, db: Session, model_id: Any) -> ModelType:
        return db.query(self.model).filter(self.model.id == model_id).first()

    def create(self, db: Session, *, schema_in: CreateSchemaType) -> ModelType:
        model_data = jsonable_encoder(schema_in)
        db_model = self.model(**model_data)
        db.add(db_model)
        db.commit()
        return db_model

    def update(self, db: Session, *, model_type: ModelType, schema_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        model_data = jsonable_encoder(schema_in)
        if isinstance(schema_in, dict):
            update_data = schema_in
        else:
            update_data = schema_in.dict(exclude_unset=True)

        for field in model_data:
            if field in update_data:
                setattr(model_type, field, update_data[field])

        db.add(model_type)
        db.commit()
        db.refresh()
        return model_type

    def delete(self, db: Session, *, model_id: int) -> ModelType:
        model_data = db.query(self.model).get(model_id)
        db.delete(model_data)
        db.commit()
        return model_data
