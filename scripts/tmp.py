#!/usr/bin/env python3
"""
Script synopsis.
# :example
.private/tmp.py
"""
import requests
from retrying import retry

# retry request parameters
MAX_RETRIES = 3
RETRY_DELAY = 3000
REQUEST_TIMEOUT = 10


class Helper:
    """Return helper class."""

    @retry(
        stop_max_attempt_number=MAX_RETRIES,
        wait_fixed=RETRY_DELAY,
        retry_on_exception=lambda ex: isinstance(ex, ConnectionError),
    )
    def get_api_response(self):
        """Get secrets scopes in Databricks workspace."""
        response = requests.get(
            url="https://httpbin.org/ip",
            timeout=REQUEST_TIMEOUT,
        )
        if response.status_code == 200:
            scopes = response.json().get("origin", [])
            print(scopes)
            raise ConnectionError("aaa")
            # return scopes
        elif response.status_code == 429:
            raise ConnectionError("aaa")
        else:
            raise ConnectionRefusedError(
                "".join(
                    [
                        f"Status code: {response.status_code}.",
                        " Failed to get secrets scopes.",
                        f"\nMessage: {response.text}",
                    ]
                )
            )


tmp = Helper()
tmp.get_api_response()
