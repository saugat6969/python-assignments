import re
url=input("URL: ").strip()
# if matches=re.search(r"^https?://(wwww\.)?twitter\.com/(.+)$",url,re.IGNORECASE):
if matches:=re.search(r"^https?://(:?wwww\.)?twitter\.com/([a-z0-9_]+)$",url,re.IGNORECASE):

   print(f"username:"  ,matches.group(1))


# username=re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
# print(f"Username:{username}")
