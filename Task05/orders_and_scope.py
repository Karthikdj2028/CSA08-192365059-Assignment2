"""Q5: Demonstrate mutable default arguments, parameters and scope."""


def add_item_buggy(item, order=[]):
    """Incorrect: the same list is reused across calls."""
    order.append(item)
    return order


def add_item(item, order=None):
    """Correct: create a new list when the caller does not supply one."""
    if order is None:
        order = []
    order.append(item)
    return order


def calculate_total(price, quantity=1, gst_rate=0.05):
    """Return the bill total and GST as two values (a tuple)."""
    subtotal = price * quantity
    gst = subtotal * gst_rate
    total = subtotal + gst
    return total, gst


print("BUGGY MUTABLE DEFAULT")
print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print("Stored default after calls:", add_item_buggy.__defaults__)

print("\nCORRECT INDEPENDENT CUSTOMER ORDERS")
customer1 = []
customer1 = add_item("Tea", customer1)
customer1 = add_item("Vada", customer1)

customer2 = []
customer2 = add_item("Coffee", customer2)
customer2 = add_item("Samosa", customer2)

customer3 = []
customer3 = add_item("Juice", customer3)

print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)

print("\nPOSITIONAL / KEYWORD / DEFAULT PARAMETERS")
print("Positional:", calculate_total(100, 2))
print("Keyword:", calculate_total(price=100, quantity=2, gst_rate=0.05))
print("Default quantity:", calculate_total(100))

total, gst = calculate_total(100, 2)
print(f"Returned separately: total = Rs {total:.2f}, GST = Rs {gst:.2f}")

# Local and global scope example.
shop_name = "Ksheera Canteen"

def show_local_and_global():
    local_message = "This is local"
    print(local_message)
    print("Global value read inside function:", shop_name)

show_local_and_global()

# nonlocal changes a name in the enclosing function.
def make_counter():
    count = 0
    def increase():
        nonlocal count
        count += 1
        return count
    return increase

counter = make_counter()
print("Nonlocal counter:", counter(), counter())

# A global statement allows reassignment, but returning a value is often clearer.
def change_shop_name():
    global shop_name
    shop_name = "Updated Canteen"

change_shop_name()
print("Global reassigned:", shop_name)
