"""Hello World program for the GitHub Actions lab."""

import os


def main():
    # Read the name from the WHO_TO_GREET environment variable.
    # If it is not set, fall back to a default value.
    name = os.environ.get("WHO_TO_GREET", "GitHub Actions Student")

    # Print the greeting.
    print(f"Hello {name}!")

    # Explain that the program ran inside GitHub Actions.
    print("This program is running inside GitHub Actions.")


if __name__ == "__main__":
    main()
