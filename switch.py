"""
Wake on lan component.
"""
import logging
import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.switch import (PLATFORM_SCHEMA)
from wakeonlan import send_magic_packet, BROADCAST_IP, DEFAULT_PORT
from homeassistant.helpers.entity import Entity, ToggleEntity
from typing import Any, Dict, Iterable, List, Optional, Union

DOMAIN = 'wol'

CONF_HOST_MAC_ADDRESS = 'mac'
CONF_HOST_IP = 'ip'
CONF_HOST_PORT = 'port'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST_MAC_ADDRESS): cv.string,
    vol.Required(CONF_HOST_PORT, default=9): cv.port,
    vol.Optional(CONF_HOST_IP): cv.string,
})

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the device."""

    MAC = config[CONF_HOST_MAC_ADDRESS]
    IP = config[CONF_HOST_IP]
    PORT = config[CONF_HOST_PORT]
    async_add_entities([Wol(MAC, IP, PORT)], True)


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