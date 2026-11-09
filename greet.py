"""Greeting program for the Week10 release exercise."""


def greet(name: str) -> str:
    """Return a greeting message for name."""
    return f"Hello, {name}!"


def main() -> int:
    """Print a greeting using the first command-line argument."""
    import sys

    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
    return 0


def test_greet() -> None:
    assert greet("Hee") == "Hello, Hee!"


if __name__ == "__main__":
    raise SystemExit(main())
