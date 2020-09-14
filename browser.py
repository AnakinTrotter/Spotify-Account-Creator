from selenium import webdriver
import os


class Browser:
    PATH = "C:/Program Files (x86)/chromedriver.exe"

    def __init__(self):
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        root_dir = os.path.join(root_dir, "Spotify-Account-Creator")
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("prefs", {
            'download.default_directory': root_dir,
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
        })
        opt.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path=self.PATH, chrome_options=opt)
        self.driver.maximize_window()

    def scrape_proxies(self, proxy_type, country, ping):
        ping = str(ping)
        url = "https://api.proxyscrape.com/?request=getproxies&proxytype=" + proxy_type + "&timeout="
        url += ping + "&country=" + country + "&ssl=all&anonymity=all"
        self.driver.get(url)
