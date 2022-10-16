#!/usr/bin/python

from threading import Thread
from rich import print
from rich.progress import track
import requests, sys, getopt

class ResolveSubdomains(Thread):
    def __init__(self):
        Thread.__init__(self)

    # fungsi untuk memindai subdomain
    def run(self):
        count = 0
        print("""[cyan][bold]
------------------------------------------
--------[ [red]Subdomains Finder Tool[cyan] ]--------
----[ [red]Waiting for Scanning Subdomain[cyan] ]----
------------------------------------------
        [cyan][bold]""")
        
        # loop untuk mendapatkan URL
        for i in track(lines):
            
            #membuat url dengan meletakkan subdomain satu per satu
            request_url = 'https://' + i.strip() + '.' + url
            
            # menggunakan tangkapan blok "try" untuk menghindari kerusakan program
            try:
                
                # mengirim permintaan ke url
                request = requests.get(request_url)
                
                # jika setelah meletakkan subdomain satu per satu url valid lalu cetak urlnya
                if request.status_code == 200:
                    print("[+] {} »» Subdomain Active! [green]✔".format(request_url))
                    count += 1
                    
            # jika url tidak valid maka berikan
            except requests.ConnectionError:   
                print("[-] {} »» Subdomain Not Active! [red]✘".format(request_url))
                pass
        #Total Subdomain yang Ditemukan
        print("\n{} Subdomains Found".format(count))

        print("""
        [cyan][bold]
-------------------------------------------
-----------[ [red]Scanning Finished[cyan] ]-----------
------------[ [red]Scanner Stopped[cyan] ]------------
-------------------------------------------
        [cyan][bold]\n
        """)

# fungsi utama
if __name__ == "__main__":
    cli_arguments = sys.argv
    
    # contoh memasukkan url
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

        # input url
        elif current_argument in ("-u", "--url"):
            url = str(current_value)
            # membuka file teks subdomain yang tersimpan
            file = open('subdomains.txt', 'r')
            #membaca file
            lines = file.readlines()

            thread = ResolveSubdomains()
            thread.start()
            thread.join()
