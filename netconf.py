from ncclient import manager

# Device connection details
router = {
    "host": "<TARGET IP ADDRESS>"
    "port": 830,
    "username": "<YOUR USERNAME>",
    "password": "<YOUR PASSWORD>",
    "hostkey_verify": False  # We'll skip strict key checking for the lab
}

# Define the XML filter
netconf_payload = """
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  <interface>
    <name>GigabitEthernet2</name>
  </interface>
</interfaces>
"""

# Establishing the NETCONF session
with manager.connect(**router) as m:
    # Apply the filter to m.get_config
    response = m.get_config(source="running", filter=('subtree', netconf_payload))
    
    print("Connected!")
    # print(m.server_capabilities)
    # schema = m.get_schema("ietf-interfaces") 
    print(response)
