# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: .venv (3.14.4)
#     language: python
#     name: python3
# ---

# %% [markdown] id="0rq-l19mEOdL"
# # Demo: HTTP and Networked Programs

# %% [markdown]
# ## Demo Part 0: HTTP
#
# ```bash
# echo '<h1>Hello HTTP</h1><p>This page comes from a local server.</p><p><a href="page2.html">Go to Page 2</a></p>' > index.html
#
# echo '<h1>This is Page 2</h1><p>You opened this page through a link or direct URL.</p><p><a href="index.html">Back to Home</a></p>' > page2.html
#
# python3 -m http.server 8000
# ```

# %% [markdown]
# ## Demo Part 0.5: Sockets

# %%
import socket as sc

s = sc.socket()
s.connect(("google.com", 80))
print("Đã kết nối.")
s.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = s.recv(3000) # Nhận tối đa 3000 bytes
print(response.decode())

print("Đang đóng kết nối.")
s.close()

# %% [markdown] id="vemk5ewZDqKT"
# ## Demo Part 1: "Hacking" HTTP with Bash
#
# Before using Python, here is the simplicity of the HTTP protocol using a terminal. This shows that HTTP is just a set of rules (a protocol) for exchanging text.
#
# Linux Bash Command:
#
# ```bash
# # Use telnet to manually connect to a web server on port 80
# telnet data.pr4e.org 80
# ```
#
# Once connected, type the following (and press Enter twice):
#
# ```bash
# GET http://data.pr4e.org/romeo.txt HTTP/1.0
# ```
#
# Notice the HTTP Response Headers (Date, Server, Content-Type) that appear before the actual file content ("But soft what light...")

# %% [markdown] id="TzsPYPxfDCUS"
# ## Demo Part 2: The "World’s Simplest Web Browser" (Sockets)
#
# Python can replicate the manual `telnet` process using the low-level `socket` library.
#
# Notice the transition from Strings to Bytes using `encode()` and `decode()`, which is a requirement for network communication in Python 3.

# %% colab={"base_uri": "https://localhost:8080/"} id="mnBD-23A-cV4" outputId="b160ed0d-ccbf-4816-e8ac-38f8207b21ad"
import socket

# Create a TCP socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# Prepare the GET command (must be encoded to bytes)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\r\n\r'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    # Decode bytes back to string for printing
    print(data.decode(), end='')

mysock.close()


# %% [markdown] id="NOP2cKLiDgmL"
# ## Demo Part 3: High-Level Retrieval with `urllib`
#
# This is the Python way to retrieve data. The `urllib` library handles the socket details and headers automatically, making a web page look like a local file.
#
# This script retrieves the text and performs a word frequency count in just a few lines.
#

# %% colab={"base_uri": "https://localhost:8080/"} id="Wha9FpHOFgeM" outputId="9d20e4fe-0051-4ee1-c765-2f1f1ea0263a"
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    # Decode line and split into words
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)


# %% [markdown] id="fvliANstFnie"
# ## Demo Part 4: Retrieving Binary Files (Images)
#
# This is how to download an image. Since images can be large, this demonstrates downloading in chunks (buffers) to avoid crashing the computer's memory.

# %% colab={"base_uri": "https://localhost:8080/"} id="ZQ34cD4gF5IB" outputId="1789f724-622a-4996-ef12-4fbb1ac235b4"
import urllib.request

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover.jpg', 'wb') # 'wb' means write-binary
size = 0

while True:
    info = img.read(100000) # Read 100,000 characters at a time
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()


# %% [markdown] id="kAs3CXp2F-AB"
# ## Demo Part 5: Web Scraping with BeautifulSoup
#
# This is how to scrape a page to extract specific information, such as all links (`<a>` tags) on a website.
#
# Remark that BeautifulSoup is essential because it can handle broken or poorly formatted HTML that would break a standard XML parser
#

# %%
# %pip install bs4

# %% colab={"base_uri": "https://localhost:8080/"} id="VPJNXkF8GQrY" outputId="0a1b5427-1b19-488c-9808-42f4287c5e66"
import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors for HTTPS sites
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.dr-chuck.com/'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))


# %% [markdown]
# ### Đi theo link qua nhiều trang

# %%
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
for i in range(4):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    url = soup('a')[2].get('href')       # lấy link thứ 3
    print('Đi tới:', url)

# %% [markdown]
# ### Trích dữ liệu từ các thẻ

# %%
url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

nums = [int(tag.contents[0]) for tag in soup('span')]

for tag in soup('span'):
    print(tag.contents)
print(nums)
print('Số lượng:', len(nums), '| Tổng:', sum(nums))

# %%
url = "https://quotes.toscrape.com/"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

quotes = soup('div', class_ = 'quote')
# quotes = soup('span')
# print(quotes)
# print(type(quotes))
for quote in quotes:
    # text = quote.find('span', class_ = 'text')
    # author = quote.find('small', class_ = 'author')
    text = quote.find('span', class_ = 'text')
    author = quote.find('small', class_ = 'author')
    print(f'{text} - {author}')

# %% [markdown] id="e0ZK0LXOHRIn"
# ## Demo Part 6: Bash Alternatives (curl & wget)
#
# Common Linux utilities perform these exact same networked tasks.
#
# Linux Bash Commands:
#
# ```bash
# # Use curl to download a file and save it locally
# curl -O http://www.py4e.com/cover.jpg
#
# # Use wget to retrieve a remote file
# wget http://www.py4e.com/cover.jpg
# ```
