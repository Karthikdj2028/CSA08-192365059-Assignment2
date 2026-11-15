# Q5 – Functions, Parameters and Scope

## Why the default-list bug occurs

A default argument is evaluated once when the function is defined. In `add_item_buggy(item, order=[])`, both calls use the same list object. The second call appends to the list created for the first call, so items from a previous customer remain in the next order. `add_item_buggy.__defaults__` displays the tuple containing that shared list.

The corrected function uses `order=None`. Each call with no list creates a fresh list. If the caller is adding multiple items to one order, it passes the order list explicitly on later calls.

## Parameters and return values

- Positional parameters: values are matched by order, e.g. `calculate_total(100, 2)`.
- Keyword parameters: names make the call clear, e.g. `calculate_total(price=100, quantity=2)`.
- Default parameters: make common values optional, e.g. quantity defaults to 1.
- More than one value can be returned as a tuple, e.g. `return total, gst`.

The sample GST rate is 5% only to demonstrate returning two values; it is an example assumption, not a rate specified in the assignment.

## Scope

A local name is created inside a function and is available there. A global name is created at module level; a function can read it without a declaration. To reassign a global name inside a function, use `global`, although passing values as parameters and returning results is usually easier to test. `nonlocal` lets an inner function reassign a name from its enclosing function. The counter example demonstrates this.

## Alternative designs

The caller can always create an empty list and pass it explicitly. This is simple and makes ownership clear. A closure can also create a private order list and return an inner `add` function; this hides the list but introduces a slightly more advanced concept. Appending one item is amortised O(1) time; storing m items for one customer uses O(m) space. Each customer's list is independent.


Example closure alternative:

```python
def make_order():
    order = []
    def add(item):
        order.append(item)
        return order
    return add

customer_one_add = make_order()
customer_two_add = make_order()
customer_one_add("Tea")
customer_two_add("Coffee")
```

Each call to `make_order()` creates a new enclosed list, so the two customers remain separate.
