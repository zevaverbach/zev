import pytest

from zev.make_url import make_url, Malformed


def test_make_url():
    assert make_url("https://team.avt.io", "api", "rates", hi=123, bye="321") in [
        "https://team.avt.io/api/rates/?hi=123&bye=321",
        "https://team.avt.io/api/rates/?bye=321&hi=123",
    ]


def test_make_wrong_url_works():
    assert make_url("team.avt.io", "api", "rates", hi=123, bye="321") in [
        "https://team.avt.io/api/rates/?hi=123&bye=321",
        "https://team.avt.io/api/rates/?bye=321&hi=123",
    ]


def test_no_trailing_slash():
    assert make_url(
        "https://team.avt.io", "api", "rates", hi=123, bye="321", trailing_slash=False
    ) in [
        "https://team.avt.io/api/rates?hi=123&bye=321",
        "https://team.avt.io/api/rates?bye=321&hi=123",
    ]


def test_make_wrong_url_errors():
    with pytest.raises(Malformed):
        make_url("team", "api")
    with pytest.raises(Malformed):
        make_url("team.", "api")
    with pytest.raises(Malformed):
        make_url("team.", "api", hi=123)
    with pytest.raises(Malformed):
        make_url("api", hi=123)
    with pytest.raises(Malformed):
        make_url("team.a", "api", hi=123)
