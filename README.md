# Wake on lan for home assistant

This is a component for home assistant to perform a wake on lan action.

There is already an component, that I found after I wrote this component.
see https://www.home-assistant.io/integrations/wake_on_lan


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