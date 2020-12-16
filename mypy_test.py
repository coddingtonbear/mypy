from typing import Any, Union

from mypy.isinstance import IsInstance

print(IsInstance[int])


def my_type_guard(my_var: Any) -> IsInstance[int]:
    try:
        int(my_var)
        return True
    except TypeError:
        return False


def my_function_with_std() -> bool:
    return True

#variable: Any = "OK"
#
#if isinstance(variable, str):
#    reveal_type(variable)
#
#if my_type_guard(variable):
#    reveal_type(variable)
#else:
#    reveal_type(variable)
#

value = my_function_with_std()

reveal_type(value)
