from typing import List

import aiohttp
from fastapi import APIRouter, Depends
from pydantic import parse_obj_as

from app.backend.api.dependencies import aio_http_client, get_current_user
from app.backend.apps.remote_data_storage.dumps.first_data_part import data as first_data_part
from app.backend.apps.remote_data_storage.dumps.second_data_part import data as second_data_part
from app.backend.apps.remote_data_storage.dumps.third_data_part import data as third_data_part
from app.backend.apps.remote_data_storage.models import Item
from app.backend.apps.remote_data_storage.utils import DataAggregator
from app.backend.apps.users.models import User
from app.backend.apps.users.permissions import is_admin_permission
from app.backend.settings import settings

router = APIRouter(prefix='/remote')


@router.get('/total', summary='Get sorted list of items', response_model=List[Item])
async def get_data(session: aiohttp.ClientSession = Depends(aio_http_client)):
    """
    Async getting data from "remote" services in "id" ordering.
    """
    return await DataAggregator(session=session).fetch_data(settings.REMOTE_SERVICES_URLS)


@router.get('/first-source', summary='First resource with items', response_model=List[Item])
async def get_ordered_data():
    """
    Getting Items list from "first-source".
    """
    return parse_obj_as(List[Item], first_data_part)


@router.get('/second-source', summary='Second resource with items', response_model=List[Item])
async def get_ordered_data():
    """
    Getting Items list from "second-source".
    """
    return parse_obj_as(List[Item], second_data_part)


@router.get('/third-part', summary='Third resource with items', response_model=List[Item])
async def get_ordered_data():
    """
    Getting Items list from "third-source".
    """
    return parse_obj_as(List[Item], third_data_part)
