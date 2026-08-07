# botnet

cool botnet tool 

70 Powerful methods

100 Powerful bots

!GIVEAWAY!

NOTE: very few spots left and this tool is only free/public for a LIMITED TIME.
for more details Contact below .

<img width="596" height="360" alt="Screenshot 2026-05-23 8 09 32 PM" src="https://github.com/user-attachments/assets/dac4b04b-8a5f-4db9-b5ac-e895049d194a" />









## Install

### Linux / macOS
```bash
apt install git python3 python3-pip
git clone https://github.com/lemonaiddhater/botnet
cd botnet
pip3 install requests
python3 botnet.py
```

### Termux
```bash
pkg update && pkg upgrade
pkg install git python
git clone https://github.com/lemonaiddhater/botnet
cd botnet
pip install requests
python botnet.py
```

### iSH Shell
```bash
apk update
apk add python3 py3-pip git
git clone https://github.com/lemonaiddhater/botnet
cd botnet
pip3 install requests
python3 botnet.py

```

### Windows
```powershell
winget install -e --id Python.Python.3; winget install -e --id Git.Git
python --version
git --version
git clone https://github.com/lemonaiddhater/botnet
cd botnet
pip install requests
python botnet.py
```

## Requirements

- Python 3.7+
- requests 


## Attack methods etc

