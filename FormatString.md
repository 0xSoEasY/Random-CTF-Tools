# Format string tool

This tool was born because of the format string exploits used in pwn.
Actually it support ELF32 and ELF64 formats but, who knows, maybe more in the future...

## Example of use
```bash
$ python formatString.py ELF32 47414c465f74497b6b7230777d217300
[+] Hex decoded :
FLAG{It_w0rks!}
```

## Code
```python
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
