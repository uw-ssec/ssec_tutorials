import os
import pytest
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

TUTORIALS_CACHE_ENV = "SSEC_TUTORIALS_CACHE"

@pytest.fixture(scope="function")
def setup_env():
    with TemporaryDirectory() as tmpdir:
        cache_dir = str((Path(tmpdir) / "ssec_tutorials").resolve())
        os.environ[TUTORIALS_CACHE_ENV] = cache_dir
        from ssec_tutorials.setup import TUTORIAL_CACHE
        yield TUTORIAL_CACHE, cache_dir

def test_default_cache():
    """Tests the tutorial cache directory exists"""
    from ssec_tutorials.setup import TUTORIAL_CACHE
    cache_dir = str(Path.home() / ".cache" / "ssec_tutorials")
    assert os.environ.get(TUTORIALS_CACHE_ENV) is None
    assert TUTORIAL_CACHE.exists() is True
    assert str(TUTORIAL_CACHE) == cache_dir
    del sys.modules["ssec_tutorials.setup"]

def test_custom_cache_dir(setup_env):
    """Tests the tutorial cache directory exists"""
    TUTORIAL_CACHE, cache_dir = setup_env
    assert TUTORIAL_CACHE.exists() is True
    assert str(TUTORIAL_CACHE) == cache_dir
    del os.environ[TUTORIALS_CACHE_ENV]
    del sys.modules["ssec_tutorials.setup"]
