# QKD-Experimental-Data-Analysis
This Python program analyzes and visualizes experimental data from two QKD devices: The Quantum Entanglement Demonstrator and the IDQ QKD Cerberus. It calculates visibility from polarization correlations and compares Quantum Bit Error Rates (QBER) with and without eavesdropping, showing how the attacks affect the channel integrity.

The goal is to gain a deeper understanding of how quantum mechanics can be utilized to create unbreakable encryption keys and how potential attacks impact communication quality.

The script processes and visualizes two main datasets:

quED Data: Measures photon polarization correlations at different analyzer angle differences. The program normalizes coincidence counts to calculate visibility, which indicates how well the quantum states are correlated.

Cerberus Data: Evaluates Quantum Bit Error Rates (QBER) both with and without an eavesdropper, showing how interception attempts can degrade the signal and compromise security.

Finally, it generates clear, easy-to-read plots that show the polarization correlation curve and how QBER changes under attack conditions. This helps visualize the fragile yet powerful nature of quantum encryption and the importance of maintaining high visibility and low QBER in secure quantum communication systems.
