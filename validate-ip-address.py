class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if ":" in queryIP:
            ipv6 = queryIP.split(":")
            flag = 0
            if len(ipv6) == 8:
                for x in ipv6:
                    if 1 <= len(x) <= 4:
                        for i in x:
                            if not i.isnumeric():
                                if not (97 <= ord(i) <= 102 or 65 <= ord(i) <= 70):
                                    flag = 1
                    else:
                        flag = 1
            else:
                flag = 1
            if not flag:
                return "IPv6"
        elif "." in queryIP:
            ipv4 = queryIP.split(".")
            flag = 0
            print(ipv4)
            print(len(ipv4))
            if len(ipv4) == 4:
                for x in ipv4:
                    if x:
                        for i in x:
                            if not i.isnumeric():
                                flag = 1
                        if not flag:
                            if int(x) > 255 or (x[0] == "0" and len(x) > 1):
                                flag = 1
                    else:
                        flag = 1
            else:
                flag = 1
            if not flag:
                return "IPv4"
        return "Neither"