import ucapi, time

browser = ucapi.HeadlessAntiBot()
browser.launch("https://inori.wtf/")
time.sleep(10)
#browser.handle_alert()
browser.ss()
time.sleep(100)
print(browser.print_page_text())