import numpy as np
from dataclasses import field, dataclass
from typing import Optional, Iterable


@dataclass(frozen=False)
class Vector:

    x: float
    y: float
    z: float
    _internal_repr: Iterable = field(init=False)
    norm: Iterable = field(init=False)

    def __post_init__(self):

        self._internal_repr = np.array([self.x, self.y, self.z])

        denom = np.linalg.norm(self._internal_repr)

        if denom == 0:

            self.norm = np.array([0, 0, 0])

        else:

            self.norm = self._internal_repr / denom

    def dot(self, other: Vector) -> float:

        return np.dot(self._internal_reprnal, other._internal_repr)

    def __add__(self, other: Vector) -> Vector:

        new_vec = self._internal_repr + other._internal_repr

        return Vector(new_vec[0], new_vec[1], new_vec[2])

    def __sub__(self, other: Vector) -> Vector:

        new_vec = self._internal_repr - other._internal_repr

        return Vector(new_vec[0], new_vec[1], new_vec[2])

    def __mul__(self, factor: float) -> Vector:

        new_vec = factor * self._internal_repr

        return Vector(new_vec[0], new_vec[1], new_vec[2])

    def __rmul__(self, factor: float) -> Vector:

        new_vec = factor * self._internal_repr

        return Vector(new_vec[0], new_vec[1], new_vec[2])
