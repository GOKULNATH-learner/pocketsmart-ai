import io
import uuid
from PIL import Image
from typing import Optional
from fastapi import APIRouter, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.config import settings
from app.services.gemini_utils import generate_jewelry_recommendations

router = APIRouter(tags=["Jewelry Planner"])

BASE_DIR = Path(__file__).resolve().parent.parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@router.get("/jewelry-planner", response_class=HTMLResponse)
async def jewelry_planner_page(request: Request):
    """Renders the Jewelry Budget Planner input form page."""
    user = getattr(request.state, "user", None)
    return templates.TemplateResponse(
        request=request,
        name="jewelry_planner.html",
        context={
            "user": user,
            "page_title": "Jewelry Budget Planner - PocketSmart AI"
        }
    )

@router.post("/generate-jewelry")
async def generate_jewelry_endpoint(
    request: Request,
    total_budget: float = Form(...),
    occasion: str = Form("Wedding Celebration"),
    style_preference: str = Form("Traditional Kundan & Gold"),
    outfit_image: Optional[UploadFile] = File(None)
):
    """
    Processes jewelry requirements and optional outfit photo upload for multimodal style matching.
    """
    user = getattr(request.state, "user", None)
    pil_image: Optional[Image.Image] = None

    if outfit_image and outfit_image.filename:
        if outfit_image.content_type not in settings.ALLOWED_IMAGE_TYPES:
            return templates.TemplateResponse(
                request=request,
                name="jewelry_planner.html",
                context={
                    "user": user,
                    "error": "Invalid image format. Allowed formats: JPG, PNG, WEBP.",
                    "page_title": "Jewelry Budget Planner - PocketSmart AI"
                }
            )

        contents = await outfit_image.read()
        if len(contents) > settings.MAX_UPLOAD_SIZE:
            return templates.TemplateResponse(
                request=request,
                name="jewelry_planner.html",
                context={
                    "user": user,
                    "error": "Uploaded image exceeds 5MB size limit. Please choose a smaller photo.",
                    "page_title": "Jewelry Budget Planner - PocketSmart AI"
                }
            )

        try:
            image_stream = io.BytesIO(contents)
            img = Image.open(image_stream)
            img = img.convert("RGB")
            img.thumbnail((1024, 1024))
            pil_image = img

            filename = f"outfit_{uuid.uuid4().hex[:8]}.jpg"
            saved_path = settings.UPLOAD_DIR / filename
            img.save(saved_path, "JPEG", quality=85)
        except Exception as e:
            print(f"Error processing outfit image: {e}")

    result = generate_jewelry_recommendations(
        total_budget=total_budget,
        occasion=occasion,
        style_preference=style_preference,
        pil_image=pil_image
    )

    db = getattr(request.app.state, "db", None)
    recommendation_id = None
    if user and db:
        try:
            recommendation_id = db.save_recommendation(
                user_id=user["id"],
                planner_type="Jewelry Recommendation",
                total_budget=total_budget,
                inputs_summary=f"Occasion: {occasion} | Style: {style_preference} | Image Uploaded: {'Yes' if pil_image else 'No'}",
                results=result
            )
        except Exception as e:
            print(f"Error saving jewelry recommendation history: {e}")

    if "application/json" in request.headers.get("accept", ""):
        return JSONResponse(content=result)

    return templates.TemplateResponse(
        request=request,
        name="recommendations.html",
        context={
            "user": user,
            "result": result,
            "recommendation_id": recommendation_id,
            "page_title": "Jewelry Budget Recommendations - PocketSmart AI"
        }
    )
