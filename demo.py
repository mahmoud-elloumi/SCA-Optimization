
"""demo.py
Demonstration script that runs SCA on standard benchmarks and saves a convergence plot.
Usage: python demo.py
"""
from sca import SCA, sphere
import numpy as np
import matplotlib.pyplot as plt
import os

def run_demo():
    dim = 30
    bounds = (-5.12 * np.ones(dim), 5.12 * np.ones(dim))
    sca = SCA(sphere, dim, bounds, pop_size=40, max_iter=200, seed=1)
    res = sca.run(verbose=True)
    converg = res['convergence']

    # save plot
    os.makedirs('outputs', exist_ok=True)
    plt.figure(figsize=(6,4))
    plt.plot(converg, linewidth=2)
    plt.yscale('log')
    plt.xlabel('Iteration')
    plt.ylabel('Best fitness (log scale)')
    plt.title('SCA Convergence on Sphere')
    plt.grid(True)
    plt.tight_layout()
    out_path = os.path.join('outputs','sca_convergence.png')
    plt.savefig(out_path, dpi=150)
    print('Saved plot to', out_path)

if __name__ == '__main__':
    run_demo()
