# Following URLs are in string getting handled
# "https://www.bit.ly/3rIRzga"
# "www.fb.com"
# "www.google.com"
# "yahoo.com"
# "chatgpt.co.in/jkl/sd7fsd"

string = "National Jobs Mela live hai! 10th pass, 12th pass aur Freshers ke liye 45000 tak ki Jobs! Abhi apply karo Vi App par Bilkul FREE! Click : https://www.bit.ly/3rIRzga www.fb.com asbdaosfblk asfjnblkdf kdnsflk www.google.com  yahoo.com chatgpt.co.in/jkl/sd7fsd"

string = string.split()
print(string)

url_pattern = re.compile(r'(https?://)?(www\.)?\w+\.\w{2,3}(/\w+)?')
url = []

for item in string:
    has_url = bool(re.search(url_pattern, item))
    if has_url:
        url.append(item)

print(has_url)
print(url)
