from check_permutation import check_permutation, check_permutation_with_map


def test_check_valid_permutation():
    assert check_permutation("some", "omes") is True
    assert check_permutation_with_map("some", "omes") is True


def test_not_valid_permutation():
    assert check_permutation("some", "oms") is False
    assert check_permutation_with_map("some", "oms") is False


def test_no_change():
    assert check_permutation("some", "some") is True
    assert check_permutation_with_map("some", "some") is True
