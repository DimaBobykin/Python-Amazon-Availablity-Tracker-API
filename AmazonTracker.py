from requests_html import HTMLSession

def ProductCheck(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    Stock = r.html.xpath('//*[@id="availability"]', first=True).text
    if "Available from these sellers" in Stock or "Currently unavailable" in Stock:
        return("Unavailable")
    else:
        return("Available")
    
if __name__ == "__main__":
    inputVar = input()
    ProductCheck(inputVar)
