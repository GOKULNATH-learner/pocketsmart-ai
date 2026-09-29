from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.config import settings

router = APIRouter(tags=["Dashboard & Info"])

BASE_DIR = Path(__file__).resolve().parent.parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@router.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    """Main landing page introducing PocketSmart AI."""
    user = getattr(request.state, "user", None)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "user": user,
            "page_title": "PocketSmart AI - Smart Budget & Recommendation Assistant"
        }
    )

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    """User dashboard page displaying recent recommendations & saved plans."""
    user = getattr(request.state, "user", None)
    db = getattr(request.app.state, "db", None)
    
    recent_history = []
    if user and db:
        try:
            recent_history = db.get_user_history(user_id=user["id"], limit=5)
        except Exception:
            pass
            
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "user": user,
            "recent_history": recent_history,
            "page_title": "Dashboard - PocketSmart AI"
        }
    )

@router.get("/testimonials", response_class=HTMLResponse)
async def testimonials_page(request: Request):
    """Testimonials and success stories page."""
    user = getattr(request.state, "user", None)
    return templates.TemplateResponse(
        request=request,
        name="testimonials.html",
        context={
            "user": user,
            "page_title": "Testimonials - PocketSmart AI"
        }
    )

@router.get("/health")
async def health_check():
    """Health status check endpoint."""
    return {
        "status": "healthy",
        "app": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "gemini_model": settings.GEMINI_MODEL,
        "has_gemini_key": bool(settings.GEMINI_API_KEY)
    }

@router.get("/startup")
async def startup_check():
    """Startup diagnostic check endpoint."""
    return {
        "status": "initialized",
        "service": settings.PROJECT_NAME,
        "planners": ["Home Interior", "Party Planning", "Jewelry Recommendation"],
        "supported_platforms": ["Amazon", "Flipkart", "IKEA", "Pepperfry", "Swiggy", "Zomato", "OYO", "BookMyShow", "Tanishq", "CaratLane"]
    }
