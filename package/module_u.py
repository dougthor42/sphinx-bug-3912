# -*- coding: utf-8 -*-
"""
Utility functions for package.
"""
# ---------------------------------------------------------------------------
### Imports
# ---------------------------------------------------------------------------
# Standard Library
import json
import warnings
import functools

# ---------------------------------------------------------------------------
### Functions
# ---------------------------------------------------------------------------


def create_db_url(dialect, username, password, host, database,
                  port="", driver="", app_name=None):
    """
    Create an RFC-1738 compliant database URL for use with SQLAlchemy.

    Parameters
    ----------
    dialect : str
        The SQLAlchemy dialect to use.
    username : str
        The username to connect with.
    password : str
        The plaintext password for the given usernamne.
    host : str
        The host name or IP address of the database.
    database : str
        The database schema to connect to.
    port : str, optional
        The port to connect on.
    driver : str, optional
        The driver to use.
    app_name : str, optional
        The application making the connection.

    Returns
    -------
    str
        The SQLAlchemy database URL.
    """
    if driver != "":
        driver = "+{}".format(driver)

    if port != "":
        port = ":{}".format(port)

    fmt = "{dialect}{driver}://{user}:{pwd}@{host}{port}/{db}"

    if app_name is not None:
        fmt += "?application_name={}".format(app_name)

    return fmt.format(dialect=dialect, driver=driver, user=username,
                      pwd=password, host=host, port=port, db=database)


def read_conn_info_file(file, conn):
    """
    Read a connection information json file.

    Parameters
    ----------
    file : str
        The file path that contains connection information.
    conn : str
        The connection name to get from the file.

    Returns
    -------
    str
        The generated SQLAlchemy database URL.
    """
    with open(file, 'r') as openf:
        data = json.load(openf)

    conn_info = data[conn]

    return create_db_url(**conn_info)


def deprecated(func):
    """
    A decorator which can be used to mark functions as deprecated.

    It will result in a warning being emitted when the function is used.
    """
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.warn_explicit(
            "Call to deprecated function {}.".format(func.__name__),
            category=DeprecationWarning,
            filename=func.func_code.co_filename,
            lineno=func.func_code.co_firstlineno + 1
        )
        return func(*args, **kwargs)
    return new_func