| Layer | Method          | Description                          | Plans                                      |
| ----- | --------------- | ------------------------------------ | ------------------------------------------ |
| L4    | ACK_FLOOD       | Floods target with ACK packets       | BASIC, PREMIUM, ENTERPRISE, LIFETIME       |
| L4    | ARP_FLOOD       | Saturates network with ARP requests  | ENTERPRISE, LIFETIME                       |
| L4    | DNS_ANY         | Floods using ANY record queries      | PREMIUM, ENTERPRISE, LIFETIME              |
| L4    | DNS_AXFR        | Abuses zone transfer requests        | ENTERPRISE, LIFETIME                       |
| L4    | DNS_BYPASS      | Bypasses DNS filtering layers        | ENTERPRISE, LIFETIME                       |
| L4    | DNS_FLOOD       | High-volume DNS query flood          | BASIC, PREMIUM, ENTERPRISE, LIFETIME       |
| L4    | DNS_IXFR        | Incremental zone transfer abuse      | ENTERPRISE, LIFETIME                       |
| L4    | DNS_TCP         | DNS flood over TCP connections       | PREMIUM, ENTERPRISE, LIFETIME              |
| L4    | ESP_FLOOD       | Floods with ESP protocol packets     | ENTERPRISE, LIFETIME                       |
| L4    | FTP_FLOOD       | Floods FTP with connection requests  | PREMIUM, ENTERPRISE, LIFETIME              |
| L4    | GRE_FLOOD       | Floods target via GRE tunnels        | ENTERPRISE, LIFETIME                       |
| L4    | ICMP_FLOOD      | Overwhelms target with ICMP pings    | BASIC, PREMIUM, ENTERPRISE, LIFETIME       |
| L4    | ICMP_LARGE      | Sends oversized ICMP echo packets    | PREMIUM, ENTERPRISE, LIFETIME              |
| L4    | NULL_FLOOD      | Sends packets with no flags set      | PREMIUM, ENTERPRISE, LIFETIME              |
| L4    | RAW_IP          | Sends raw crafted IP packets         | ENTERPRISE, LIFETIME                       |
| L4    | RST_FLOOD       | Terminates connections with RST spam | BASIC, PREMIUM, ENTERPRISE, LIFETIME       |
| L4    | SMTP_FLOOD      | Floods SMTP with mail requests       | PREMIUM, ENTERPRISE, LIFETIME              |
| L4    | SYN_ACK         | Floods with SYN-ACK packets          | BASIC, PREMIUM, ENTERPRISE, LIFETIME       |
| L4    | SYN_ACK_REFLECT | Reflects SYN-ACK at spoofed targets  | ENTERPRISE, LIFETIME                       |
| L4    | SYN_FLOOD       | Classic SYN handshake flood          | FREE, BASIC, PREMIUM, ENTERPRISE, LIFETIME |
| L4    | SYN_RAND_PORT   | SYN flood across randomized ports    | PREMIUM, ENTERPRISE, LIFETIME              |
| L4    | SYN_RST         | Pairs SYN and RST to disrupt sessions| PREMIUM, ENTERPRISE, LIFETIME              |
| L4    | TCP_AMP_HTTP    | HTTP-amplified TCP flood             | ENTERPRISE, LIFETIME                       |
| L4    | TCP_AMP_SSH     | SSH-amplified TCP flood              | ENTERPRISE, LIFETIME                       |
| L4    | TCP_BYPASS_PROXY| Routes traffic around proxy filters  | ENTERPRISE, LIFETIME                       |
| L4    | TCP_BYPASS_SSL  | Bypasses SSL inspection layers       | ENTERPRISE, LIFETIME                       |
| L4    | TCP_FLOOD       | Floods with raw TCP connections      | BASIC, PREMIUM, ENTERPRISE, LIFETIME       |
| L4    | TELNET_FLOOD    | Floods Telnet with connections       | PREMIUM, ENTERPRISE, LIFETIME              |
| L4    | UDP_AMP_DNS     | DNS-amplified UDP flood              | ENTERPRISE, LIFETIME                       |
| L4    | UDP_FLOOD       | High-volume raw UDP packet flood     | FREE, BASIC, PREMIUM, ENTERPRISE, LIFETIME |
| L4    | UDP_GAME        | Targets game server UDP protocols    | PREMIUM, ENTERPRISE, LIFETIME              |
| L4    | UDP_RAND_PORT   | UDP flood across randomized ports    | BASIC, PREMIUM, ENTERPRISE, LIFETIME       |
| L4    | UDP_VOIP        | Disrupts VoIP UDP traffic streams    | PREMIUM, ENTERPRISE, LIFETIME              |
| L4    | VLAN_FLOOD      | Floods with tagged VLAN frames       | ENTERPRISE, LIFETIME                       |
| L4    | XMAS_FLOOD      | Sends packets with all flags set     | PREMIUM, ENTERPRISE, LIFETIME              |
| L7    | DNS_AMP         | DNS-based amplification flood        | ENTERPRISE, LIFETIME                       |
| L7    | DNS_DRDOS       | Distributed DNS reflection flood     | ENTERPRISE, LIFETIME                       |
| L7    | DNS_DYNAMIC     | Dynamic record-based DNS flood       | PREMIUM, ENTERPRISE, LIFETIME              |
| L7    | DNS_FLOOD       | High-volume DNS query flood          | BASIC, PREMIUM, ENTERPRISE, LIFETIME       |
| L7    | DNS_NXDOMAIN    | Floods with invalid domain lookups   | PREMIUM, ENTERPRISE, LIFETIME              |
| L7    | DNS_REFLECT     | Reflects DNS traffic at target       | ENTERPRISE, LIFETIME                       |
| L7    | FTP_AUTH        | Hammers FTP with auth attempts       | PREMIUM, ENTERPRISE, LIFETIME              |
| L7    | HTTP2_FLOOD     | Multiplexed HTTP/2 stream flood      | ENTERPRISE, LIFETIME                       |
| L7    | HTTP3_FLOOD     | QUIC-based HTTP/3 flood              | ENTERPRISE, LIFETIME                       |
| L7    | HTTP_BYPASS     | Bypasses HTTP filtering rules        | PREMIUM, ENTERPRISE, LIFETIME              |
| L7    | HTTP_CACHE_BYPASS| Forces cache misses on every hit    | PREMIUM, ENTERPRISE, LIFETIME              |
| L7    | HTTP_COOKIE     | Floods with crafted cookie headers   | PREMIUM, ENTERPRISE, LIFETIME              |
| L7    | HTTP_DELETE     | Floods with HTTP DELETE requests     | BASIC, PREMIUM, ENTERPRISE, LIFETIME       |
| L7    | HTTP_GET        | High-rate HTTP GET request flood     | FREE, BASIC, PREMIUM, ENTERPRISE, LIFETIME |
| L7    | HTTP_HEAD       | Floods with HTTP HEAD requests       | FREE, BASIC, PREMIUM, ENTERPRISE, LIFETIME |
| L7    | HTTP_OPTIONS    | Floods with HTTP OPTIONS requests    | BASIC, PREMIUM, ENTERPRISE, LIFETIME       |
| L7    | HTTP_PATCH      | Floods with HTTP PATCH requests      | BASIC, PREMIUM, ENTERPRISE, LIFETIME       |
| L7    | HTTP_POST       | Floods with HTTP POST payloads       | FREE, BASIC, PREMIUM, ENTERPRISE, LIFETIME |
| L7    | HTTP_PUT        | Floods with HTTP PUT requests        | BASIC, PREMIUM, ENTERPRISE, LIFETIME       |
| L7    | HTTP_RANGE      | Exploits range header processing     | PREMIUM, ENTERPRISE, LIFETIME              |
| L7    | HTTP_REDIRECT   | Chains redirects to exhaust server   | PREMIUM, ENTERPRISE, LIFETIME              |
| L7    | HTTP_SLOW       | Slowly drains server connections     | PREMIUM, ENTERPRISE, LIFETIME              |
| L7    | HTTPS_FLOOD     | Floods over encrypted HTTPS channel  | PREMIUM, ENTERPRISE, LIFETIME              |
| L7    | HTTPS_RENEG     | Abuses TLS renegotiation overhead    | ENTERPRISE, LIFETIME                       |
| L7    | IMAP_AUTH       | Floods IMAP with login attempts      | PREMIUM, ENTERPRISE, LIFETIME              |
| L7    | MEMCACHED_AMP   | Memcached-based amplification flood  | ENTERPRISE, LIFETIME                       |
| L7    | NTP_AMP         | NTP monlist amplification flood      | ENTERPRISE, LIFETIME                       |
| L7    | POP3_AUTH       | Floods POP3 with auth requests       | PREMIUM, ENTERPRISE, LIFETIME              |
| L7    | RDP_LOGIN       | Hammers RDP with login attempts      | ENTERPRISE, LIFETIME                       |
| L7    | SMTP_AUTH       | Floods SMTP with auth handshakes     | PREMIUM, ENTERPRISE, LIFETIME              |
| L7    | SNMP_AMP        | SNMP-based amplification flood       | ENTERPRISE, LIFETIME                       |
| L7    | SSH_FLOOD       | Exhausts SSH with connection spam    | ENTERPRISE, LIFETIME                       |
| L7    | SSDP_AMP        | SSDP reflection amplification flood  | ENTERPRISE, LIFETIME                       |
| L7    | TELNET_LOGIN    | Hammers Telnet with login attempts   | ENTERPRISE, LIFETIME                       |
| L7    | WEBSOCKET       | Exhausts server via WebSocket spam   | PREMIUM, ENTERPRISE, LIFETIME              |




| Plan | Concurrents | Duration |
|------|---------|----------|
| FREE | 1/0   | 120s |
| BASIC | 20/0  | 300s |
| PREMIUM | 50/0 | 3600s |
| ENTERPRISE | 299 | 9500s |
| LIFETIME | Contact. | Contact. |


!GIVEAWAY!

NOTE: very few spots left and this tool is only free/public for a LIMITED TIME.
for more details Contact below .

## Contact

Discord: jugged.em

TikTok: @hitmyport53

Tiktok: @lolicake443

Telegram: @commitscrime


Telegram Serv: https://t.me/+E5x9WNEdu4ZmYTIx
