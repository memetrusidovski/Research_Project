# ⚡️D-Optimal Solutions Using Quantum Algorithms⚡️

## Overview

This project aims to explore the use of quantum algorithms for solving D-Optimal experimental design problems. D-Optimal designs seek to maximize the determinant of a certain matrix, which measures the quality of the design in terms of its ability to discriminate between different model parameters. The problem is known to be NP-hard, meaning that its computational complexity grows exponentially with the size of the problem instance.

Quantum computers offer the potential to solve some problems faster than classical computers by exploiting the principles of quantum mechanics, such as superposition and entanglement. In particular, quantum algorithms for matrix operations, such as the quantum matrix inversion algorithm, promise exponential speedups for some applications, including D-Optimal designs.

## Requirements
To run the code in this project, you will need:

- A quantum computing platform or simulator, such as IBM Q or D-wave Leap.
- A classical computer with Python 3 and the following libraries:
- Qiskit for interfacing with quantum devices and simulators.
- Ocean SDK
- Numpy for numerical computations.
- Matplotlib for plotting results.
- NetworkX

## Results
The results of this project demonstrate the potential of quantum algorithms for solving D-Optimal designs. By using a quantum matrix inversion algorithm, we were able to achieve speedups of up to several orders of magnitude compared to classical algorithms. Moreover, the fidelity of the quantum circuit was high enough to produce designs with high quality metrics, as measured by the determinant of the design matrix.

## Conclusion
In conclusion, this project shows that quantum algorithms can provide a significant advantage for solving D-Optimal experimental design problems, which are known to have exponential complexity. By exploiting the power of quantum mechanics, we were able to achieve speedups that can enable the design of more efficient and effective experiments in a wide range of scientific and engineering domains.
