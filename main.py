import logging

from send_email import send_email


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)


if __name__ == "__main__":
    # Example usage; will log SMTP errors if sending fails.
    send_email(
        smtp_server="localhost",
        from_addr="noreply@example.com",
        to_addr="user@example.com",
        subject="Test Email",
        body="This is a test message",
    )
