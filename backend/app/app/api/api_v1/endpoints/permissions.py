from fastapi import APIRouter, Depends, HTTPException
from typing import Any
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=schemas.PermissionList)
def read_permissions(db: Session = Depends(deps.get_db), current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
  """
  获取权限列表
  """
  permissions = crud.permission.get_multi(db, skip=0, limit=99999)
  return permissions


@router.post("/", response_model=schemas.Permission)
def create_permission(*,
                      db: Session = Depends(deps.get_db),
                      obj_in: schemas.PermissionCreate,
                      current_user: models.User = Depends(deps.get_current_active_superuser)) -> Any:
  """
  创建权限
  """
  item = crud.permission.create(db, obj_in=obj_in)
  return item


@router.get("/{code}", response_model=schemas.Permission)
def read_permission_by_code(
  code: str, current_user: models.User = Depends(deps.get_current_active_user), db: Session = Depends(deps.get_db)) -> Any:
  """
  根据Code获取权限信息
  """
  item = crud.permission.get_by_code(db, code=code)
  if not item:
    raise HTTPException(status_code=404, detail="权限不存在")
  return item


@router.put("/{code}", response_model=schemas.Permission)
def update_permission(*,
                      db: Session = Depends(deps.get_db),
                      code: str,
                      obj_in: schemas.PermissionUpdate,
                      current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
  """
  更新权限信息
  """
  item = crud.permission.get_by_code(db, code=code)
  if not item:
    raise HTTPException(status_code=404, detail="权限不存在")
  item = crud.permission.update(db, db_obj=item, obj_in=obj_in)
  return item


@router.delete("/{code}", response_model=schemas.Permission)
def delete_permission(*,
                      db: Session = Depends(deps.get_db),
                      code: str,
                      current_user: models.User = Depends(deps.get_current_active_superuser)) -> Any:
  """
  删除权限
  """
  item = crud.permission.get_by_code(db, code=code)
  if not item:
    raise HTTPException(status_code=404, detail="权限不存在")
  db.delete(item)
  db.commit()
  return item
