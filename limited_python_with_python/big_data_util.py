import ctypes
import os
import threading
import time
from ctypes import wintypes

# Constants
JOB_OBJECT_LIMIT_PROCESS_TIME = 0x00000002
JOB_OBJECT_LIMIT_PROCESS_MEMORY = 0x00000100
JobObjectExtendedLimitInformation = 9

# Define the nested basic limit struct
class JOB_OBJECT_BASIC_LIMIT_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("PerProcessUserTimeLimit", ctypes.c_longlong),
        ("PerJobUserTimeLimit", ctypes.c_longlong),
        ("LimitFlags", wintypes.DWORD),
        ("MinimumWorkingSetSize", ctypes.c_size_t),
        ("MaximumWorkingSetSize", ctypes.c_size_t),
        ("ActiveProcessLimit", wintypes.DWORD),
        ("Affinity", ctypes.c_size_t),
        ("PriorityClass", wintypes.DWORD),
        ("SchedulingClass", wintypes.DWORD),
    ]

class IO_COUNTERS(ctypes.Structure):
    _fields_ = [("Dummy", ctypes.c_ulonglong * 6)]  # We're not using IO data here

# Wrap it in the extended struct
class JOBOBJECT_EXTENDED_LIMIT_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("BasicLimitInformation", JOB_OBJECT_BASIC_LIMIT_INFORMATION),
        ("IoInfo", IO_COUNTERS),
        ("ProcessMemoryLimit", ctypes.c_size_t),
        ("JobMemoryLimit", ctypes.c_size_t),
        ("PeakProcessMemoryUsed", ctypes.c_size_t),
        ("PeakJobMemoryUsed", ctypes.c_size_t),
    ]

def set_limits(memory_mb: int, time_sec: int):
    print(f"Applying limits: {memory_mb} MB memory, {time_sec} seconds time limit.")

    memory_bytes = memory_mb * 1024 * 1024
    time_100ns = time_sec * 10_000_000

    k32 = ctypes.windll.kernel32
    job = k32.CreateJobObjectW(None, None)
    if not job:
        raise OSError("Failed to create Job Object")

    info = JOBOBJECT_EXTENDED_LIMIT_INFORMATION()
    info.BasicLimitInformation.LimitFlags = JOB_OBJECT_LIMIT_PROCESS_TIME | JOB_OBJECT_LIMIT_PROCESS_MEMORY
    info.BasicLimitInformation.PerProcessUserTimeLimit = time_100ns
    info.ProcessMemoryLimit = memory_bytes

    res = k32.SetInformationJobObject(job, JobObjectExtendedLimitInformation,
                                      ctypes.byref(info), ctypes.sizeof(info))
    if not res:
        err = k32.GetLastError()
        raise OSError(f"Failed to set job info. Error code: {err}")

    # Assign current process to job
    proc = k32.OpenProcess(0x1F0FFF, False, os.getpid())
    if not k32.AssignProcessToJobObject(job, proc):
        raise OSError("Failed to assign process to job")

    # Wall-clock kill fallback
    def enforce_wall_time():
        time.sleep(time_sec)
        print("|====|  ⏱️  Time Limit reached ⏱️  |====|")
        os._exit(1)

    threading.Thread(target=enforce_wall_time, daemon=True).start()


def print_size_of_object(obj):
    """
    This is a util function to check how much memory an object takes in memory.
    """
    try:
        from pympler import asizeof
    except:
        print("Before using get_size_of_object(obj), you must `python -m pip install pympler`")
        exit()

    
    print(f"Object memory used: {asizeof.asizeof(obj) / (1024 ** 2):.2f} MB")

def print_current_memory_usage():
    """ 
    This is a util function to check how much memory the python process takes. When this number reaches the limit, the process crashes.
    """
    try:
        import psutil
        import os
    except:
        print("Before using get_current_memory_usage(), you must `python -m pip install psutil`")
        exit()

    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()

    print(f"Total Memory Used: {mem_info.vms / (1024 ** 2):.2f} MB")   # Virtual Memory Size
