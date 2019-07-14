# -*- coding: future_fstrings -*-
import sys

if sys.version_info[0] < 3:
    import urllib
    import urlparse

    url_encode = urllib.urlencode
    url_parse = urlparse.urlparse
else:
    import urllib.parse

    url_encode = urllib.parse.urlencode
    url_parse = urllib.parse.urlparse


class Malformed(Exception):
    pass


def make_url(*parts, **params):
    base = "/".join(parts)
    trailing_slash = True
    if params.get("trailing_slash") is not None:
        trailing_slash = params["trailing_slash"]
        del params["trailing_slash"]
    if trailing_slash:
        base += "/"
    url = None

    if not base.startswith("http"):
        base = f"https://{base}"
    if params:
        url = f"{base}?{url_encode(params)}"

    url = url or base
    _validate(url)

    return url


def _validate(url):
    result = url_parse(url)
    if (
        result.netloc.endswith(".")
        or "." not in result.netloc
        or len(result.netloc.split(".")[-1]) < 2
    ):
        raise Malformed("Must provide a domain")
    if all((result.scheme, result.netloc, result.path)):
        return None
    else:
        missing = [i for i in ("scheme", "netloc", "path") if not getattr(result, i)]
        is_are = "is" if len(missing) == 1 else "are"
        raise Malformed(f"{' and '.join(missing)} {is_are} missing.")
