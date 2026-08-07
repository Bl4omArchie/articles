# Introduction to Ivre framework

IVRE (French: Instrument de veille sur les réseaux extérieurs) or DRUNK (Dynamic Recon of UNKnown networks) is an open-source framework for network recon, written in Python. It relies on open-source tools, such as nmap, masscan etc, to gather intelligence from the network, actively or passively.

# List of supported tools

As IVRE is relying on external tools, let's see which tools are natively supported. This list isn't exhaustive.

| Name | Description | URL |
| :---: | :--- | :---: |
| Nmap | Network scanner used for host discovery, port scanning, service/version detection, OS fingerprinting, NSE scripting, and security auditing. | [link](https://nmap.org) |
| Masscan | Ultra-fast asynchronous port scanner designed for Internet-scale scans, capable of scanning millions of hosts per second. | [link](https://github.com/robertdavidgraham/masscan) |
| Dismap | High-performance asset identification and service fingerprinting tool focused on rapid Internet asset mapping and banner collection. | [link](https://github.com/zhzyker/dismap) |
| Zeek | Network traffic analysis and security monitoring framework used for deep protocol inspection, event logging, and behavioral analysis. | [link](https://zeek.org) |
| ZGrab2 | Application-layer banner grabber used to collect protocol metadata from exposed services. | [link](https://github.com/zmap/zgrab2) |
| httpx | HTTP probing toolkit used to identify web services, technologies, titles, TLS data, and response fingerprints. | [link](https://github.com/projectdiscovery/httpx) |
| dnsx | Fast DNS toolkit for resolution, brute force, wildcard filtering, and DNS probing. | [link](https://github.com/projectdiscovery/dnsx) |
