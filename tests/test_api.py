import math
import json

import numpy as np
import pandas as pd
from fastapi.testclient import TestClient


def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    # Given
    payload = {
        # Replace the np.nan
        "inputs": (test_data.replace({np.nan: None}).to_dict(orient="records"))
    }

    # The expected probability of default
    expected_pred_proba = 0.066

    # When
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload,
    )
    prediction_data = response.json()
    pred_proba = prediction_data.get("default_probability")[0]

    # Then
    assert response.status_code == 200
    assert prediction_data.get("default_probability")
    assert prediction_data.get("errors") is None
    assert np.isclose(expected_pred_proba, pred_proba, atol=0.03).all()
