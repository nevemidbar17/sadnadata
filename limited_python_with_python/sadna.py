from big_data_util import set_limits, print_current_memory_usage, print_size_of_object

# Example usage: Limit to 20MB memory and 5 minutes execution
set_limits(memory_mb=20, time_sec=300)

l = [0] * 1_000_000  # This allocation exceeds the limit and crashes the process.

help(print_current_memory_usage)  # Util function, remove this if not used
help(print_size_of_object)  # Util function, remove this if not used
