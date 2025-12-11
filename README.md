
# Sine Cosine Algorithm (SCA) - Implementation

This repository contains a Python implementation of the Sine Cosine Algorithm (SCA) for global optimization,
a demo showing its behavior on the Sphere function, and plotting utilities.

## Files
- `sca.py` : Implementation of the SCA algorithm (class `SCA`) and example `sphere` function.
- `demo.py`: Demo script that runs SCA on the Sphere benchmark and saves a convergence plot to `outputs/`.
- `requirements.txt`: Minimal required packages.
- `README.md`: This file.

## Usage
1. Create a Python environment and install requirements:
```
pip install -r requirements.txt
```

2. Run the demo:
```
python demo.py
```

3. Outputs will be saved in the `outputs/` folder (e.g., `sca_convergence.png`).

## How to use in your project / GitHub
- Copy `sca.py` into your repository.
- Add benchmark functions or adapt the `SCA` class to your needs.
- Cite: Mirjalili, S. (2016). SCA: Sine Cosine Algorithm.

## License
MIT - For educational use.
