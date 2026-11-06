"""Draw the initial conditions for Lecture 15's two-star simulation."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def main():
    navy, green, gray = "#223247", "#16804a", "#919baa"
    plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "stix"})
    fig, ax = plt.subplots(figsize=(12, 7), facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.92, bottom=0.15, top=0.85)
    ax.set(xlim=(-1.05, 1.05), ylim=(-0.8, 0.8), aspect="equal")
    ax.axis("off")
    fig.suptitle("Initial positions and velocities of two stars",
                 fontsize=25, weight="bold", color=navy, y=0.96)

    def arrow(start, end, color, width=1.5, size=12):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=size, linewidth=width,
                                    color=color, shrinkA=0, shrinkB=0))

    arrow((-0.95, 0), (0.95, 0), gray)
    arrow((0, -0.72), (0, 0.72), gray)
    ax.text(0.98, -0.025, "$x$", fontsize=23, color=navy)
    ax.text(0.035, 0.71, "$y$", fontsize=23, color=navy)
    ax.plot(0, 0, ".", color=navy, markersize=7)
    ax.text(0.035, -0.1, r"$O\ (0,0)$", fontsize=17, color=navy)

    # The actual coordinates and velocities match the simulation cell.
    stars = [(-0.5, 0.6, "tab:blue", 1), (0.5, -0.6, "tab:orange", 2)]
    for x, vy, color, i in stars:
        arrow((x, 0), (x, vy), green, width=3, size=16)
        ax.plot(x, 0, "o", color=color, markersize=23, zorder=5)
        if i == 1:
            ax.text(x - 0.07, -0.16, "Star 1", ha="center", color=color, fontsize=20)
            ax.text(x - 0.07, -0.29, r"$\vec r_1=(-0.5,\,0)$", ha="center", color=navy, fontsize=21)
            ax.text(x - 0.1, 0.35, r"$\vec v_1=(0,\,0.6)$", ha="right", color=green, fontsize=22)
        else:
            ax.text(x + 0.07, 0.16, "Star 2", ha="center", color=color, fontsize=20)
            ax.text(x + 0.07, 0.29, r"$\vec r_2=(0.5,\,0)$", ha="center", color=navy, fontsize=21)
            ax.text(x + 0.1, -0.35, r"$\vec v_2=(0,\,-0.6)$", ha="left", color=green, fontsize=22)

    fig.text(0.5, 0.065, r"$Gm_1=Gm_2=1$    |    Equal masses; equal and opposite initial velocities.",
             ha="center", fontsize=17, color=navy)
    path = Path(__file__).with_name("two-star-initial-conditions")
    for suffix in (".png", ".svg", ".pdf"):
        fig.savefig(path.with_suffix(suffix), dpi=180, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
