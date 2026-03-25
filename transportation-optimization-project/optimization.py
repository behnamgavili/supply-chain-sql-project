import pulp

# Create problem
model = pulp.LpProblem("Transportation_Problem", pulp.LpMinimize)

# Data
warehouses = ["Milan", "Rome", "Paris", "Berlin"]
customers = ["North", "South", "East", "West"]

supply = {
    "Milan": 500,
    "Rome": 400,
    "Paris": 450,
    "Berlin": 420
}

demand = {
    "North": 300,
    "South": 350,
    "East": 400,
    "West": 320
}


cost = {
    ("Milan", "North"): 4,
    ("Milan", "South"): 7,
    ("Milan", "East"): 6,
    ("Milan", "West"): 5,

    ("Rome", "North"): 6,
    ("Rome", "South"): 4,
    ("Rome", "East"): 5,
    ("Rome", "West"): 7,

    ("Paris", "North"): 5,
    ("Paris", "South"): 6,
    ("Paris", "East"): 7,
    ("Paris", "West"): 4,

    ("Berlin", "North"): 3,
    ("Berlin", "South"): 6,
    ("Berlin", "East"): 4,
    ("Berlin", "West"): 5,
}
# Decision variables
x = pulp.LpVariable.dicts("ship", (warehouses, customers), lowBound=0)

# Objective
model += pulp.lpSum(cost[i, j] * x[i][j] for i in warehouses for j in customers)

# Supply constraints
for i in warehouses:
    model += pulp.lpSum(x[i][j] for j in customers) <= supply[i]

# Demand constraints
for j in customers:
    model += pulp.lpSum(x[i][j] for i in warehouses) == demand[j]

# Solve
model.solve()

print("\nOptimal Shipping Plan:\n")

for i in warehouses:
    for j in customers:
        if x[i][j].value() > 0:
            print(f"{i} → {j}: {x[i][j].value()} units")

print("\nTotal Transportation Cost:", pulp.value(model.objective))


print("\nInsight:")
print("The model allocates shipments to minimize total cost while satisfying demand.")
print("Warehouses with lower transportation cost serve more customers.")

import pandas as pd

# build results list (after solve)
results = []
for i in warehouses:
    for j in customers:
        qty = x[i][j].value()
        if qty is not None and qty > 0:
            results.append({
                "from": i,
                "to": j,
                "quantity": float(qty),
                "unit_cost": cost[(i, j)],
                "route_cost": float(qty) * cost[(i, j)]
            })

df_results = pd.DataFrame(results)
print("\nShipment table:\n", df_results)

# summary: shipments per warehouse
print("\nTotal shipped per warehouse:")
print(df_results.groupby("from")[["quantity","route_cost"]].sum())

# summary: shipments per customer
print("\nTotal received per customer:")
print(df_results.groupby("to")[["quantity","route_cost"]].sum())

# save results
df_results.to_csv("transportation_shipments.csv", index=False)
print("\nSaved: transportation_shipments.csv")



import matplotlib.pyplot as plt
import numpy as np

# A: shipments per warehouse
agg_wh = df_results.groupby("from")["quantity"].sum().reindex(warehouses).fillna(0)
plt.figure()
agg_wh.plot(kind="bar")
plt.ylabel("Units shipped")
plt.title("Total Shipped by Warehouse")
plt.tight_layout()
plt.savefig("fig_shipped_by_warehouse.png")
plt.show()

# B: route heatmap (warehouses x customers)
pivot = df_results.pivot_table(index="from", columns="to", values="quantity", aggfunc="sum").reindex(index=warehouses, columns=customers).fillna(0)
plt.figure(figsize=(6,4))
plt.imshow(pivot, cmap="Blues", aspect="auto")
plt.colorbar(label="Quantity")
plt.xticks(range(len(customers)), customers)
plt.yticks(range(len(warehouses)), warehouses)
plt.title("Shipment Quantities (warehouse → customer)")
for (i, j), val in np.ndenumerate(pivot.values):
    if val>0:
        plt.text(j, i, int(val), ha="center", va="center", color="k")
plt.tight_layout()
plt.savefig("fig_route_heatmap.png")
plt.show()

total_cost = pulp.value(model.objective)
total_shipped = df_results["quantity"].sum()
top_routes = df_results.sort_values("route_cost", ascending=False).head(5)

print(f"\nTotal cost = {total_cost}")
print(f"Total units shipped = {total_shipped}")
print("\nTop 5 route cost contributors:")
print(top_routes[["from","to","quantity","route_cost"]])