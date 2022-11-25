import typing as tp

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from loguru import logger

from app.api import api_router
from app.config import settings, setup_app_logging

# Setup logging
setup_app_logging(config=settings)

description = """This is used to make predictions
(probability of default and default status) using the lending data.
"""

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description=description,
)

root_router = APIRouter()


@root_router.get("/")
def index() -> tp.Any:
    """This is the index. It returns a basic HTML response."""
    body = """
            <html>
                <body style='padding: 15px;'>
                    <h1>Welcome to the Lending Club API</h1>
                    <div>
                    Check the docs: <a href='/docs'>here</a>
                    </div>
                </body>
            </html>
    """
    return HTMLResponse(content=body)


# Add the routers
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


if __name__ == "__main__":
    import uvicorn

    host = "localhost"
    port = 8005

    # Use this for debugging purposes only
    logger.warning("Running in development mode. Do not run like this in production.")

    # Run the server
    uvicorn.run(app, host=host, port=port, log_level="debug")
