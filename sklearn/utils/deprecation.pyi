from typing import Callable, Optional, Union, Any
import warnings
import functools

__all__ = ["deprecated"]

class deprecated:

    # Adapted from https://wiki.python.org/moin/PythonDecoratorLibrary,
    # but with many changes.

    def __init__(self, extra: str = "") -> None: ...
    def __call__(self, obj: Union[Callable, property]) -> Union[Callable, property]: ...
    def _decorate_class(self, cls): ...
    def _decorate_fun(self, fun: Callable) -> Callable: ...
    def _decorate_property(self, prop: property) -> property: ...
    def _update_doc(self, olddoc: Optional[str]) -> str: ...

def _is_deprecated(func): ...
