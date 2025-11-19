# MCNPX-PoliMi Simulation and Analysis Workflow

This guide outlines the steps to set up your environment, run an MCNPX-PoliMi simulation, post-process the data using `pyMPPost`, and visualize the results using a custom Python script.

## 1. Installing Python

Before starting, ensure you have Python installed on your system.

* **Windows, macOS, & Linux:** [Official Python Downloads](https://www.python.org/downloads/)
* **Anaconda Distribution (All OS):** [Anaconda Installers](https://www.anaconda.com/products/distribution) (Recommended for scientific computing)
* **macOS (Homebrew):** `brew install python`
* **Linux (apt):** `sudo apt-get install python3`

## 2. Installing pyMPPost

Install the [`pyMPPost`](https://gitlab.eecs.umich.edu/umich-dnng/pymppost) package directly from PyPI using pip:

```bash
pip install pyMPPost
```

## 3. Installing Required Post-Processing Packages

Install the necessary libraries for data handling and plotting. Specifically, the plotting script requires `matplotlib` and `pandas`.

```bash
pip install matplotlib pandas
```

## 4. Running Example MCNPX-PoliMi File

**Prerequisites:**
* **MCNPX-PoliMi:** This must be installed on your machine.
* **MCNP6.3 (or compatible):** Required for nuclear data libraries.

> **Note:** You can obtain these codes via the **[RSICC website](https://rsicc.ornl.gov/)**.

**Execution:**
Run the simulation in your terminal. The basic syntax follows standard MCNP conventions.

```bash
polimi i=EJ309.i n=EJ309. d=EJ309.d
```

* `i`: Input file
* `n`: Tally output file (standard MCNP output)
* `d`: Collision data dump file (PoliMi specific output)

*Note: Your specific executable might have a longer default name (e.g., `mcnpx_polimi_v2`). It is common practice to alias or rename it to `polimi` for ease of use.*

## 5. Process Output Data

Once the simulation is complete, use `pyMPPost` to parse the collision dump file (`.d` file) according to your configuration.

```bash
pyMPPost input_config.toml
```

*Ensure your `input_config.toml` is properly formatted to read the `EJ309.d` file generated in the previous step.*

## 6. Plot Outputs

Finally, visualize the energy deposition and light output using the Python script.

```bash
python energy_light_histograms.py
```

This will generate a figure with two side-by-side plots:
1.  **Left:** Energy deposition (Total vs. Individual ZAIDs).
2.  **Right:** Light output histograms.
