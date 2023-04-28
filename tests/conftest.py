import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client