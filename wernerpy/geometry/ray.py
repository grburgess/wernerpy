import numpy as np
from dataclasses import field, dataclass
from typing import Optional, Iterable

from .vector import Vector


@dataclass(frozen=False)
class Ray:

    origin: Vector
    direction: Vector

    def position(self, n) -> Vector:

        return self.origin + self.direction * n


class Photon(Ray):
    def __init__(
        self,
        energy: float,
        origin: Vector,
        direction: Vector,
        parent: Optional["Photon"] = None,
    ):

        self._energy: float = energy
        self._parent: Optional["Photon"] = parent
        self._child: Optional["Photon"] = None

        super().__init__(origin=origin, direction=direction)

    @property
    def energy(self) -> float:
        return self._energy

    @property
    def parent(self) -> Optional["Photon"]:
        return self._parent

    @property
    def child(self) -> Optional["Photon"]:
        return self._child

    def interact(self):

        # compton scatter and create a new photon

        pass
