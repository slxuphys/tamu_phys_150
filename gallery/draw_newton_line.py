"""Draw the straight-line derivation of Newton's method for Lecture 16.

Equations use Matplotlib's LaTeX-style mathtext, without an external TeX install.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    navy, blue, gray = "#223247", "#2878b5", "#969da7"
    plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "stix"})
    fig = plt.figure(figsize=(12, 6), facecolor="white")
    fig.text(0.05, 0.92, "Newton’s method: the root of a straight line",
             fontsize=23, weight="bold", color=navy)

    ax = fig.add_axes([0.055, 0.14, 0.46, 0.69])
    ax.set(xlim=(-0.6, 6.7), ylim=(-0.6, 5.1))
    ax.axis("off")
    arrow = dict(arrowstyle="-|>", color=navy, lw=1.4, mutation_scale=12)
    ax.annotate("", xy=(6.5, 0), xytext=(-0.25, 0), arrowprops=arrow)
    ax.annotate("", xy=(0, 4.95), xytext=(0, -0.3), arrowprops=arrow)
    ax.text(6.5, -0.3, "$x$", fontsize=22, color=navy)
    ax.text(-0.35, 4.85, "$y$", fontsize=22, color=navy)

    x0, y0, k = 4.3, 3.1, 1.2
    x1 = x0 - y0 / k
    x = np.linspace(x1 - 0.3, 5.8, 200)
    ax.plot(x, k * (x - x0) + y0, color=blue, lw=2.2)
    ax.plot([0, x0, x0], [y0, y0, 0], "--", color=gray, lw=1.2)
    ax.plot(x0, y0, "o", color=blue, markersize=7)
    ax.plot(x1, 0, "o", color=navy, markersize=6)
    ax.text(x0, -0.38, "$x_0$", ha="center", fontsize=22, color=navy)
    ax.text(x1, -0.38, "$x_1$", ha="center", fontsize=22, color=navy)
    ax.text(-0.16, y0, "$y_0$", ha="right", va="center", fontsize=22, color=navy)
    ax.annotate("$(x_0,y_0)$", (x0, y0), xytext=(-18, 16),
                textcoords="offset points", ha="right", fontsize=21, color=blue)
    ax.text(4.65, 2.7, "Slope: $k$", fontsize=18, color=blue)

    left = 0.57
    fig.text(left, 0.79, "Equation of the line", fontsize=16, color=navy)
    fig.text(left, 0.72, r"$y(x)=k(x-x_0)+y_0$", fontsize=24, color=blue)
    fig.text(left, 0.61, "At the root, $y(x_1)=0$", fontsize=16, color=navy)
    fig.text(left, 0.54, r"$0=k(x_1-x_0)+y_0$", fontsize=24, color=navy)
    fig.text(left, 0.43, r"$x_1=x_0-\frac{y_0}{k}$", fontsize=27, color=navy)
    fig.text(left, 0.31, r"$k=y'(x_0),\qquad y_0=y(x_0)$", fontsize=22, color=navy)
    fig.text(left, 0.16, r"$x_1=x_0-\frac{y(x_0)}{y'(x_0)}$", fontsize=29, color=blue)
    fig.text(left, 0.065, "For a line with nonzero slope, one step gives the root.",
             fontsize=12, color=navy)
    fig.savefig(Path(__file__).with_name("newton_line.png"), dpi=200, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
