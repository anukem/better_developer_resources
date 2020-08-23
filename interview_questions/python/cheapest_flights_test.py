from cheapest_flights import cheapestFlights


def test_one_stop():
    cheapestFlights([[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1) == 200


def test_no_stop():
    cheapestFlights([[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0) == 500
