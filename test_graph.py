import pytest

from guide.logic.graph import *


class Point:
    def __init__(self, x_coord: float, y_coord: float):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __str__(self):
        return f'Point({self.x_coord}, {self.y_coord})'


def test_simple_route():
    points = [Point(0.0, 0.0),
              Point(0.0, 1.0)]

    routes = find_routes(points, points[0], 111227)

    assert len(routes) == 1
    assert 111227*0.8 < routes[0].length() < 111227
    assert len(routes[0].nodes) == 2


def test_three_point_route():
    points = [Point(0.0, 0.0), Point(0.0, 1.0), Point(1.0, 0.0)]

    routes = find_routes(points, points[0], 268530)
    assert len(routes) == 2

    for r in routes:
        assert 268530 * 0.8 < r.length() < 268530
        assert len(r.nodes) == 3
    assert routes[0].length() == routes[1].length()

    routes = find_routes(points, points[0], 111227)

    assert len(routes) == 2
    for r in routes:
        assert 111227 * 0.8 < r.length() < 111227
        assert len(r.nodes) == 2
