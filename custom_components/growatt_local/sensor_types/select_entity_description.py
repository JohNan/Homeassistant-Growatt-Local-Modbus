"""Sensor Entity Description for the Growatt integration."""
from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.select import SelectEntityDescription


@dataclass
class GrowattSelectRequiredKeysMixin:
    """Mixin for required keys."""

    key: str
    options_dict: dict[int, str]


@dataclass
class GrowattSelectEntityDescription(SelectEntityDescription, GrowattSelectRequiredKeysMixin):
    """Describes Growatt sensor entity."""


