"""Draw the initial conditions of Lecture 15's second three-body simulation."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def main():
    navy, green, gray = "#223247", "#16804a", "#919baa"
    plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "stix"})
    fig = plt.figure(figsize=(16, 9), facecolor="white")
    fig.text(0.045, 0.93, "Three stars: second set of initial conditions",
             fontsize=28, weight="bold", color=navy)
    ax = fig.add_axes([0.04, 0.20, 0.47, 0.63])
    ax.set(xlim=(-1.5, 1.65), ylim=(-1.05, 1.15), aspect="equal")
    ax.axis("off")

    def arrow(start, end, color, width=1.5, size=12):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=size, linewidth=width,
                                    color=color, shrinkA=0, shrinkB=0))

    arrow((-1.4, 0), (1.5, 0), gray)
    arrow((0, -0.95), (0, 1.0), gray)
    ax.text(1.54, -0.04, "$x$", fontsize=24, color=navy)
    ax.text(0.05, 0.99, "$y$", fontsize=24, color=navy)

    positions = np.array([[0., 0.], [0.97000436, -0.24308753],
                          [-0.97000436, 0.24308753]])
    velocities = np.array([[-0.93240737, -0.86473146],
                           [0.93240737 / 2, 0.86473146 / 2],
                           [0.93240737 / 2, 0.86473146 / 2]])
    colors = ["tab:blue", "tab:orange", "tab:green"]
    for i, (r, v, color) in enumerate(zip(positions, velocities, colors), 1):
        if i != 1:
            ax.plot([r[0], r[0]], [0, r[1]], ":", color=gray, linewidth=1.2)
        arrow(r, r + 0.8 * v, green, width=3, size=17)
        ax.plot(*r, "o", color=color, markersize=22, zorder=5)

    ax.text(0.15, 0.19, "Star 1", fontsize=20, color=colors[0])
    ax.text(0.15, 0.055, r"$O\ (0,0)$", fontsize=18, color=navy)
    ax.text(0.98, -0.48, "Star 2", ha="center", fontsize=20, color=colors[1])
    ax.text(-1.02, 0.08, "Star 3", ha="right", fontsize=20, color=colors[2])
    ax.text(-0.60, -0.23, r"$\vec v_1$", fontsize=28, color=green)
    ax.text(1.38, 0.16, r"$\vec v_2$", fontsize=28, color=green)
    ax.text(-1.02, 0.65, r"$\vec v_3$", fontsize=28, color=green)

    labels = [
        ("Star 1: at the origin", r"$\vec r_1=(0,\,0)$",
         r"$\vec v_1=(-0.93240737,\,-0.86473146)$"),
        ("Star 2", r"$\vec r_2=(0.97000436,\,-0.24308753)$",
         r"$\vec v_2=(0.466203685,\,0.432365730)$"),
        ("Star 3", r"$\vec r_3=(-0.97000436,\,0.24308753)$",
         r"$\vec v_3=(0.466203685,\,0.432365730)$"),
    ]
    for y, color, (title, r, v) in zip((0.78, 0.55, 0.32), colors, labels):
        fig.text(0.55, y, title, fontsize=21, color=color)
        fig.text(0.55, y - 0.065, r, fontsize=23, color=navy)
        fig.text(0.55, y - 0.13, v, fontsize=23, color=green)
    fig.text(0.045, 0.10, r"$Gm_1=Gm_2=Gm_3=1$    |    $\vec v_2=\vec v_3=-\frac{1}{2}\vec v_1$",
             fontsize=22, color=navy)
    fig.text(0.045, 0.045, "Green arrows show initial velocities on a common scale; they do not show forces.",
             fontsize=17, color=navy)
    assert np.allclose(positions.sum(axis=0), 0)
    assert np.allclose(velocities.sum(axis=0), 0)
    path = Path(__file__).with_name("three-star-second-initial-conditions")
    for suffix in (".png", ".svg", ".pdf"):
        fig.savefig(path.with_suffix(suffix), dpi=180, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
