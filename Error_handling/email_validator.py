from custom_errors import NameTooShort, MustContainAtSymbolError, InvalidDomainError
from helper import VALID_DOMAINS

email = input()


def valid_email(email):
    try:
        name, domain = email.split("@")
    except ValueError:
        raise MustContainAtSymbolError("Email must contain @")

    try:
        domain_name, extension = domain.split(".")
    except ValueError:
        raise InvalidDomainError("Domain must be...")
    if extension not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be...")

    if len(name) < 4:
        raise NameTooShort("Name must be at least 4 symbols")
    return True


while not email == "End":
    if valid_email(email):
        print("Email is valid")
    email = input()


