from wakeonlan import send_magic_packet, BROADCAST_IP, DEFAULT_PORT
from homeassistant.helpers.entity import Entity, ToggleEntity
from typing import Any, Dict, Iterable, List, Optional, Union


class Wol(ToggleEntity):

    def __init__(self, name, mac_address, ip_address=BROADCAST_IP, port=DEFAULT_PORT):
        self.device_name = name
        self.mac_address = mac_address
        self.ip_address = ip_address
        self.port = port

    def send(self):
        send_magic_packet(self.mac_address, ip_address=self.ip_address, port=self.port)

    @property
    def name(self):
        """Return the switch name."""
        return self.device_name

    @property
    def is_on(self) -> bool:
        """Return True if entity is on."""
        return False

    def turn_on(self, **kwargs: Any) -> None:
        """Turn the entity on."""
        self.send()

    def turn_off(self, **kwargs: Any) -> None:
        """ do nothing """