### JSON FILTERING -- SERVICES DATA

import json

servers_struc = {
 "rack": [
      { "server": { "dev_id": "S1" , "server_name": "svr1" , "domain": "biasc.be", "ip-address": "10.2.3.11" ,
                     "os": "linux"  , "server_type": "vm" ,
                     "services": [   
                       {"service": "ad" , "service_type": "vm", "protocol": "tcp", "port": "389"},
                       {"service": "dns", "service_type": "vm", "protocol": "udp", "port": "53"},
                       {"service": "ntp", "service_type": "vm", "protocol": "udp", "port": "123"} 
                    ]
                  }
      },
      { "server": { "dev_id": "S2" , "server_name": "svr2" , "domain": "biasc.be", "ip-address": "10.2.3.12" ,
                    "os": "linux"  , "server_type": "vm" ,
                    "services": [   
                      {"service": "flask", "service_type": "vm", "protocol": "tcp", "port": "8089"  }, 
                      {"service": "db"   , "service_type": "vm", "protocol": "tcp", "port": "1521"  } 
                    ]     
                 }
      },
      { "server": { "dev_id": "S3" , "server_name": "svr3" ,  "domain": "biasc.be" , "ip-address": "10.2.3.13",
                    "os": "linux"  , "server_type": "vm" ,
                    "services": [   
                      {"service": "dns" , "service_type": "vm", "protocol": "tcp", "port": "8089" }, 
                      {"service": "ntp" , "service_type": "vm", "protocol": "udp", "port": "123" },
                      {"service": "dhcp", "service_type": "docker", "protocol": "udp", "port": "67" }
                    ] 
                  }
      }
   ]
}

print('ip address 1st server:')
print(servers_struc["rack"][0]["server"]["ip-address"])

print('2nd port last server:')
print(servers_struc["rack"][-1]["server"]["services"][1]["port"])

print('name and ip address of all servers:')
for i in servers_struc["rack"]:
  print(i["server"]["server_name"] + " | " + i["server"]["ip-address"])

print('all ports of server:')
for i in servers_struc["rack"]:
  print(i["server"]["server_name"] + " | ")
  print(i["server"]["services"])