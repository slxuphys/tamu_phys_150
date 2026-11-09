"""Render three Newton iterations on one set of axes for Lecture 16."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    navy, blue, gray = "#223247", "#2878b5", "#969da7"
    colors = ["#cf343b", "#c77b12", "#25845b"]
    plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "stix"})
    f = lambda x: x**2 - 2
    df = lambda x: 2 * x
    iterates = [3.0]
    for _ in range(3):
        x = iterates[-1]
        iterates.append(x - f(x) / df(x))

    fig, ax = plt.subplots(figsize=(12, 9), facecolor="white")
    fig.subplots_adjust(left=0.09, right=0.96, bottom=0.24, top=0.73)
    fig.text(0.07, 0.94, "Newton’s method: three iterations", fontsize=25,
             weight="bold", color=navy)
    fig.text(0.07, 0.88, r"$f(x)=x^2-2,\quad f'(x)=2x,\quad x_0=3$",
             fontsize=23, color=navy)
    fig.text(0.07, 0.79,
             r"$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}"
             r"=x_n-\frac{x_n^2-2}{2x_n}$",
             fontsize=27, color=blue)

    x = np.linspace(1.12, 3.18, 600)
    ax.plot(x, f(x), color=blue, lw=2.4, label="$f(x)=x^2-2$")
    ax.axhline(0, color=navy, lw=1.2)
    for n, color in enumerate(colors):
        xn, xnext = iterates[n:n+2]
        step = xn - xnext
        tangent_x = np.linspace(xnext - 0.12 * step, xn + 0.06 * step, 100)
        ax.plot(tangent_x, f(xn) + df(xn) * (tangent_x - xn),
                color=color, lw=2.5, label=rf"Iteration {n+1}: tangent at $x_{n}$",
                zorder=3+n)
        ax.plot([xn, xn], [0, f(xn)], "--", color=gray, lw=1.2)
        ax.plot(xn, f(xn), "o", color=color, markersize=6, zorder=7)
        ax.plot(xnext, 0, "o", color=color, markersize=6, zorder=7)

    ax.annotate("$x_0$", (iterates[0], 0), xytext=(0, -24),
                textcoords="offset points", ha="center", fontsize=21, color=navy)
    # Stagger the labels because the final two estimates are close together.
    offsets = [(0, -27), (32, -46), (-32, -70)]
    for n, (color, offset) in enumerate(zip(colors, offsets)):
        ax.annotate(rf"$x_{n+1}$", (iterates[n+1], 0), xytext=offset,
                    textcoords="offset points", ha="center", fontsize=21,
                    color=color, arrowprops=dict(arrowstyle="-", color=color, lw=1))
    ax.set(xlim=(1.12, 3.18), ylim=(-2.4, 8.2))
    ax.set_xlabel("$x$", fontsize=23, color=navy)
    ax.set_ylabel("$f(x)$", fontsize=23, color=navy)
    ax.set_xticks([])
    ax.set_yticks([0, 2, 4, 6, 8])
    ax.tick_params(labelsize=12, colors=navy)
    ax.spines[["top", "right", "bottom"]].set_visible(False)
    ax.spines["left"].set_color(gray)
    ax.legend(loc="upper left", frameon=False, fontsize=14)

    fig.text(0.07, 0.15,
             rf"$x_0={iterates[0]:.6f}\ \longrightarrow\ x_1={iterates[1]:.6f}"
             rf"\ \longrightarrow\ x_2={iterates[2]:.6f}\ \longrightarrow\ x_3={iterates[3]:.6f}$",
             fontsize=21, color=navy)
    fig.text(0.07, 0.09, "Each tangent’s x-intercept gives the next estimate.",
             fontsize=17, color=navy)
    fig.text(0.07, 0.045, r"The estimates approach $\sqrt{2}\approx 1.414214$; the final steps become very small.",
             fontsize=15, color=navy)
    fig.savefig(Path(__file__).with_name("newton_three_iterations.png"), dpi=200,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
