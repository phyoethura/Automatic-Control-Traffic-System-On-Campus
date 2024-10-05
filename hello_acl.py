from netmiko import ConnectHandler, exceptions
from rich import print as rprint
from projj.acl__inventory  import ACL_DENIED_INVENTORY
import denied_texts as hello
from projj.unnecessary.status import R1_STATUS


rprint(R1_STATUS)
rprint(f"---------------------{ACL_DENIED_INVENTORY[0]['host']}-------------------")
connection = ConnectHandler(
        device_type = "cisco_ios",
        host = ACL_DENIED_INVENTORY[0]["host"],
        username = 'hello',
        password = 'hello',
        secret = 'hello',
        port = 22
        
    )
connection.enable()
connection.config_mode()
which_prompt = connection.find_prompt()
print(which_prompt)

output = connection.send_config_from_file(config_file='./permitted_texts/R1-PC3-cancel.txt')

R1_STATUS[0]["R3"]="permitted"

rprint(R1_STATUS)
    
rprint(output)



connection.disconnect()





