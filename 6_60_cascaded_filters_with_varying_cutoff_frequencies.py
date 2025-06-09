import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Set Plotly to open in your default web browser
pio.renderers.default = "browser"

# Define band-pass filter application scenarios
applications = [
    {"Application": "Voice communication", "fc_low": 300, "fc_high": 3400},
    {"Application": "Subwoofer crossover", "fc_low": 20, "fc_high": 200},
    {"Application": "Fast sensor (e.g., vibration)", "fc_low": 10, "fc_high": 1000},
    {"Application": "AM radio", "fc_low": 530e3, "fc_high": 1.7e6}
]

# Fixed resistor value (standard E12 value)
R_fixed = 10_000  # 10 kΩ

# Compute capacitor values for each application
table_data = []
for app in applications:
    C_high = 1 / (2 * np.pi * R_fixed * app["fc_low"])
    C_low = 1 / (2 * np.pi * R_fixed * app["fc_high"])
    table_data.append({
        "Application": app["Application"],
        "fc_low (Hz)": app["fc_low"],
        "fc_high (Hz)": app["fc_high"],
        "Resistor (Ohms)": R_fixed,
        "C_high (uF)": C_high * 1e6,
        "C_low (uF)": C_low * 1e6
    })

# Display capacitor value table in the terminal
df = pd.DataFrame(table_data)
print("\nCapacitor values for each band-pass application (assuming 10 kΩ resistor):\n")
print(df.to_string(index=False))

# Define frequency sweep for plotting (1 Hz to 10 MHz)
f = np.logspace(0, 7, 1000)

# Transfer function for cascaded RC stage
def cascaded_RC_response(fc, f, filter_type='low', stages=2):
    if filter_type == 'low':
        H_single = 1 / (1 + 1j * (f / fc))
    elif filter_type == 'high':
        H_single = (1j * (f / fc)) / (1 + 1j * (f / fc))
    else:
        raise ValueError("filter_type must be 'low' or 'high'")
    return H_single ** stages

# Plotting loop
for app in applications:
    fc_low = app["fc_low"]
    fc_high = app["fc_high"]

    # Calculate full band-pass transfer function
    H_hp = cascaded_RC_response(fc_low, f, 'high', 2)
    H_lp = cascaded_RC_response(fc_high, f, 'low', 2)
    H_bp = H_hp * H_lp
    magnitude = 20 * np.log10(np.abs(H_bp))

    # Get gain at cutoff frequencies
    H_fc_low = cascaded_RC_response(fc_low, np.array([fc_low]), 'high', 2) * \
               cascaded_RC_response(fc_high, np.array([fc_low]), 'low', 2)
    H_fc_high = cascaded_RC_response(fc_low, np.array([fc_high]), 'high', 2) * \
                cascaded_RC_response(fc_high, np.array([fc_high]), 'low', 2)
    mag_fc_low = 20 * np.log10(np.abs(H_fc_low))[0]
    mag_fc_high = 20 * np.log10(np.abs(H_fc_high))[0]

    # Create interactive plot
    fig = go.Figure()

    # Main response curve
    fig.add_trace(go.Scatter(
        x=f,
        y=magnitude,
        mode='lines',
        name='Magnitude',
        line=dict(color='blue')
    ))

    # Marker at fc_low
    fig.add_trace(go.Scatter(
        x=[fc_low],
        y=[mag_fc_low],
        mode='markers+text',
        marker=dict(size=10, color='red', symbol='circle'),
        text=[f"fc_low\n{fc_low:.1f} Hz"],
        textposition="bottom right"
    ))

    # Marker at fc_high
    fig.add_trace(go.Scatter(
        x=[fc_high],
        y=[mag_fc_high],
        mode='markers+text',
        marker=dict(size=10, color='green', symbol='circle'),
        text=[f"fc_high\n{fc_high:.1f} Hz"],
        textposition="top left"
    ))

    # Plot layout
    fig.update_layout(
        title=f"Band-pass Filter Response: {app['Application']}",
        xaxis_title="Frequency (Hz)",
        yaxis_title="Magnitude (dB)",
        xaxis_type="log",
        yaxis=dict(range=[-60, 5]),
        width=800,
        height=500,
        showlegend=False
    )

    # Show plot in browser
    fig.show()
