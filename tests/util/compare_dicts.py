import logging

LOGGER = logging.getLogger(__name__)


def remove_none_values(d):
    """
    Recursively remove all None values from dictionary and its sub-dictionaries.

    This is because Pydantic includes optional types in the model result,
    so to compare the model with the original input we must remove None values.
    """
    if isinstance(d, list):
        return [remove_none_values(v) for v in d]
    elif isinstance(d, dict):
        return {k: remove_none_values(v) for k, v in d.items() if v is not None}
    else:
        return d


def replace_bool_w_strings(d):
    """
    Model can return Booleans as True or False, while input was 'true' or 'false'
    """

    def replace_bools(v):
        if v is False:
            return "false"
        if v is True:
            return "true"
        return v

    if isinstance(d, list):
        return [replace_bools(v) for v in d]
    elif isinstance(d, dict):
        return {k: replace_bools(v) for k, v in d.items() if v is not None}
    else:
        return d


def equal_dicts(d1, d2):
    d1 = replace_bool_w_strings(remove_none_values(d1))
    d2 = replace_bool_w_strings(remove_none_values(d2))
    LOGGER.debug("Comparing:\nd1:%s\nd2:%s", d1, d2)
    return d1 == d2
