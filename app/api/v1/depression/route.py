from fastapi import APIRouter

from app.api.v1.depression.schema import DepressionRequest
from .service import get_depression

router=APIRouter()

@router.post('/depression',tags=['Depression'])
def get_depression():
    return get_depression()

@router.get('/info',tags=['Depression'])
def info():
    return {"service":"Depression API","version":"1.0"}

@router.delete('/depression',tags=['Depression'])
def delete_depression_record(record_id: int):
    return {"status":"depression","record_id":record_id}

@router.put('/depression',tags=['Depression'])
def update_depression_record(record_id: int, data: DepressionRequest):
    return {"status":"depression","record_id":"record_id"}

@router.patch('/depression',tags=['Depression'])
def patch_update_depression_record(record_id: int, data: dict):
    return {"status":"depression","record_id":"record_id"}