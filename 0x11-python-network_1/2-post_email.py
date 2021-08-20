#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the
body of the response (decoded in utf-8)
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    with urllib.request.urlopen("http://0.0.0.0:5000/post_email", data) as req:
        print(req.read().decode('utf-8'))
