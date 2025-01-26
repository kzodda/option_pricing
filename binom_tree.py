"""
Binom Pricing algo.
Karl Zodda
1/2/25
"""
## Part 1: Set initial parameters
initial_price = 4
u = 2
d = 0.5
periods = 8
r = .25
K = 5

# ---------------------------------------------------------
## DO NOT MODIFY BELOW THIS LINE!!!
# ---------------------------------------------------------
# Initializing other variables and data structures
tree = {0: [initial_price]}
p_hat = (1 + r - d)/(u - d)
q_hat = (u - 1 - r)/(u - d)
value_tree = {}


## Part 2: Building the binomial tree
for period in range(1, periods + 1):
    temp = []
    for value in tree[period - 1]:
        temp.append(value * u)
        temp.append(value * d)
        tree[period] = temp


## Part 3: Calculating the no-arb price of a European option
key_len = len(tree.keys())
x4 = tree[key_len - 1]
v4 = []
for i in range(len(x4)):
    v4.append(max(0, x4[i] - K))


def price_binom(x: list, phat: float, qhat: float, rate: float) -> None:
    """
    Recursive function to price a European option using a binomial tree.
    """
    if len(x) > 2:
        y = []
        # Pair the prices by index 0 and 1, 2 and 3, etc.
        for t in range(0, len(x), 2):
            # Calculating the Price of each node working backwards
            y.append(((1 / (1 + rate)) * (phat * x[t] + qhat * x[t + 1])))
            # print(y)
        price_binom(y, phat, qhat, rate)
    else:
        # Final Price
        price = (1 / (1 + rate)) * ((phat * x[0]) + (qhat * x[1]))
        # Printing the Final Price
        print(f"The price is: ${price:.2f}")
        return None


## Calls the recursive function to work backwards through the tree and price the European option
price_binom(v4, p_hat, q_hat, r)
