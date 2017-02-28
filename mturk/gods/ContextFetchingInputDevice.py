import Queue
import uuid

from system import system_channels

from devices import InputDevice
from TextData import TextData


class ContextFetchingInputDevice(InputDevice.AbstractInputDevice):
    """
    """
    def __init__(self, timeout_seconds = 0.5):
        super(ContextFetchingInputDevice, self).__init__()
        self.timeout_seconds = timeout_seconds
        self.dispatched_inputs = Queue.Queue()

    def request_context(self):
        """
            Fetch a new input and add to the dispatched queue.
        """
        new_id = uuid.uuid4().hex
        new_input = {
            "id" : new_id,
            "data": "Sample context. {}".format(new_id)
        }

        self.dispatched_inputs.put(new_input)
        return new_input

    def take_input(self):
        """
            Get inputs from the dispatched queue.
        """
        try:
            return self.dispatched_inputs.get(True, timeout = self.timeout_seconds)
        except Queue.Empty:
            return None