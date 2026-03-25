# Transportation Optimization (Min-cost shipping)

## Problem
Minimize total transportation cost from warehouses to customers while satisfying supply and demand constraints.

## Tools used
- Python
- PuLP (CBC)
- pandas
- matplotlib

## Files
- `optimization.py` — builds & solves the LP; prints and saves results.
- `requirements.txt` — package list.
- `transportation_shipments.csv` — generated solved shipment table.
- `fig_shipped_by_warehouse.png` — generated bar chart of shipments by warehouse.
- `fig_route_heatmap.png` — generated heatmap of route quantities.

## How to run
1. (Optional) Create and activate a virtual environment:
   - macOS / Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows:
     ```powershell
     python -m venv .venv
     .venv\Scripts\activate
     ```

2. Install requirements:
```bash
pip install -r requirements.txt
