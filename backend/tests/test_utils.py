import logging
from unittest.mock import patch

from app.utils import send_email_safely


def test_send_email_safely_logs_and_swallows_delivery_errors(
    caplog: logging.LogCaptureFixture,
) -> None:
    with (
        patch("app.utils.send_email", side_effect=RuntimeError("smtp down")),
        caplog.at_level(logging.ERROR),
    ):
        send_email_safely(
            email_to="user@example.com", subject="Hello", html_content="<p>hi</p>"
        )

    assert "Failed to send email" in caplog.text


def test_send_email_safely_passes_arguments_through() -> None:
    with patch("app.utils.send_email") as send:
        send_email_safely(
            email_to="user@example.com", subject="Hello", html_content="<p>hi</p>"
        )

    send.assert_called_once_with(
        email_to="user@example.com", subject="Hello", html_content="<p>hi</p>"
    )
