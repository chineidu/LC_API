import json
import typing as tp

import numpy as np
import pandas as pd
from classification_model import __version__ as model_version
from classification_model.predict import make_predictions
from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from loguru import logger

from app import __version__ as api_version, schemas
from app.config import settings

api_router = APIRouter()


@api_router.get(
    "/api-details/", response_model=schemas.APIDetails, status_code=status.HTTP_200_OK
)
def api_details() -> tp.Dict:
    """
    This endpoint is used to get the API details. It returns info like:
    project_name, api_version and model_version
    """
    api_details_ = schemas.APIDetails(
        project_name=settings.PROJECT_NAME,
        api_version=api_version,
        model_version=model_version,
    )

    return api_details_.dict()


@api_router.post(
    "/predict/", response_model=schemas.PredictionResults, status_code=status.HTTP_200_OK
)
async def predict(input_data: schemas.MultipleLendingDataInputs) -> tp.Any:
    """
    This endpoint is used to make predictions on the probability of default
    and default rate using the Lending Club Data. 
    """
    # Convert the MultipleLendingDataInputs object to Dict
    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))
    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    # Make predictions using the custom Classification Model
    results = make_predictions(input_data=input_df.replace({np.nan: None}))
    
    # Check for errors
    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('default_probability')}")

    return results
