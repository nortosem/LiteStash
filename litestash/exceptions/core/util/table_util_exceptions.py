"""LiteStash Table Utility Exceptions Module

This module defines the exception classes used within the
`litestash.table_util` module.

These exceptions inherit from `LiteStashException` and provide
specific error handling for operations related to table creation
and management in the LiteStash key-value store.

- **`TableUtilError`**  Base exception class for table_util module
- **`TableNameNotFoundError`** Table name is unfound
- **`InvalidTableClassError`** Invalid table class provided somehow
- **`ParentTableClassError`** Must use a defined table
- **`NoneTableClassError`** None is not a table
- **`InvalidStashColumnError`** Invalid argument for StashColumn
- **`StashColumnTypeError`** Type must be a StashColumn
"""
from litestash.exceptions.base_exception import LiteStashException
from litestash.core.config.default_exceptions.util_exceptions import \
    TableUtilErrorMessages


class TableUtilError(LiteStashException):
    """
    Base class for exceptions in the `table_util` module.

    This exception class serves as the foundation for all custom
    exceptions defined within the `table_util` module. It inherits
    from `LiteStashException`, providing a consistent base
    exception type for table utility-related operations.

    Inheritance:
        LiteStashException
    """
    pass


class TableNameNotFoundError(TableUtilError):
    """
    Exception raised when a table name is not found.

    This exception is raised by functions in the `table_util` module
    when an attempt is made to access or generate a table name that
    does not exist or cannot be determined.

    Initialization:
        __init__(self, message=None)

    Args:
        message (str, optional):
            A custom error message to provide more context about the
            exception. If None, a default message is used.

    Inheritance:
        TableUtilError
    """

    def __init__(self, message=None):
        """
        Initializes a new instance of TableNameNotFoundError.
        """
        super().__init__(
            message or TableUtilErrorMessages.table_not_found()
        )


class InvalidTableClassError(TableUtilError):
    """
    Exception raised when an invalid table class is used.

    This exception is raised when a function in `table_util` receives
    an argument that is not a valid table class, such as when a
    non-class type or a class that does not inherit from the
    appropriate base class is provided.

    Initialization:
        __init__(self, message=None)

    Args:
        message (str, optional):
            A custom error message. If None, a default message is used.

    Inheritance:
        TableUtilError
    """

    def __init__(self, message=None):
        """
        Initializes a new instance of InvalidTableClassError.
        """
        super().__init__(
            message or TableUtilErrorMessages.invalid_table_class()
        )


class ParentTableClassError(TableUtilError):
    """
    Exception raised when the parent Table class is used directly.

    This exception is raised when a function in `table_util` is
    called with the base `Table` class itself, rather than a
    specific subclass representing a concrete table definition.

    Initialization:
        __init__(self, message=None)

    Args:
        message (str, optional):
            A custom error message. If None, a default message is used.

    Inheritance:
        TableUtilError
    """

    def __init__(self, message=None):
        """
        Initializes a new instance of ParentTableClassError.
        """
        super().__init__(
            message or TableUtilErrorMessages.parent_table_class()
        )


class NoneTableClassError(TableUtilError):
    """
    Exception raised when None is provided as the table class.

    This exception is raised when a function in `table_util` that
    expects a table class receives `None` as an argument.

    Initialization:
        __init__(self, message=None)

    Args:
        message (str, optional):
            A custom error message. If None, a default message is used.

    Inheritance:
        TableUtilError
    """

    def __init__(self, message=None):
        """
        Initializes a new instance of NoneTableClassError.
        """
        super().__init__(
            message or TableUtilErrorMessages.none_table_class()
        )


class InvalidStashColumnError(TableUtilError):
    """
    Exception raised when an invalid StashColumn is used.

    This exception is raised when a function in `table_util` receives
    an argument that is not a valid `StashColumn` object, such as
    when `None` or an object of an incorrect type is provided.

    Initialization:
        __init__(self, message=None)

    Args:
        message (str, optional):
            A custom error message. If None, a default message is used.

    Inheritance:
        TableUtilError
    """

    def __init__(self, message=None):
        """
        Initializes a new instance of InvalidStashColumnError.
        """
        super().__init__(
            message or TableUtilErrorMessages.invalid_stash_column()
        )


class StashColumnTypeError(TableUtilError):
    """
    Exception raised when the stash_column type is invalid.

    This exception is raised when a function in `table_util` expects
    an argument of type `StashColumn` but receives a value of a
    different type.

    Initialization:
        __init__(self, message=None)

    Args:
        message (str, optional):
            A custom error message. If None, a default message is used.

    Inheritance:
        TableUtilError
    """

    def __init__(self, message=None):
        """
        Initializes a new instance of StashColumnTypeError.
        """
        super().__init__(
            message or TableUtilErrorMessages.stash_column_type()
        )
