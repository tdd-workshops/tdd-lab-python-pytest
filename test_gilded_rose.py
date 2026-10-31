from gilded_rose import GildedRose, Item


def test_should_keep_item_name():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"
