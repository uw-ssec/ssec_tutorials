import os
import pytest
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

TUTORIALS_CACHE_ENV = "SSEC_TUTORIALS_CACHE"

@pytest.fixture(scope="function", params=[False, True])
def cache_dir(request):
    if request.param:
        with TemporaryDirectory() as tmpdir:
            cache_dir = str((Path(tmpdir) / "ssec_tutorials").resolve())
            os.environ[TUTORIALS_CACHE_ENV] = cache_dir
    else:
        cache_dir = str(Path.home() / ".cache" / "ssec_tutorials")

    yield cache_dir

    if TUTORIALS_CACHE_ENV in os.environ:
        del os.environ[TUTORIALS_CACHE_ENV]
    del sys.modules["ssec_tutorials.setup"]

def test_cache_dir(cache_dir):
    """Tests the tutorial cache directory exists"""
    from ssec_tutorials.setup import TUTORIAL_CACHE
    if ".cache" in cache_dir:
        # Ensure that environment variable is not set
        assert TUTORIALS_CACHE_ENV not in os.environ
    assert TUTORIAL_CACHE.exists() is True
    assert str(TUTORIAL_CACHE) == cache_dir
