import qrcode

channel = "https://www.javatpoint.com/generate-a-qr-code-using-python"
url = qrcode.make(channel)
url.save("subscribe.png")
