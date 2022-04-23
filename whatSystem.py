#!/usr/bin/env python3
#coding: utf-8
#by https://github.com/Robbna
# ==================================
# python3 whatSystem.py [IP ADDRESS]
# ==================================


import subprocess
import sys

color_linux = '\033[1;93m'
color_info = '\033[1;92m'
color_error = '\033[1;91m'
color_windows = '\033[1;94m'
color_reset = '\033[0m'


def getIp():
    if len(sys.argv) != 2:
        print("\n"+color_error+"[!] Error"+color_reset)
        print("\n"+color_info+"USAGE:"+color_reset)
        print("\n\tpython3 " + sys.argv[0] + " [IP ADDRESS]\n")
        sys.exit(1)
    else:
        return sys.argv[1]


def getTTL(ip):
    output = subprocess.getoutput("ping -c 1 " + ip)

    for word in output.split():
        if("ttl" in word):
            number = int(word.split("=")[1])

            # LINUX TTL RANGE (0-64)
            if(0 <= number <= 64):
                print("\n[*] System: " + color_linux +
                      "LINUX" + color_reset + " (" + str(number) + " TTL)")

            # WINDOWS TTL RANGE (65-128)
            if(65 <= number <= 128):
                print("\n[*] System: " + color_windows +
                      "WINDOWS" + color_reset + " (" + str(number) + " TTL)")


if __name__ == "__main__":
    ipArgs = getIp()
    getTTL(ipArgs)
