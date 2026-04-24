class ValidationException(Exception):
    pass


class StakeValidationException(ValidationException):
    pass


class BetValidationException(ValidationException):
    pass


class LimitValidationException(ValidationException):
    pass


class ProbabilityValidationException(ValidationException):
    pass