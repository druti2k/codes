import urllib.request

url = "ftp://ita.ee.lbl.gov/traces/calgary_access_log.gz"
output_file = "calgary_access_log.gz"

urllib.request.urlretrieve(url, output_file)

print("✅ Downloaded:", output_file)
