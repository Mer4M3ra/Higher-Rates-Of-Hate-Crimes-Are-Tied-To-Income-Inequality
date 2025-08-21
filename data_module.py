# data_module.py
import pandas as pd
import matplotlib.pyplot as plt
plt.ion
# Keep a global DataFrame so all functions can access and modify it
df = pd.read_csv("hate_crimes.csv")

def display_dataset_preview():
    """Shows the first few rows of the dataset."""
    print("\n=== Dataset Preview ===")
    print(df.head())
    print(f"\nRows: {df.shape[0]}, Columns: {df.shape[1]}")

def display_visualisation():
    plt.figure(figsize=(10, 6))
    plt.scatter(df["median_household_income"], df["hate_crimes_per_100k_splc"], alpha=0.7)
    plt.title("Median Household Income vs Hate Crimes per 100k")
    plt.xlabel("Median Household Income")
    plt.ylabel("Hate Crimes per 100k (SPLC)")
    plt.grid(True)
    plt.show(block=True)  # block=True ensures the program waits until you close the plot

def search_data():
    """Search dataset by state name."""
    term = input("Enter state name to search: ").strip().lower()
    results = df[df["state"].str.lower().str.contains(term)]
    if not results.empty:
        print(results)
    else:
        print("No matching entries found.")

def update_data_entry():
    """Update a row for a specific state."""
    state_name = input("Enter state name to update: ").strip()
    if state_name in df["state"].values:
        col_name = input(f"Enter column to update ({', '.join(df.columns)}): ").strip()
        if col_name in df.columns:
            new_value = input("Enter new value: ").strip()
            try:
                # Convert numeric columns to the correct type
                if pd.api.types.is_numeric_dtype(df[col_name]):
                    new_value = float(new_value)
            except ValueError:
                print("Invalid number. Value will be saved as text.")
            df.loc[df["state"] == state_name, col_name] = new_value
            print(f"{col_name} for {state_name} updated.")
        else:
            print("Invalid column name.")
    else:
        print("State not found.")

def save_changes():
    """Save the DataFrame back to CSV."""
    df.to_csv("hate_crimes.csv", index=False)
