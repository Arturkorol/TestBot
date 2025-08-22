import logging
import smtplib
from email.message import EmailMessage

logger = logging.getLogger(__name__)


def send_email(smtp_server: str, from_addr: str, to_addr: str, subject: str, body: str) -> None:
    """Send an email using SMTP and log any issues.

    Parameters
    ----------
    smtp_server: str
        SMTP server address.
    from_addr: str
        Sender email address.
    to_addr: str
        Recipient email address.
    subject: str
        Email subject line.
    body: str
        Email body content.
    """
    msg = EmailMessage()
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP(smtp_server) as smtp:
            smtp.send_message(msg)
        logger.info("Email sent to %s", to_addr)
    except Exception as exc:
        logger.exception("Failed to send email: %s", exc)
