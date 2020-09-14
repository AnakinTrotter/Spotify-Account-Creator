from browser import Browser
from generator import AccountGenerator


def run():
    ans = ""
    proxy_type = ""
    country = ""
    ping = -1
    while ans != "y" and ans != "n":
        ans = input("Would you like to update your proxies? (y/n)\n").lower()
        if ans == "y":
            while ans != "http" and ans != "socks4" and ans != "socks5":
                ans = input("What type of proxy would you like to use? (http, socks4, socks5)\n").lower()
                proxy_type = ans
            while ans != "y":
                ans = input("What is the abbreviation for the country you will use the account in? (ex: US)\n").upper()
                country = ans
                ans = input("Is your country 100% accurate? (y/n)\n").lower()
            ans = 0
            while ans < 1000 or ans > 10000:
                ans = input("What should the max ping be for the proxies? [1000, 10000] (higher ping = more proxies)\n")
                try:
                    ans = int(ans)
                    ping = ans
                except ValueError:
                    print("Please enter a valid integer.")
            get_proxies(proxy_type=proxy_type, country=country, ping=ping)
            ans = "y"
        elif ans == "n":
            while ans != "http" and ans != "socks4" and ans != "socks5":
                ans = input("What type of proxy would you like to use? (http, socks4, socks5)\n").lower()
                proxy_type = ans
            get_proxies(proxy_type=proxy_type, use_new=False)
            ans = "y"

    ans = ""
    while ans != "n":
        ans = input("How many accounts should be generated? [0, 1000]\n")
        try:
            gen_accounts(proxy_type, int(ans))
        except ValueError:
            print("Please enter a valid integer.")
        ans = input("\nWould you like to go again? (y/n)\n").lower()
        if ans == "y":
            run()


def gen_accounts(proxy_type, num):
    if num < 0 or num > 1000:
        raise ValueError
    gen = AccountGenerator()
    gen.run(proxy_type=proxy_type, account_num=num)
    gen.setup()
    gen.multi_threading()


def get_proxies(proxy_type="http", country="US", ping=3000, use_new=True):
    if use_new:
        print("Connecting to host: https://proxyscrape.com/free-proxy-list")
        web = Browser()
        web.scrape_proxies(proxy_type, country, ping)

    source_name = proxy_type + "_proxies.txt"
    source_file = open(source_name)
    source_proxies = source_file.read()
    source_file.close()

    dest_name = "Proxies.txt"
    dest_file = open(dest_name, "w")
    dest_file.write(source_proxies)
    dest_file.close()

    if use_new:
        print("\nScraped:")
        print(source_proxies)


if __name__ == '__main__':
    print("\n\n\n")
    run()
    print("\n\n\n")
