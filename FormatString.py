import sys

def format(format, string):
    if(format == "ELF64" or format == "ELF32"):
        if(format == "ELF64"):
            val = 16
        elif(format == "ELF32"):
            val = 8
        if((len(string)%val) != 0):
            print("[!] ERROR : invalid string")    
        else:
            d=[]
            for i in range(0,len(string),val):
                d.append(string[i:i+val])

            result=""
            for car in d:
                s=[]
                for i in range(0,len(car),2):
                    s.append(car[i:i+2])
                result+="".join(reversed(s))

            print("[+] Hex decoded :")
            print(result.decode('hex'))

    else:
        print("\n[!] Invalid format.\n")
        print("SUPPORTED FORMATS : ")
        print("* ELF64")
        print("* ELF32\n")

if(len(sys.argv) != 3):
    print("\n[!] USAGE : python formatString.py <format> <hex string (without spaces)>\n")
    print(" ---> [Example] : 'python formatString.py 32 44434241'")
    print(" ---> [Result] : 'ABCD'\n")
else:
    format(sys.argv[1], sys.argv[2])
