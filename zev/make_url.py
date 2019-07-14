# -*- coding: future_fstrings -*-
import sys
import urllib.parse


class Malformed(Exception):
    pass


def make_url(*parts, trailing_slash=True, **params):
    base = "/".join(parts)
    if trailing_slash:
        base += "/"
    url = None

    if not base.startswith("http"):
        base = f"https://{base}"
    if params:
        url = f"{base}?{urllib.parse.urlencode(params)}"

    url = url or base
    validate(url)

    return url


def validate(url):
    result = urllib.parse.urlparse(url)
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
