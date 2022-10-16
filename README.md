# Aero-Subfinder
Subdomain Finder Tools using Python

```
────╔═══╗────╔╗────────╔═══╗───────────────
────║╔═╗║────║║────────║╔═╗║───────────────
────║║─║║╔══╗║║───╔╗─╔╗║║─║║╔══╗╔═╗╔══╗────
────║║─║║║╔╗╗║║─╔╗║║─║║║╚═╝║║║═╣║╔╝║╔╗║────
────║╚═╝║║║║║║╚═╝║║╚═╝║║╔═╗║║║═╣║║─║╚╝║────
────╚═══╝╚╝╚╝╚═══╝╚═╗╔╝╚╝─╚╝╚══╝╚╝─╚══╝────
──────────────────╔═╝║─────────────────────
──────────────────╚══╝─────────────────────
```

# SubDomains Finder Tool 🔎
### What is sDFT?
**sDFT** is a tool written in Python that helps you find all accessible **sub-domains** for specific website. It is **simple** and **fast**.
<br><br>

### How it works?
The tool is very simple. All you have to do is specify **target website**. Then, **sDFT** will try to resolve every **subdomain** of specified website and print all that **resolves with success**.

### Installation
#### Linux
```BASH
sudo apt update
sudo apt install python3 python3-pip git # Install dependencies
git clone https://github.com/AeroOnLy/Aero-Subfinder.git # Clone sDFT repository
cd Aero-Subfinder
python3 -m pip install -r requirements.txt # Install pip dependencies
```

#### Windows
1. Download and install [Python 3](https://www.python.org/downloads/) (make sure to add Python and Pip to your PATH)
2. Download [the sDFT repository](https://github.com/AeroOnLy/Aero-Subfinder/archive/refs/heads/main.zip)
3. Extract the zip archive you've downloaded and open the folder in command prompt
4. In command prompt type `python -m pip install -r requirements.txt` to install required pip dependencies
5. After doing this, you can use the tool by typing `python Aero-Subfinder.py --url="your_targeted_website"`

### Usage
In command prompt type `python main.py --url="your_targeted_website"`, where "your_targeted_website" is a website you want to target.
[**Remember!** Use URL without `https://www` (for example: **github.com**)]

After that, **sDFT** will print all subdomains that resolves with success

