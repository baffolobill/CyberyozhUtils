# -*- coding: utf-8 -*-
import os
import mmap
import json
import pprint


class JsonSerializer:
    """
    Parse JSON config file (use mmap module to speed up the process)
    """

    def __init__(self):
        """
        Stub
        """
        pass

    @staticmethod
    def deserialize(json_path) -> 'dict':
        """
        Deserialize: config file to JSON
        :param_name json_path: Path to config file
        :return: memory buffer contains JSON
        """
        file_size = os.path.getsize(json_path)
        with open(json_path, "r") as payload_file:
            mapped_file = mmap.mmap(payload_file.fileno(), 0, access=mmap.ACCESS_READ)
            mapped_file.seek(0)
            json_buffer = mapped_file[:file_size]
        return json.loads(json_buffer.decode("utf-8"))

    @staticmethod
    def serialize(json_path, json_data, sort_keys=True):
        """
        Serialize: JSON to config file
        :param_name json_path: Path where to save config file
        :param_name json_data: Buffer to serialize
        """
        with open(json_path, 'w+', encoding='utf8') as outfile:
            outfile.write(json.dumps(json_data, indent=2, sort_keys=sort_keys, ensure_ascii=False))

    @staticmethod
    def pprint(json_dict):
        """
        Pretty print of JSON with UTF-8 encoding
        """
        bin_utf8 = pprint.pformat(json_dict).encode('utf-8')
        print(bin_utf8.decode())
