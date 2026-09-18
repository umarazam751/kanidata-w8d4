"""Tiny pipeline used to demonstrate Docker + CI/CD."""
import sys


def clean_email(email: str) -> str:
    """Strip + lowercase."""
    return email.strip().lower()


def is_valid_customer(row: dict) -> bool:
    """Return True if this row looks like a valid customer."""
    if not row.get("email"):
        return False
    return "@" in row["email"]


def run() -> int:
    rows = [
        {"name": "Sarah", "email": "  Sarah@Example.com "},
        {"name": "Bob",   "email": "bob-no-at"},
        {"name": "Carol", "email": "carol@example.com"},
    ]
    valid = [r for r in rows if is_valid_customer(r)]
    for r in valid:
        r["email"] = clean_email(r["email"])
    print(f"Pipeline ran. {len(valid)} valid rows of {len(rows)}.")
    for r in valid:
        print(f"  - {r['name']:8s}  {r['email']}")
    return 0


if __name__ == "__main__":
    sys.exit(run())