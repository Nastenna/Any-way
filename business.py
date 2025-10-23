import math
from typing import List, TYPE_CHECKING, Union
from ..models import Point, Route, RouteNode

if TYPE_CHECKING:
    from . import graph

EARTH_RADIUS = 6372.800   # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
KMH_TO_MS_MULTIPLIER = 3.6
WALK_SPEED = 2.5 * KMH_TO_MS_MULTIPLIER


def is_routes_equal(stored: List[RouteNode], new: 'graph.GraphRoute') -> bool:
    if len(stored) != len(new.nodes):
        return False
    for i in range(len(stored)):
        if new.nodes[i].point != stored[i].point:
            return False
    return True


def existed_routes(new_routes: List['graph.GraphRoute']):
    result = list()
    old_routes = {x: RouteNode.objects.get(route_id=x.id).order_by('number_in_route') for x in Route.objects.all()}

    for nr in new_routes:
        pass


def find_routes(points: List[Point], entry_point: Point, route_time: Union[int, float], required_point: Point = None):
    route_length = route_time * WALK_SPEED
    routes = graph.find_routes(points=points, entry_point=entry_point, route_length=route_length,
                               required_point=required_point)



