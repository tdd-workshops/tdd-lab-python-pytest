from pathlib import Path

from gilded_rose import GildedRose, Item


def test_should_match_thirty_days_of_texttest_output():
    items = [
        Item("+5 Dexterity Vest", 10, 20),
        Item("Aged Brie", 2, 0),
        Item("Elixir of the Mongoose", 5, 7),
        Item("Sulfuras, Hand of Ragnaros", 0, 80),
        Item("Sulfuras, Hand of Ragnaros", -1, 80),
        Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
        Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
        Item("Conjured Mana Cake", 3, 6),
    ]
    gilded_rose = GildedRose(items)
    lines = ["OMGHAI!"]

    for day in range(31):
        lines.append(f"-------- day {day} --------")
        lines.append("name, sellIn, quality")
        lines.extend(str(item) for item in items)
        lines.append("")
        gilded_rose.update_quality()

    expected = (Path(__file__).parent / "texttests" / "ThirtyDays" / "stdout.gr").read_text(
        encoding="utf-8"
    )
    assert "\n".join(lines) + "\n" == expected
