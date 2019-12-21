# Wake on lan for home assistant

this is a component for home assistant to perform a wake on lan action.


# Device config
Add to your config file. 

`configuration.yaml`  

```yaml
switch:
  - platform: wol
    device_name: Your PC NAME
    mac: 00:80:41:ae:fd:7e 
```

---
| property | description |
| --- | --- |
| platform | define which platform or plugin should handle the switch config |
| device_name | reference name (used to generate the entity id) |
| mac | mac address of the computers networkcard that support wol |
| ip | local ip address of your computer, default is the broadcast ip |
| port | port will be used to send the wol signal | 