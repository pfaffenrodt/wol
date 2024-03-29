"""Wake on lan component"""
import logging
from typing import Any

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.switch import PLATFORM_SCHEMA
from homeassistant.helpers.entity import ToggleEntity
from wakeonlan import BROADCAST_IP, DEFAULT_PORT, send_magic_packet

DOMAIN = 'wol'

CONF_HOST_NAME = 'device_name'
CONF_HOST_MAC_ADDRESS = 'mac'
CONF_HOST_IP = 'ip'
CONF_HOST_PORT = 'port'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST_NAME, 'PC'): cv.string,
    vol.Required(CONF_HOST_MAC_ADDRESS): cv.string,
    vol.Required(CONF_HOST_PORT, default=DEFAULT_PORT): cv.port,
    vol.Optional(CONF_HOST_IP, default=BROADCAST_IP): cv.string,
})

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the device."""

    device_name = config.get(CONF_HOST_NAME)
    mac = config.get(CONF_HOST_MAC_ADDRESS)
    ip = config.get(CONF_HOST_IP)
    port = config.get(CONF_HOST_PORT)
    async_add_entities([WakeOnLanDevice(device_name, mac, ip, port)], True)


class WakeOnLanDevice(ToggleEntity):

    def __init__(self, name, mac_address, ip_address=BROADCAST_IP, port=DEFAULT_PORT):
        self.device_name = name
        self.mac_address = mac_address
        self.ip_address = ip_address
        self.port = port

    def send(self):
        """send and perform the wol"""
        send_magic_packet(self.mac_address, ip_address=self.ip_address, port=self.port)
        _LOGGER.info("Perform wake on lan to %s", self.name)

    @property
    def name(self):
        """Return the switch name."""
        return self.device_name

    @property
    def is_on(self) -> bool:
        """Return Always False. Cannot determine if device is on."""
        return False

    def turn_on(self, **kwargs: Any) -> None:
        """Turn the entity on."""
        self.send()

    def turn_off(self, **kwargs: Any) -> None:
        """ wol can not turn off the device """
