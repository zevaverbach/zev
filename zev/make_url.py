# -*- coding: future_fstrings -*-
import urllib.parse


class Malformed(Exception):
    pass


def make_url(*parts, **params) -> str:
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
        url = f"{base}?{urllib.parse.urlencode(params)}"

    url = url or base
    _validate(url)

    return url


def _validate(url: str) -> None:
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
