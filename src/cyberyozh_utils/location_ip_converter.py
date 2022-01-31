# -*- coding: utf-8 -*-
import os
import sys
import csv
import argparse
import socket
import struct


"""
The script converts every range in IP2Location LITE IP-COUNTRY Database 
https://lite.ip2location.com/ip-address-ranges-by-country
from integer representation to form 'xxx.xxx.xxx.xxx'
"""


def int_to_ip(ip):
    """
    Convert 4-byte integer to IP-address form 'xxx.xxx.xxx.xxx'
    """
    return socket.inet_ntoa(struct.pack("!I", ip))


def convert_ip2location(database_file, output_file):
    """
    Converts every range in IP2Location LITE-IP-COUNTRY Database
    in CSV format START_ADDR,END_ADDR,COUNTRY_CODE,COUNTRY
    from integer representation to form 'xxx.xxx.xxx.xxx'
    """
    full_filepath = os.path.abspath(database_file)
    if not os.path.isfile(full_filepath):
        print("{0} does not exist, exiting".format(full_filepath))
        sys.exit(0)

    all_ranges = list()
    with open(full_filepath, "r", newline='') as csvfile:
        ip_reader = csv.reader(csvfile)
        for iprange_row in ip_reader:
            text_row = list()
            text_row.append(int_to_ip(int(iprange_row[0])))
            text_row.append(int_to_ip(int(iprange_row[1])))
            text_row.append("%s" % iprange_row[2])
            text_row.append("%s" % iprange_row[3])
            all_ranges.append(", ".join(text_row))
    with open(output_file, 'w', newline='') as new_cvs:
        for line in all_ranges:
            new_cvs.write("%s\n" % line)


def strip_port(database_file, output_file):
    full_filepath = os.path.abspath(database_file)
    if not os.path.isfile(full_filepath):
        print("{0} does not exist, exiting".format(full_filepath))
        sys.exit(0)
    with open(full_filepath, "r", newline='') as input_file:
        ip_collection = input_file.read().splitlines()
    new_list = list()
    for line in ip_collection:
        ip_port = line.split(":")
        new_list.append(ip_port[0])
    with open(output_file, 'w', newline='') as new_cvs:
        for line in new_list:
            new_cvs.write("%s\n" % line)


def main():
    """
    :return: system exit code
    """
    parser = argparse.ArgumentParser(description='Command-list_str interface')
    parser.add_argument('--ip',
                        help='IP addresses to convert from int to string',
                        required=False)
    parser.add_argument('--from-file',
                        help='Text file with newline-separated IP ranges START,END,COUNTRY_CODE,COUNTRY',
                        required=False)
    parser.add_argument('--to-file',
                        help='CSV file to write IP converted result',
                        required=False)

    args = parser.parse_args()
    if args.ip:
        print(int_to_ip(args.ip))
    if args.from_file and args.to_file:
        script_path = os.path.dirname(os.path.realpath(__file__))
        full_filepath = os.path.join(script_path, args.from_file)
        print("Input CSV database: %s" % os.path.abspath(full_filepath))
        print("Output file: %s" % os.path.abspath(args.to_file))
        convert_ip2location(database_file=os.path.abspath(full_filepath), output_file=os.path.abspath(args.to_file))

    return 0


if __name__ == '__main__':
    sys.exit(main())
