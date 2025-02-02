"""BleBox sensor entities."""

from homeassistant.components.sensor import SensorEntity

from . import BleBoxEntity, create_blebox_entities
from .const import BLEBOX_TO_HASS_DEVICE_CLASSES, BLEBOX_TO_UNIT_MAP


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up a BleBox entry."""

    create_blebox_entities(
        hass, config_entry, async_add_entities, BleBoxSensorEntity, "sensors"
    )


class BleBoxSensorEntity(SensorEntity, BleBoxEntity):
    """Representation of a BleBox sensor feature."""

    @property
    def state(self):
        """Return the state."""
        return self._feature.current

    @property
    def unit_of_measurement(self):
        """Return the unit."""
        return BLEBOX_TO_UNIT_MAP[self._feature.unit]

    @property
    def device_class(self):
        """Return the device class."""
        return BLEBOX_TO_HASS_DEVICE_CLASSES[self._feature.device_class]
