from ssec_tutorials.setup import TUTORIAL_CACHE


def test_cache_dir():
    """Tests the tutorial cache directory exists"""
    assert TUTORIAL_CACHE.exists() is True
