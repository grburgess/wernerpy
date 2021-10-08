import numba as nb
import numpy as np

from .vector import Vector


class Cylinder:
    def __init__(self, radius: float, height: float, origin: Vector) -> None:

        self._radius: float = radius
        self._height: float = height

        self._origin: Vector = origin

    @staticmethod
    @nb.njit(
        "float64(float64, float64, float64, float64[:], float64[:])",
        cache=True,
    )
    def _intersect(
        radius: float,
        z0: float,
        z1: float,
        ray_origin: np.ndarray,
        ray_direction: np.ndarray,
    ):

        pass
