"""TODO: Add docstring."""

import time

import pyarrow as pa
from dora import Node

def main() -> None:
    """TODO: Add docstring."""
    dora_node = Node()
    i = 0
    start = time.time()
    while time.time() - start < 10:
        dora_node.send_output("ts", pa.array([time.perf_counter_ns(), i]))
        i += 1
        # print(f"Sent {i} times", flush=True)
        time.sleep(0.001)


if __name__ == "__main__":
    main()
