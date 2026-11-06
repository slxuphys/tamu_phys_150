"""Render the two-body gravity diagram used in Lecture 15."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def main():
    navy, red, gray = "#223247", "#cf343b", "#969da7"
    plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "stix"})
    fig = plt.figure(figsize=(16, 9), facecolor="white")
    fig.text(0.05, 0.92, "Gravitational forces between two bodies",
             fontsize=29, weight="bold", color=navy)
    ax = fig.add_axes([0.045, 0.18, 0.48, 0.66])
    ax.set(xlim=(-0.5, 8.3), ylim=(-0.5, 6.4), aspect="equal")
    ax.axis("off")

    def arrow(start, end, color, width=2, size=14, style="-|>"):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                    mutation_scale=size, linewidth=width,
                                    color=color, shrinkA=0, shrinkB=0))

    arrow((0, 0), (8, 0), navy)
    arrow((0, 0), (0, 6.1), navy)
    ax.text(8.12, -0.08, "$x$", fontsize=26, color=navy)
    ax.text(-0.15, 6.2, "$y$", fontsize=26, color=navy)
    ax.text(-0.3, -0.42, r"$O\,(0,0)$", fontsize=21, color=navy)

    x1, x2, y = 2.0, 7.0, 4.2
    ax.plot([0, 7.8], [y, y], "--", color=gray, linewidth=1.3, zorder=0)
    for x in (x1, x2):
        ax.plot([x, x], [3.1, y], "--", color=gray, linewidth=1.2)
    # Each force is applied at its own body and points toward the other.
    arrow((x1, y), (x1 + 1.9, y), red, width=3.6, size=20)
    arrow((x2, y), (x2 - 1.9, y), red, width=3.6, size=20)
    ax.add_patch(Circle((x1, y), 0.28, facecolor=navy, edgecolor="#162435", zorder=4))
    ax.add_patch(Circle((x2, y), 0.28, facecolor="#f4bf4d", edgecolor="#aa791f", linewidth=2, zorder=4))
    for x, i in ((x1, 1), (x2, 2)):
        ax.text(x, 5.95, rf"$m_{i}$", ha="center", fontsize=29, color=navy)
        ax.text(x, 5.3, rf"$\vec r_{i}=(x_{i},y_{i})$", ha="center", fontsize=23, color=navy)
    ax.text(3.0, 4.55, r"$\vec F_{12}$", ha="center", fontsize=29, color=red)
    ax.text(6.0, 4.55, r"$\vec F_{21}$", ha="center", fontsize=29, color=red)
    arrow((x1, 3.25), (x2, 3.25), gray, width=1.5, size=13, style="<->")
    ax.text(4.5, 2.7, r"$\Delta r=|\vec r_2-\vec r_1|$", ha="center", fontsize=25, color=navy)

    x = 0.57
    fig.text(x, 0.72, r"$\vec F_{12}=-\frac{Gm_1m_2}{(\Delta r)^3}(\vec r_1-\vec r_2)$", fontsize=29, color=red)
    fig.text(x, 0.63, "Force on body 1 from body 2.", fontsize=19, color=navy)
    fig.text(x, 0.47, r"$\vec F_{21}=-\frac{Gm_1m_2}{(\Delta r)^3}(\vec r_2-\vec r_1)$", fontsize=29, color=red)
    fig.text(x, 0.38, "Force on body 2 from body 1.", fontsize=19, color=navy)
    fig.text(x, 0.23, r"$\vec F_{12}=-\vec F_{21}$", fontsize=31, color=navy)
    fig.text(x, 0.16, "Equal magnitude, opposite directions.", fontsize=18, color=navy)
    fig.text(0.05, 0.065, "Each force acts on a different body.", fontsize=21, color=navy)
    output = Path(__file__).with_name("two-body-gravitational-forces")
    for suffix in (".png", ".svg", ".pdf"):
        fig.savefig(output.with_suffix(suffix), dpi=180, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
