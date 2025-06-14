# Inventory-Simulation

# Nail Salon Inventory Simulation

This Python project simulates how a nail salon tracks and manages its daily inventory of essential products like nail polish and acrylic powder. It helps predict when items run out and when they need to be restocked.

> Designed to reflect real-world salon supply use, restocking decisions, and daily tracking.

---

## What It Does

- Simulates **30 days** of product usage in a nail salon  
- Tracks how much stock is used, when items are restocked, and when supplies run out  
- Saves **daily inventory logs** as CSV files  
- Creates a **visual chart** showing stock levels over time using Seaborn  

---

## Technologies Used

| Tool       | Purpose                                |
|------------|----------------------------------------|
| Python     | Core logic and simulation              |
| `pandas`   | Storing daily inventory logs in tables |
| `seaborn`  | Visualizing stock changes as a chart   |
| `matplotlib` | Backend for Seaborn’s plotting      |

---

## Example Products Simulated

- **Nail Polish**: High daily use, bulk restocked  
- **Acrylic Powder**: Moderate use, occasional restock  

You can easily customize these products in the code to simulate different salon supplies.

---

## How to Run It

### 1. Clone the repository:

```bash
git git@github.com:ninihuynh/Inventory-Simulation.git
cd nail-salon-inventory-simulation
```

### 2. Install Required Python Libraries:

```bash
pip3 install -r requirements.txt
```

### 3. Run the Simulation

```bash
python3 inventory_simulation.py
```
