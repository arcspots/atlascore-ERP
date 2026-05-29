class DomainException(Exception):
    """Base exception for domain errors"""
    pass


class CompanyAlreadyExists(DomainException):
    pass


class CompanyNotFound(DomainException):
    pass


class UserAlreadyExists(DomainException):
    pass


class UnauthorizedAction(DomainException):
    pass