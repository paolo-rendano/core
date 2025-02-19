"""Contains base entity classes for Starlink entities."""
from __future__ import annotations

from homeassistant.helpers.entity import DeviceInfo, Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import StarlinkUpdateCoordinator


class StarlinkEntity(CoordinatorEntity[StarlinkUpdateCoordinator], Entity):
    """A base Entity that is registered under a Starlink device."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: StarlinkUpdateCoordinator,
    ) -> None:
        """Initialize the device info and set the update coordinator."""
        super().__init__(coordinator)
        self._attr_device_info = DeviceInfo(
            identifiers={
                (DOMAIN, self.coordinator.data.status["id"]),
            },
            sw_version=self.coordinator.data.status["software_version"],
            hw_version=self.coordinator.data.status["hardware_version"],
            name="Starlink",
            configuration_url=f"http://{self.coordinator.channel_context.target.split(':')[0]}",
            manufacturer="SpaceX",
            model="Starlink",
        )
