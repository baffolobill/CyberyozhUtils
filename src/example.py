import os
import sys
from cyberyozh_utils.time_utils import get_current_time
from cyberyozh_utils.ip_utils import get_public_ip


def main():
    print(f"Current Unix time: {get_current_time()}")
    print(f"My public IP: {get_public_ip()}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
