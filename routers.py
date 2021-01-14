from fastapi import APIRouter
from endpoints import home_page, reverse, forward, ip_address

router = APIRouter()

router.include_router(home_page.router, tags=["Home"])
router.include_router(reverse.router, tags=["Reverse"])
router.include_router(forward.router, tags=["Forward"])
router.include_router(ip_address.router, tags=["IP_Address"])