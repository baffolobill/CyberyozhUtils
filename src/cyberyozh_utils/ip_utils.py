import requests
import socket
import ipaddress


__doc__ = """Module contains ip-related functions"""


def get_public_ip():
    """
    Get the IP address available from the internet
    :return : public ip address
    """
    headers = {'Accept': 'application/json'}
    request = requests.get("https://ifconfig.co/", headers=headers)
    return request.json()["ip"]


def get_own_ip():
    """
    Get the IP address of an active Ethernet adapter
    """
    h_name = socket.gethostname()
    return socket.gethostbyname(h_name)


def is_valid_ip4(ip):
    """
    :param_name ip: IPv4 address string
    :return: True if IPv4 address is valid, False otherwise
    """
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False


def is_valid_ip6(ip):
    """
    :param_name ip: IPv6 address string
    :return: True if IPv6 address is valid, False otherwise
    """
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ValueError:
        return False


def is_valid_ip(ip):
    """
    :param_name ip: IPv4 or IPv6 address string
    :return: True if IPv4 or IPv6 address is valid, False otherwise
    """
    return is_valid_ip4(ip) or is_valid_ip6(ip)

