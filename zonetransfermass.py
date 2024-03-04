import dns.query
import dns.zone

# List of domain names
domains = [
    'admin.inlanefreight.htb',
    'ftp.admin.inlanefreight.htb',
    'careers.inlanefreight.htb',
    'dc1.inlanefreight.htb',
    'dc2.inlanefreight.htb',
    'internal.inlanefreight.htb',
    'admin.internal.inlanefreight.htb',
    'wsus.internal.inlanefreight.htb',
    'ir.inlanefreight.htb',
    'dev.ir.inlanefreight.htb',
    'resources.inlanefreight.htb',
    'securemessaging.inlanefreight.htb',
    'test1.inlanefreight.htb',
    'us.inlanefreight.htb',
    'cluster14.us.inlanefreight.htb',
    'messagecenter.us.inlanefreight.htb',
    'ww02.inlanefreight.htb',
    'www1.inlanefreight.htb'
]

# Nameserver IP address

nameserver_ip = '10.129.48.177'

# Perform zone transfer and check for TXT record
for domain in domains:
    try:
        zone = dns.zone.from_xfr(dns.query.xfr(nameserver_ip, domain))
        txt_records = zone.find_rdataset(domain, dns.rdatatype.TXT)
        if txt_records:
            print(f"Domain: {domain} has TXT record: {txt_records}")
        else:
            print(f"Domain: {domain} does not have a TXT record")
    except dns.exception.FormError:
        print(f"Zone transfer failed for domain: {domain}")


