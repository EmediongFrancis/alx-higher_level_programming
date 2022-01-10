#!/usr/bin/python3
'''
    Script that fetches https://intranet.hbtn.io/status.
'''
import urllib.request

if __name__ == "__main__":
    fetchedUrl = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(fetchedUrl) as fu:
        fur = fu.read()
        print("Body response:")
        print("\t- type: {}".format(type(fur)))
        print("\t- content: {}".format(fur))
        print("\t- utf8 content: {}".format(fur.decode("utf-8")))
