"""Entry point for running the bot."""

from bot.config import TOKEN


def main() -> None:
    """Placeholder start function for the bot."""
    # The TOKEN is imported to ensure that configuration loading works
    # during startup. Actual bot logic would go here.
    _ = TOKEN  # Prevent unused-variable warnings
    print("Bot initialized")


if __name__ == "__main__":
    main()
