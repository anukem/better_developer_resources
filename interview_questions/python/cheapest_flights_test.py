from cheapest_flights import cheapestFlights


def test_one_stop():
    cheapestFlights([[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1) == 200


def test_no_stop():
    cheapestFlights([[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0) == 500


def test_path_that_leads_no_where():
    cheapestFlights([[0, 4, 120], [1, 2, 100]], 0, 2, 0) == -1


def test_no_solution():
    cheapestFlights([[1, 2, 100]], 0, 2, 0) == -1
