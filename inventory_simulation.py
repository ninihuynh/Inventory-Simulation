# This program simulates a nail salon's inventory.
# It tracks how many supplies are used every day and when to restock them.

import random                      # helps us simulate random daily usage
import os                          # helps us work with folders and files
import pandas as pd                # lets us store and work with table data
import seaborn as sns              # makes nice charts
import matplotlib.pyplot as plt    # works with seaborn to display charts


# This class describes one product (like nail polish or acrylic powder)
class Product:
    def __init__(self, name, stock, reorder_threshold, reorder_amount):
        self.name = name  # Name of the product
        self.stock = stock  # How much we start with
        self.reorder_threshold = reorder_threshold  # When to order more
        self.reorder_amount = reorder_amount  # How much to reorder
        self.total_restocked = 0  # How many we added over time
        self.total_used = 0  # How many were used in total
        self.total_unavailable = 0  # When we didn’t have enough
        self.history = []  # We’ll save a daily log here

    # This simulates one day of using this product
    def simulate_day(self, day: int):
        usage = random.randint(1, 15)  # Random usage for the day
        start_stock = self.stock  # Remember how much we started with

        # If we don’t have enough, we use what we can and track what's missing
        if usage > self.stock:
            self.total_unavailable += usage - self.stock
            self.total_used += self.stock  # Use whatever is left
            self.stock = 0  # Stock is now empty
        else:
            self.stock -= usage  # Use the product
            self.total_used += usage

        # If we're low on stock, reorder
        restocked = 0
        if self.stock <= self.reorder_threshold:
            self.stock += self.reorder_amount
            restocked = self.reorder_amount
            self.total_restocked += restocked

        # Save what happened today
        self.history.append({
            "Day": day,
            "Product": self.name,
            "Start Stock": start_stock,
            "Used Today": usage,
            "Restocked": restocked,
            "End Stock": self.stock,
            "Unavailable": max(0, usage - start_stock)
        })

    # Save the history of this product to a CSV file (like a spreadsheet)
    def save_to_csv(self, folder="sample_output"):
        os.makedirs(folder, exist_ok=True)  # Make sure folder exists
        df = pd.DataFrame(self.history)  # Turn our log into a table
        filename = f"{folder}/{self.name.replace(' ', '_').lower()}_inventory_log.csv"
        df.to_csv(filename, index=False)  # Save it
        print(f"[✔] Saved CSV: {filename}")

    # This just returns the history in table form
    def get_dataframe(self):
        return pd.DataFrame(self.history)

    # At the end, we use this to show a summary of this product
    def get_summary(self):
        return {
            "Product": self.name,
            "Final Stock": self.stock,
            "Total Used": self.total_used,
            "Total Restocked": self.total_restocked,
            "Times Unavailable": self.total_unavailable
        }


# This function runs the entire simulation for all products
def run_simulation(days: int = 30):
    # List of products used in a nail salon
    inventory = [
        Product("Nail Polish", stock=60, reorder_threshold=20, reorder_amount=50),
        Product("Acrylic Powder", stock=40, reorder_threshold=15, reorder_amount=30)
    ]

    print("\n[💅] Starting Nail Salon Inventory Simulation...\n")

    # Simulate each day
    for day in range(1, days + 1):
        print(f"Day {day}")
        for product in inventory:
            product.simulate_day(day)  # Simulate today’s usage
            print(f" - {product.name}: {product.stock} left in stock")
        print()

    # Save daily logs and combine them for charting
    all_data = []
    for product in inventory:
        product.save_to_csv()
        all_data.append(product.get_dataframe())

    # Combine all product logs into one big table
    combined_df = pd.concat(all_data)

    # Plot the results
    sns.set(style="whitegrid")  # Make chart background white and clean
    plt.figure(figsize=(10, 5))  # Set chart size

    # Line chart showing inventory for each product
    sns.lineplot(
        data=combined_df,
        x="Day",
        y="End Stock",
        hue="Product",
        marker="o"
    )

    plt.title("Nail Salon Inventory Over Time")
    plt.xlabel("Day")
    plt.ylabel("Stock Remaining")
    plt.legend(title="Product")
    plt.tight_layout()

    # Save chart image
    os.makedirs("sample_output", exist_ok=True)
    plot_path = "sample_output/nail_salon_inventory_plot.png"
    plt.savefig(plot_path)
    print(f"[📊] Plot saved: {plot_path}")
    plt.show()

    # Show summary results
    print("\n--- Final Inventory Summary ---")
    for product in inventory:
        summary = product.get_summary()
        print(f"{summary['Product']}:")
        print(f"  Final Stock       : {summary['Final Stock']}")
        print(f"  Total Used        : {summary['Total Used']}")
        print(f"  Total Restocked   : {summary['Total Restocked']}")
        print(f"  Times Unavailable : {summary['Times Unavailable']}\n")


# This runs the simulation when the file is run directly
if __name__ == "__main__":
    run_simulation()
