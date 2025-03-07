from fastapi import APIRouter, Request
from phish_interface import request_linkedin_html, create_bait
import logging

logger = logging.getLogger('router')

router = APIRouter(
    prefix="/mock",
    tags=["mock"],
    responses={404: {"description": "Not found"}},
)

@router.get("/fetch-linkedin-page/{url}")
async def fetch_linkedin_page(request: Request, url:str):
    return request_linkedin_html(url)

@router.get("/bait/{url}")
async def bait(request: Request, url:str):
    return create_bait()

@router.get("/welcome")
async def welcome(request: Request):
    return "Welcome"

