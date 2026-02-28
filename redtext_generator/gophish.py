"""
GoPhish API client for REDTEXT.

Pure-stdlib HTTP client using urllib.request. Handles authentication,
JSON serialization, SSL context, and error translation.
"""

import json
import ssl
import time
import urllib.error
import urllib.request


class GoPhishAPIError(Exception):
    """Raised when the GoPhish API returns an error or connection fails."""

    def __init__(self, message, status_code=None, response_body=None):
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body


class GoPhishClient:
    """HTTP client for the GoPhish REST API.

    Args:
        api_url: Base URL of the GoPhish server (e.g. https://localhost:3333).
        api_key: API key for authentication.
        verify_ssl: Whether to verify SSL certificates. Set to False for
                     self-signed certs commonly used by GoPhish.
    """

    # Transient HTTP status codes that should trigger a retry
    _RETRYABLE_STATUS_CODES = {502, 503, 504, 429}

    def __init__(self, api_url, api_key, verify_ssl=True, timeout=30,
                 retries=3):
        self.api_url = api_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self.retries = retries

        if verify_ssl:
            self._ssl_context = ssl.create_default_context()
        else:
            self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            self._ssl_context.check_hostname = False
            self._ssl_context.verify_mode = ssl.CERT_NONE

    def _request(self, method, endpoint, data=None):
        """Send an HTTP request to the GoPhish API.

        Retries on transient errors (502, 503, 504, 429, connection failures)
        with exponential backoff. Non-retryable errors fail immediately.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE).
            endpoint: API path starting with / (e.g. /api/templates/).
            data: Optional dict to JSON-encode as the request body.

        Returns:
            Parsed JSON response as dict or list.

        Raises:
            GoPhishAPIError: On HTTP errors, connection failures, or
                             malformed responses.
        """
        url = self.api_url + endpoint
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json",
        }

        body = None
        if data is not None:
            body = json.dumps(data).encode("utf-8")

        last_error = None
        for attempt in range(self.retries):
            req = urllib.request.Request(
                url, data=body, headers=headers, method=method,
            )

            try:
                with urllib.request.urlopen(
                    req, context=self._ssl_context, timeout=self.timeout,
                ) as resp:
                    raw = resp.read().decode("utf-8")
                    if not raw:
                        return {}
                    return json.loads(raw)
            except urllib.error.HTTPError as e:
                resp_body = ""
                try:
                    resp_body = e.read().decode("utf-8")
                except Exception:
                    pass
                msg = f"GoPhish API error (HTTP {e.code})"
                try:
                    detail = json.loads(resp_body)
                    if "message" in detail:
                        msg = f"{msg}: {detail['message']}"
                except (json.JSONDecodeError, KeyError):
                    if resp_body:
                        msg = f"{msg}: {resp_body}"
                last_error = GoPhishAPIError(
                    msg, status_code=e.code, response_body=resp_body,
                )
                # Only retry on transient server errors
                if e.code not in self._RETRYABLE_STATUS_CODES:
                    raise last_error
            except urllib.error.URLError as e:
                last_error = GoPhishAPIError(f"Connection error: {e.reason}")
            except json.JSONDecodeError as e:
                raise GoPhishAPIError(f"Invalid JSON response: {e}")

            # Exponential backoff before retry
            if attempt < self.retries - 1:
                time.sleep(min(2 ** attempt, 8))

        # All retries exhausted
        raise last_error

    # ── Templates ──────────────────────────────────────────────

    def get_templates(self):
        """List all email templates."""
        return self._request("GET", "/api/templates/")

    def create_template(self, name, subject, text, html=""):
        """Create a new email template.

        Args:
            name: Template display name.
            subject: Email subject line.
            text: Plain text email body.
            html: HTML email body (optional).
        """
        payload = {"name": name, "subject": subject, "text": text, "html": html}
        return self._request("POST", "/api/templates/", data=payload)

    # ── Groups ─────────────────────────────────────────────────

    def create_group(self, name, targets):
        """Create a target group.

        Args:
            name: Group display name.
            targets: List of dicts with keys: email, first_name, last_name, position.
        """
        payload = {"name": name, "targets": targets}
        return self._request("POST", "/api/groups/", data=payload)

    # ── SMTP Profiles ──────────────────────────────────────────

    def get_smtp_profiles(self):
        """List all SMTP sending profiles."""
        return self._request("GET", "/api/smtp/")

    # ── Campaigns ──────────────────────────────────────────────

    def create_campaign(self, name, template_name, page_name, smtp_name,
                        url, group_names, launch_date=None):
        """Create a phishing campaign.

        GoPhish references templates, pages, SMTP profiles, and groups by
        name rather than by ID.

        Args:
            name: Campaign display name.
            template_name: Name of an existing GoPhish template.
            page_name: Name of an existing landing page.
            smtp_name: Name of an existing SMTP profile.
            url: Phishing URL that targets will receive.
            group_names: List of target group names.
            launch_date: ISO 8601 datetime string to schedule the campaign.
                         If None, the campaign launches immediately.
        """
        payload = {
            "name": name,
            "template": {"name": template_name},
            "page": {"name": page_name},
            "smtp": {"name": smtp_name},
            "url": url,
            "groups": [{"name": g} for g in group_names],
        }
        if launch_date:
            payload["launch_date"] = launch_date
        return self._request("POST", "/api/campaigns/", data=payload)

    def get_campaign_results(self, campaign_id):
        """Get the result summary for a campaign.

        Args:
            campaign_id: Integer campaign ID.
        """
        return self._request("GET", f"/api/campaigns/{campaign_id}/summary")
