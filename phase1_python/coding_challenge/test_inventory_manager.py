import json
from pathlib import Path

import pytest

from inventory_manager import Product


@pytest.fixture()
def tmp_inventory_dir(tmp_path, monkeypatch):
    # Make Product read/write relative to this temp directory.
    monkeypatch.chdir(tmp_path)
    return tmp_path


def write_json(path: Path, data):
    path.write_text(json.dumps(data), encoding="utf-8")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_load_products_missing_file_returns_empty(tmp_inventory_dir):
    p = Product()
    assert p.load_products() == []


def test_load_products_invalid_json_returns_empty(tmp_inventory_dir):
    inv = Path("inventory.json")
    inv.write_text("{not json", encoding="utf-8")

    p = Product()
    assert p.load_products() == []


def test_load_products_empty_file_returns_empty(tmp_inventory_dir):
    inv = Path("inventory.json")
    inv.write_text("", encoding="utf-8")

    p = Product()
    assert p.load_products() == []


def test_low_stock_report_filters_by_quantity():
    p = Product()
    products = [
        {"Id": "1", "Quantity": 4},
        {"Id": "2", "Quantity": 5},
        {"Id": "3", "Quantity": 1},
    ]
    assert p.low_stock_report(products, threshold=5) == [products[0], products[2]]


def test_add_product_creates_inventory_file(tmp_inventory_dir):
    p = Product()
    res = p.add_product("1", "Widget", 12.5, 3)

    assert res is None
    inv = read_json(Path("inventory.json"))
    assert isinstance(inv, list)
    assert inv == [
        {"Id": "1", "Name": "Widget", "Price": 12.5, "Quantity": 3}
    ]


def test_add_product_rejects_duplicate_id(tmp_inventory_dir, capsys):
    p = Product()
    p.add_product("1", "Widget", 12.5, 3)
    res = p.add_product("1", "Widget2", 9.99, 10)

    assert res == " iD 1 already exist "

    # Ensure inventory still has only the original product
    inv = read_json(Path("inventory.json"))
    assert len(inv) == 1
    assert inv[0]["Name"] == "Widget"


def test_remove_product_decreases_quantity(tmp_inventory_dir):
    p = Product()
    p.add_product("1", "Widget", 10, 10)
    res = p.remove_product("1", 6)

    assert res is None
    inv = read_json(Path("inventory.json"))
    assert inv[0]["Quantity"] == 4


def test_remove_product_not_enough_quantity_returns_message(tmp_inventory_dir):
    p = Product()
    p.add_product("1", "Widget", 10, 3)
    res = p.remove_product("1", 5)

    assert res == ' only 3 left '


def test_remove_product_missing_id_creates_low_stock_report_if_applicable(tmp_inventory_dir):
    p = Product()
    # Create an inventory where a low-stock product exists.
    p.add_product("1", "LowWidget", 10, 1)
    p.add_product("2", "HighWidget", 10, 10)

    res = p.remove_product("999", 1)
    assert res == " Product with ID 999 not found "

    low = read_json(Path("low_stock_report.json"))
    assert low == [{"Id": "1", "Name": "LowWidget", "Price": 10.0, "Quantity": 1}]


def test_upgrade_quantity_increases_quantity(tmp_inventory_dir):
    p = Product()
    p.add_product("1", "Widget", 10, 2)
    res = p.upgrade_quantity("1", 5)
    assert res is None

    inv = read_json(Path("inventory.json"))
    assert inv[0]["Quantity"] == 7


def test_upgrade_quantity_missing_id_returns_message(tmp_inventory_dir):
    p = Product()
    p.add_product("1", "Widget", 10, 2)

    res = p.upgrade_quantity("999", 5)
    assert res == " Product with ID 999 not found "

