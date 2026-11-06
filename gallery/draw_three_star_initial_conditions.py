"""Draw the initial conditions of the first three-body example in Lecture 15."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def main():
    navy, green, gray = "#223247", "#16804a", "#919baa"
    plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "stix"})
    fig = plt.figure(figsize=(14, 8), facecolor="white")
    fig.text(0.05, 0.92, "Initial positions and velocities of three stars",
             fontsize=26, weight="bold", color=navy)
    ax = fig.add_axes([0.04, 0.19, 0.52, 0.63])
    ax.set(xlim=(-0.95, 0.95), ylim=(-0.75, 0.75), aspect="equal")
    ax.axis("off")

    def arrow(start, end, color, width=1.5, size=12):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=size, linewidth=width,
                                    color=color, shrinkA=0, shrinkB=0))

    arrow((-0.86, 0), (0.86, 0), gray)
    arrow((0, -0.66), (0, 0.66), gray)
    ax.text(0.89, -0.025, "$x$", fontsize=24, color=navy)
    ax.text(0.035, 0.66, "$y$", fontsize=24, color=navy)
    ax.plot(0, 0, ".", markersize=6, color=navy)
    ax.text(-0.025, -0.12, r"$O\ (0,0)$", ha="right", fontsize=17, color=navy)

    stars = [((0.1, 0), (0, 0), "tab:blue"),
             ((0.5, 0), (-0.2, 0.5), "tab:orange"),
             ((-0.5, 0), (0.2, -0.5), "tab:green")]
    for i, ((x, y), (vx, vy), color) in enumerate(stars, 1):
        if vx or vy:
            arrow((x, y), (x + vx, y + vy), green, width=3, size=17)
        ax.plot(x, y, "o", color=color, markersize=21, zorder=5)
        offset = {1: (0.08, -0.18), 2: (0.08, -0.12), 3: (-0.08, 0.14)}[i]
        ax.text(x + offset[0], y + offset[1], f"Star {i}",
                ha="center", fontsize=18, color=color)
    ax.text(0.16, 0.12, r"$\vec v_1=0$", fontsize=21, color=green)
    ax.text(0.47, 0.32, r"$\vec v_2$", fontsize=27, color=green)
    ax.text(-0.57, -0.32, r"$\vec v_3$", fontsize=27, color=green)

    labels = [
        ("Star 1: initially at rest", r"$\vec r_1=(0.1,\,0)$", r"$\vec v_1=(0,\,0)$", "tab:blue"),
        ("Star 2", r"$\vec r_2=(0.5,\,0)$", r"$\vec v_2=(-0.2,\,0.5)$", "tab:orange"),
        ("Star 3", r"$\vec r_3=(-0.5,\,0)$", r"$\vec v_3=(0.2,\,-0.5)$", "tab:green"),
    ]
    for y, (title, position, velocity, color) in zip((0.77, 0.54, 0.31), labels):
        fig.text(0.61, y, title, fontsize=21, color=color)
        fig.text(0.61, y - 0.065, position, fontsize=24, color=navy)
        fig.text(0.61, y - 0.13, velocity, fontsize=24, color=green)
    fig.text(0.05, 0.065, r"$Gm_1=Gm_2=Gm_3=1$    |    Green arrows show initial velocity, not force.",
             fontsize=18, color=navy)
    path = Path(__file__).with_name("three-star-initial-conditions")
    for suffix in (".png", ".svg", ".pdf"):
        fig.savefig(path.with_suffix(suffix), dpi=180, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
