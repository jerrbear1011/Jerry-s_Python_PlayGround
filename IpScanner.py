from icmplib import ping, multiping, traceroute, resolve

ListOfIp = []
Network = input("Enter the network to scan (e.g., 192.168.1): ")
IP_Start = input("Enter first IP to scan:")
IP_End= input("Enter last IP to scan:")

def get_ip(IPad,IPs, IPe):
    IPs, IPe, IPad = int(IPs), int(IPe), str(IPad)
    address = IPad + str(IPs)
    print(ping(address, 4, 1, 2, None, None))



get_ip(Network, IP_Start, IP_End)