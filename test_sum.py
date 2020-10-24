from sum import Sum

class TestSum:
    def test_additions_are_additive(self):
        sum = Sum()
        assert sum.addition(1, 1)  == 2, "expected two numbers to add up"
