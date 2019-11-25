# Copyright (c) 2016 testtools developers. See LICENSE for details.

"""Backwards compatibility for testtools.twistedsupport."""

__all__ = [
    'AsynchronousDeferredRunTest',
    'AsynchronousDeferredRunTestForBrokenTwisted',
    'SynchronousDeferredRunTest',
    'assert_fails_with',
]

from .twistedsupport import (
    AsynchronousDeferredRunTest,
    AsynchronousDeferredRunTestForBrokenTwisted,
    SynchronousDeferredRunTest,
    assert_fails_with,
)

# Never explicitly exported but had public names:
from .twistedsupport import (  # noqa: F401
    CaptureTwistedLogs,
    flush_logged_errors,
)
from .twistedsupport._runtest import (  # noqa: F401
    run_with_log_observers,
    UncleanReactorError,
)
