"""
Wake on lan component.
"""
import logging
import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.switch import (PLATFORM_SCHEMA)

from wol import Wol

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
