"""
This type stub file was generated by pyright.
"""

from kombu.log import get_logger
from kombu.utils.eventio import ERR, READ, WRITE
from kombu.utils.objects import cached_property

"""Event loop implementation."""
logger = get_logger(__name__)
_current_loop = None
W_UNKNOWN_EVENT = """\
Received unknown event %r for fd %r, please contact support!\
"""
class Stop(BaseException):
    """Stops the event loop."""
    ...


def get_event_loop():
    """Get current event loop object."""
    ...

def set_event_loop(loop):
    """Set the current event loop object."""
    ...

class Hub:
    """Event loop object.

    Arguments:
        timer (kombu.asynchronous.Timer): Specify custom timer instance.
    """
    READ = ...
    WRITE = ...
    ERR = ...
    on_close = ...
    def __init__(self, timer=...) -> None:
        ...
    
    @property
    def poller(self):
        ...
    
    @poller.setter
    def poller(self, value):
        ...
    
    def reset(self):
        ...
    
    def stop(self):
        ...
    
    def __repr__(self):
        ...
    
    def fire_timers(self, min_delay=..., max_delay=..., max_timers=..., propagate=...):
        ...
    
    def add(self, fd, callback, flags, args=..., consolidate=...):
        ...
    
    def remove(self, fd):
        ...
    
    def run_forever(self):
        ...
    
    def run_once(self):
        ...
    
    def call_soon(self, callback, *args):
        ...
    
    def call_later(self, delay, callback, *args):
        ...
    
    def call_at(self, when, callback, *args):
        ...
    
    def call_repeatedly(self, delay, callback, *args):
        ...
    
    def add_reader(self, fds, callback, *args):
        ...
    
    def add_writer(self, fds, callback, *args):
        ...
    
    def remove_reader(self, fd):
        ...
    
    def remove_writer(self, fd):
        ...
    
    def close(self, *args):
        ...
    
    def on_callback_error(self, callback, exc):
        ...
    
    def create_loop(self, generator=..., sleep=..., min=..., next=..., Empty=..., StopIteration=..., KeyError=..., READ=..., WRITE=..., ERR=...):
        ...
    
    def repr_active(self):
        ...
    
    def repr_events(self, events):
        ...
    
    @cached_property
    def scheduler(self):
        ...
    
    @property
    def loop(self):
        ...
    


