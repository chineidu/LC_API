from typing import Generator


import pandas as pd
import pytest
from fastapi.testclient import TestClient
from classification_model.config.core import config
from classification_model.processing.data_manager import load_data

from app.main import app


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    data = load_data(filepath=config.app_config.test_data_file, is_train=False)
    return data.head(1)


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
