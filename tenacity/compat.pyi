from typing import Any, Optional

def warn_about_non_retry_state_deprecation(cbname: Any, func: Any, stacklevel: Any) -> None: ...
def warn_about_dunder_non_retry_state_deprecation(fn: Any, stacklevel: Any) -> None: ...
def func_takes_retry_state(func: Any): ...
def make_retry_state(previous_attempt_number: Any, delay_since_first_attempt: Any, last_result: Optional[Any] = ...): ...
def func_takes_last_result(waiter: Any): ...
def stop_dunder_call_accept_old_params(fn: Any): ...
def stop_func_accept_retry_state(stop_func: Any): ...
def wait_dunder_call_accept_old_params(fn: Any): ...
def wait_func_accept_retry_state(wait_func: Any): ...
def retry_dunder_call_accept_old_params(fn: Any): ...
def retry_func_accept_retry_state(retry_func: Any): ...
def before_func_accept_retry_state(fn: Any): ...
def after_func_accept_retry_state(fn: Any): ...
def before_sleep_func_accept_retry_state(fn: Any): ...
def retry_error_callback_accept_retry_state(fn: Any): ...
def get_exc_info_from_future(future: Any): ...