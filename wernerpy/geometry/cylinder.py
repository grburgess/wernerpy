import numba as nb
import numpy as np

from .vector import Vector
from .ray import Ray

class Cylinder:
    def __init__(
        self,
        radius: float,
        height: float,
        origin: Vector,
        oreintation: Vector = Vector(0.0, 0.0, 1.0),
    ) -> None:
    """

        :param radius: 
        :type radius: float
        :param height: 
        :type height: float
        :param origin: 
        :type origin: Vector
        :param oreintation: 
        :type oreintation: Vector
        :param 0.0: 
        :type 0.0: 
        :param 1.0): 
        :type 1.0): 
        :returns: 

        """
        self._radius: float = radius
        self._height: float = height

        self._origin: Vector = origin

        self._oreintation: Vector = oreintation

        if self._oreintation == Vector(0.0, 0.0, 1.0):

            self._do_build_rot_matrix: bool = False

        else:

            self._do_build_rot_matrix: bool = True

    def intersect(self, ray: Ray):

        return self._intersect(
            self._origin.to_numpy(),
            self._height,
            self._radius,
            self._oreintation.to_numpy(),
            ray.origin.to_numpy(),
            ray.direction.to_numpy(),
            self._do_build_rot_matrix,
        )

    @staticmethod
    # @nb.njit()
    def _intersect(
        center: np.ndarray,
        height: float,
        radius: float,
        oreintation: np.ndarray,
        ray_origin: np.ndarray,
        ray_direction: np.ndarray,
        build_rot_matrix: bool,
    ):

        if build_rot_matrix:
            pass
        #             cos_fi = normalize(axis)[2]
        #             rot_axis = np.array([normalize(axis)[1], -normalize(axis)[0], 0])
        #             sin_fi = np.linalg.norm(rot_axis)
        #             R = rot(rot_axis, sin_fi, cos_fi)

        #             ray_direction2=np.matmul(R, (ray_direction))
        #             ray_origin2=np.matmul(R, (ray_origin - center))

        else:

            shifted_ray_origin = ray_origin - center

            shifted_ray_origin_norm_2 = np.linalg.norm(shifted_ray_origin) ** 2

            ray_direction_norm_2 = np.linalg.norm(ray_direction) ** 2
            ray_direction_fabs_2 = np.fabs(ray_direction) ** 2

            shifted_ray_origin_fabs_2 = np.fabs(shifted_ray_origin) ** 2

            a = ray_direction_norm_2 - ray_direction_fabs_2[2]
            b = (
                2 * np.dot(ray_direction, shifted_ray_origin)
                - 2 * ray_direction[2] * shifted_ray_origin[2]
            )
            c = (
                shifted_ray_origin_norm_2
                - shifted_ray_origin_fabs_2[2]
                - radius ** 2
            )

            print(a, b, c)

            delta = b ** 2 - 4 * a * c
            print(delta)

            if delta > 0:
                t1 = (-b + np.sqrt(delta)) / (2 * a)
                t2 = (-b - np.sqrt(delta)) / (2 * a)

                z1 = shifted_ray_origin[2] + t1 * ray_direction[2]
                z2 = shifted_ray_origin[2] + t2 * ray_direction[2]

                if (z1 > -height / 2 and z1 < height / 2) and (
                    z2 > -height / 2 and z2 < height / 2
                ):
                    if t1 > 0 and t2 > 0:
                        return min(t1, t2)

                elif z1 > -height / 2 and z1 < height / 2:
                    if t1 > 0:
                        return t1
                elif z2 > -height / 2 and z2 < height / 2:
                    if t2 > 0:
                        return t2

            else:

                return -np.inf


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
