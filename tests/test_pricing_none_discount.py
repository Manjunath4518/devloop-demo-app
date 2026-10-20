from store.pricing import apply_discount

def test_apply_discount_with_none_discount():
    # When discount_percent is None, should return price unchanged
    assert apply_discount(100, None) == 100.0