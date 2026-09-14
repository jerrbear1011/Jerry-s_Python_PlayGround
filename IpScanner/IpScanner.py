from icmplib import ping, multiping, traceroute, resolve

ListOfIp = []
Network = input("Enter the network to scan (e.g., 192.168.1): ")
IP_Start = input("Enter first IP to scan:")
IP_End= input("Enter last IP to scan:")
attempts = input("Enter number of attempts to ping each IP: ")

def get_ip(IPad,IPs, IPe, attempts):
    IPs, IPe, IPad, attempts = int(IPs), int(IPe), str(IPad), int(attempts)


    for IPs in range(IPs, IPe + 1):
        address = IPad + str(IPs)
        new = ""
        new = str(ping(address, attempts, 1, 2, None, None))
        #print(new)
        return ListOfIp.append(new)



get_ip(Network, IP_Start, IP_End, attempts)

print(ListOfIp)