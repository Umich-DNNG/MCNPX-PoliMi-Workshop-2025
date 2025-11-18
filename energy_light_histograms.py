import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_energy_and_light():
    # --- Load File 1: EJ309.d ---
    # 'header=None' because the snippet has no header
    # 'delim_whitespace=True' handles spaces or tabs
    try:
        df_energy = pd.read_csv('EJ309.d', delim_whitespace=True, header=None)
        # Column 7 corresponds to index 6 (0-based index)
        energy_data = df_energy.iloc[:, 6]
        # Column 5 corresponds to index 4 (0-based index) - ZAID
        zaid_data = df_energy.iloc[:, 4]
    except Exception as e:
        print(f"Error reading EJ309.d: {e}")
        return

    # --- Load File 2: EJ309_mpp_All_Pulses ---
    # This file has a header, so pandas will automatically use it
    try:
        df_light = pd.read_csv('EJ309_mpp_All_Pulses', delim_whitespace=True)
        # Column 7 corresponds to index 6.
        # We can select by index 6, or by name 'light' if we are sure of the header.
        # Using index 6 to be safe as per instructions.
        light_data = df_light.iloc[:, 6]
    except Exception as e:
        print(f"Error reading EJ309_mpp_All_Pulses: {e}")
        return

    # --- Plotting ---
    # Create a figure with 1 row and 2 columns
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # 1. Left Plot: Energy Deposition
    # Define common bins for all energy histograms to ensure alignment
    energy_bins = np.linspace(energy_data.min(), energy_data.max(), 100)

    # Plot Total
    ax1.hist(energy_data, bins=energy_bins, color='skyblue', edgecolor='black', alpha=0.7, label='Total')

    # Plot Individual ZAIDs
    unique_zaids = zaid_data.unique()

    # Use a colormap (tab10) to ensure distinct colors for each ZAID
    cmap = plt.get_cmap('tab10')

    for i, zaid in enumerate(unique_zaids):
        subset = energy_data[zaid_data == zaid]
        # Select color from colormap
        # We start from index 1 (orange) to avoid the first blue color clashing with 'skyblue'
        color = cmap((i + 1) % 10)
        ax1.hist(subset, bins=energy_bins, histtype='step', linewidth=2.5, color=color, label=f'ZAID {zaid}')

    ax1.set_title('Energy Deposition')
    ax1.set_xlabel('Energy Deposited (MeV)')
    ax1.set_ylabel('Counts')
    ax1.set_yscale('log')
    ax1.legend()

    # Add Total Counts text to top right of the plot area
    count_text_1 = f"Total Counts: {len(energy_data)}"
    ax1.text(0.95, 0.95, count_text_1,
             transform=ax1.transAxes,
             horizontalalignment='right',
             verticalalignment='top',
             bbox=dict(boxstyle="round", facecolor='white', alpha=0.5))

    # 2. Right Plot: Light Output
    ax2.hist(light_data, bins=100, color='orange', edgecolor='black', alpha=0.7)
    ax2.set_title('Light Output')
    ax2.set_xlabel('Light Output (MeVee)')
    ax2.set_ylabel('Counts')
    ax2.set_yscale('log')

    # Add Total Counts text to top right of the plot area
    count_text_2 = f"Total Counts: {len(light_data)}"
    ax2.text(0.95, 0.95, count_text_2,
             transform=ax2.transAxes,
             horizontalalignment='right',
             verticalalignment='top',
             bbox=dict(boxstyle="round", facecolor='white', alpha=0.5))

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    plot_energy_and_light()
