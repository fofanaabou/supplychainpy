from decimal import Decimal


class MonteCarloWindow:

    def __init__(self):
        self._sku_id = ""
        self._lead_time = 0
        self._opening_stock = 0
        self._demand = 0
        self._closing_stock = 0
        self._backlog = 0
        self._holding_cost = Decimal('0.0')
        self._shortage_cost = Decimal('0.0')
        self._po_raised_flag = False
        self._purchase_order_raised_qty = 0
        self._purchase_order_receipt_qty = 0
        self._backlog_at_po_placement = 0
        self._quantity_sold = 0
        self._position = 0
        self._shortage_units = 0

    @property
    def shortage_units(self):
        return self._shortage_cost

    @shortage_units.setter
    def shortage_units(self, shortage_units):
        self._shortage_cost = shortage_units

    @property
    def sku_id(self) -> str:
        return self._sku_id

    @sku_id.setter
    def sku_id(self, sku_id: str):
        self._sku_id = sku_id

    @property
    def lead_time(self) -> int:
        return self._lead_time

    @lead_time.setter
    def lead_time(self, lead_time):
        self._lead_time = lead_time

    @property
    def opening_stock(self)->int:
        return self._opening_stock

    @opening_stock.setter
    def opening_stock(self, opening_stock: int):
        self._opening_stock = opening_stock

    @property
    def demand(self) -> int:
        return self._demand

    @demand.setter
    def demand(self, demand: int):
        self._demand = demand

    @property
    def closing_stock(self) -> int:
        return self._closing_stock

    @closing_stock.setter
    def closing_stock(self, closing_stock: int):
        self._closing_stock = closing_stock

    @property
    def backlog(self) -> int:
        return self._backlog

    @backlog.setter
    def backlog(self, backlog: int):
        self._backlog = backlog

    @property
    def holding_cost(self) -> Decimal:
        return self._holding_cost

    @holding_cost.setter
    def holding_cost(self, holding_cost: Decimal):
        pass

    @property
    def shortage_cost(self) -> Decimal:
        return self._shortage_cost

    @shortage_cost.setter
    def shortage_cost(self, shortage_cost: Decimal):
        self._shortage_cost = shortage_cost

    @property
    def po_raised_flag(self) -> bool:
        return self._po_raised_flag

    @po_raised_flag.setter
    def po_raised_flag(self, po_raised_flag: bool):
        self._po_raised_flag = po_raised_flag

    @property
    def purchase_order_raised_qty(self) -> Decimal:
        return self._purchase_order_raised_qty

    @purchase_order_raised_qty.setter
    def purchase_order_raised_qty(self, po_raised_qty: Decimal):
        self._purchase_order_raised_qty = po_raised_qty

    @property
    def purchase_order_receipt_qty(self) -> int:
        return self._purchase_receipt_raised_qty

    @purchase_order_receipt_qty.setter
    def purchase_order_receipt_qty(self, po_receipt_qty: int):
        self._purchase_order_receipt_qty = po_receipt_qty

    @property
    def backlog_at_po_placement(self) -> int:
        return self._backlog_at_po_placement

    @backlog_at_po_placement.setter
    def backlog_at_po_placement(self, backlog: int):
        self._backlog_at_po_placement = backlog

    @property
    def quantity_sold(self) -> int:
        return self._quantity_sold

    @quantity_sold.setter
    def quantity_sold(self, quantity_sold: int):
        self._quantity_sold = quantity_sold

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position: int):
        self._position = position