import json
import os

import matplotlib.pyplot as plt
import numpy as np


def aggregate_read_write_report(report_object):
    read_time = 0
    write_time = 0
    for key in report_object:
        if "get" in key:
            read_time += report_object.get(key)
        elif "export" in key:
            write_time += report_object.get(key)

    return read_time, write_time


def get_report_object_from_file(path):
    cwd = os.getcwd()

    f = open(path, "r")
    return json.load((f))


def object_file_json_to_time(path):
    obj = get_report_object_from_file(path)
    return aggregate_read_write_report(obj)


def object_mapping_to_time(obj):
    getter_obj = {}
    for key in obj:
        path = obj.get(key)
        read_time, write_time = object_file_json_to_time(path)
        getter_obj[key] = {
            "readTime": read_time,
            "writeTime": write_time,
        }

    return getter_obj


def object_report_to_lists(_object):
    keys = []
    read_times = []
    write_times = []
    for key in _object:
        keys.append(key)
        read_times.append(_object[key].get("readTime"))
        write_times.append(_object[key].get("writeTime"))

    return keys, read_times, write_times
