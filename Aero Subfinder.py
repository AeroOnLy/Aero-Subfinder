#!/usr/bin/python

from threading import Thread
from rich import print
from rich.progress import track
import requests, sys, getopt


class ResolveSubdomains(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        count = 0
        print("""[cyan][bold]
------------------------------------------
--------[ [red]Subdomains Finder Tool[cyan] ]--------
----[ [red]Waiting for Scanning Subdomain[cyan] ]----
------------------------------------------
        [cyan][bold]""")

        for i in track(lines):
            request_url = 'https://' + i.strip() + '.' + url
            try:
                request = requests.get(request_url)
                if request.status_code == 200:
                    print("[+] {} »» Subdomain Active! [green]✔".format(request_url))
                    count += 1

            except requests.ConnectionError:   
                print("[-] {} »» Subdomain Not Active! [red]✔".format(request_url))
                pass
        print("\n{} Subdomains Found".format(count))

        print("""
        [cyan][bold]
-------------------------------------------
-----------[ [red]Scanning Finished[cyan] ]-----------
------------[ [red]Scanner Stopped[cyan] ]------------
-------------------------------------------
        [cyan][bold]\n
        """)


if __name__ == "__main__":
    cli_arguments = sys.argv
    if len(cli_arguments) != 2:
        print("\n[bold]Usage:[/bold] python main.py --url=\"Destinated_URL\"\n")
        sys.exit(2)

    argument_list = cli_arguments[1:]
    short_args = "hu:"
    long_args = ["help", "url="]

    try:
        arguments, values = getopt.getopt(argument_list, short_args, long_args)
    except:
        print("\n[bold]Usage:[/bold] python main.py --url=\"Destinated_URL\"\n")
        sys.exit(2)

    for current_argument, current_value in arguments:
        if current_argument in ("-h", "--help"):
            print("\n[bold]Usage:[/bold] python main.py --url=\"Destinated_URL\"\n")

        elif current_argument in ("-u", "--url"):
            url = str(current_value)
            file = open('subdomains.txt', 'r')
            lines = file.readlines()

            thread = ResolveSubdomains()
            thread.start()
            thread.join()