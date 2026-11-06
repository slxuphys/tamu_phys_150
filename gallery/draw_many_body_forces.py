"""Render pairwise gravitational forces and their sum for Lecture 15."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


def main():
    navy, red, green, gray = "#223247", "#cf343b", "#16804a", "#a0a8b4"
    plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "stix"})
    fig = plt.figure(figsize=(16, 9), facecolor="white")
    fig.text(0.05, 0.92, "Gravitational forces: adding the contributions",
             fontsize=28, weight="bold", color=navy)
    ax = fig.add_axes([0.035, 0.18, 0.48, 0.65])
    ax.set(xlim=(-0.5, 8.5), ylim=(-0.3, 6.7), aspect="equal")
    ax.axis("off")
    r1, r2, r3 = np.array([4., 5.]), np.array([1., 1.]), np.array([7., 1.])
    # Equal masses and equal separations give equal force magnitudes here.
    f12 = 0.4 * (r2 - r1)
    f13 = 0.4 * (r3 - r1)
    total = f12 + f13

    def arrow(start, end, color, width=3, size=17):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=size, linewidth=width,
                                    color=color, shrinkA=0, shrinkB=0, zorder=3))

    for r in (r2, r3):
        ax.plot([r1[0], r[0]], [r1[1], r[1]], "--", color=gray, linewidth=1.4)
    # Complete a parallelogram to show the vector sum geometrically.
    for f in (f12, f13):
        start, end = r1 + f, r1 + total
        ax.plot([start[0], end[0]], [start[1], end[1]],
                ":", color=green, linewidth=1.4)
    arrow(r1, r1 + f12, red)
    arrow(r1, r1 + f13, red)
    arrow(r1, r1 + total, green, width=3.5)
    for r, color in ((r1, navy), (r2, "#f4bf4d"), (r3, "#4389cf")):
        ax.add_patch(Circle(r, 0.25, facecolor=color, edgecolor=navy, linewidth=1.4, zorder=5))

    ax.text(4, 6.1, r"$m_1$", fontsize=28, ha="center", color=navy)
    ax.text(4, 5.55, r"$\vec r_1=(x_1,y_1)$", fontsize=22, ha="center", color=navy)
    for x, i in ((1, 2), (7, 3)):
        ax.text(x, 0.43, rf"$m_{i}$", fontsize=27, ha="center", color=navy)
        ax.text(x, -0.08, rf"$\vec r_{i}=(x_{i},y_{i})$", fontsize=21, ha="center", color=navy)
    ax.text(2.35, 4.2, r"$\vec F_{12}$", fontsize=29, ha="center", color=red)
    ax.text(5.65, 4.2, r"$\vec F_{13}$", fontsize=29, ha="center", color=red)
    ax.text(4.25, 2.35, r"$\vec F_1$", fontsize=29, color=green)

    x = 0.56
    fig.text(x, 0.73, r"$\vec F_{12}=-\frac{Gm_1m_2}{(\Delta r_{12})^3}(\vec r_1-\vec r_2)$", fontsize=28, color=red)
    fig.text(x, 0.65, "Force on body 1 from body 2.", fontsize=18, color=navy)
    fig.text(x, 0.51, r"$\vec F_{13}=-\frac{Gm_1m_3}{(\Delta r_{13})^3}(\vec r_1-\vec r_3)$", fontsize=28, color=red)
    fig.text(x, 0.43, "Force on body 1 from body 3.", fontsize=18, color=navy)
    fig.text(x, 0.29, r"$\vec F_1=\vec F_{12}+\vec F_{13}$", fontsize=30, color=green)
    fig.text(x, 0.20, r"$\Delta r_{1j}=|\vec r_1-\vec r_j|$", fontsize=25, color=navy)
    fig.text(0.05, 0.09, "All force arrows shown act on body 1; each pairwise force points toward the attracting body.",
             fontsize=18, color=navy)
    fig.text(0.05, 0.045, "Illustration: equal masses and equal separations. The net force is the vector sum.",
             fontsize=15, color="#647184")
    path = Path(__file__).with_name("many-body-gravitational-forces")
    for suffix in (".png", ".svg", ".pdf"):
        fig.savefig(path.with_suffix(suffix), dpi=180, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
