import math
import time
import traceback
import tkinter as tk

ALL = ("v", "u", "a", "s", "t", "th")
NAME = {"v": "final velocity", "u": "initial velocity", "a": "acceleration",
        "s": "displacement", "t": "time", "th": "theta"}
SYMBOL = {"v": "v", "u": "u", "a": "a", "s": "s", "t": "t", "th": "θ"}
UNIT = {"v": "m/s", "u": "m/s", "a": "m/s²", "s": "m", "t": "s", "th": "°"}
DEFAULT_G = 9.81


class SolveError(Exception):
    """A friendly message for the person at the keyboard."""


def _roots_to_u(base, r):
    """Both answers of a quadratic for u (base +/- r), keeping only speeds >= 0."""
    out = []
    for x in (base + r, base - r):
        if x >= -1e-9:
            x = max(x, 0.0)
            if all(abs(x - y) > 1e-9 for y in out):
                out.append(x)
    return out


def _safe_sqrt(d, ref, tol=0.005):
    """sqrt(d), forgiving a tiny negative d that comes from rounded inputs."""
    if d < -tol * ref - 1e-9:
        return None
    return math.sqrt(max(d, 0.0))


# A rule returns:  None -> can't use it right now (it would divide by zero)
#                  []   -> the numbers are impossible
#                  [x]  -> the answer (or [x, y] when two answers are possible)

def _t_land(k):
    """Landing time = the LATER time the fireball is at height s (it is coming down)."""
    uy = k["u"] * math.sin(k["th"])
    root = _safe_sqrt(uy * uy + 2 * k["a"] * k["s"], uy * uy + abs(2 * k["a"] * k["s"]))
    if root is None:
        return []
    t = (-uy - root) / k["a"]
    return [t] if t > 1e-9 else []


def _s_from_t(k):
    return [k["u"] * math.sin(k["th"]) * k["t"] + 0.5 * k["a"] * k["t"] ** 2]


def _v_from_s(k):
    root = _safe_sqrt(k["u"] ** 2 + 2 * k["a"] * k["s"], k["u"] ** 2 + abs(2 * k["a"] * k["s"]))
    return [] if root is None else [root]


def _u_from_v(k):
    root = _safe_sqrt(k["v"] ** 2 - 2 * k["a"] * k["s"], k["v"] ** 2 + abs(2 * k["a"] * k["s"]))
    return [] if root is None else [root]


def _s_from_v(k):
    return [(k["v"] ** 2 - k["u"] ** 2) / (2 * k["a"])]


def _th_from_t(k):
    if k["u"] < 1e-9:
        return None
    x = (k["s"] - 0.5 * k["a"] * k["t"] ** 2) / (k["u"] * k["t"])
    if abs(x) > 1.01:                  # a little slack for rounded inputs (e.g. a straight-up shot)
        return []
    return [math.asin(max(-1.0, min(1.0, x)))]


def _u_from_t(k):
    sn = math.sin(k["th"])
    if abs(sn) < 1e-9:
        return None            # a flat shot: time says nothing about the speed
    u = (k["s"] - 0.5 * k["a"] * k["t"] ** 2) / (sn * k["t"])
    return [] if u < -1e-9 else [max(u, 0.0)]


def _a_from_t(k):
    a = 2 * (k["s"] - k["u"] * math.sin(k["th"]) * k["t"]) / k["t"] ** 2
    return [a] if a < -1e-9 else []


def _a_from_v(k):
    if abs(k["s"]) < 1e-9:
        return None
    a = (k["v"] ** 2 - k["u"] ** 2) / (2 * k["s"])
    return [a] if a < -1e-9 else []


def _a_from_tv(k):
    ux = k["u"] * math.cos(k["th"])
    uy = k["u"] * math.sin(k["th"])
    root = _safe_sqrt(k["v"] ** 2 - ux ** 2, k["v"] ** 2)
    if root is None:
        return []
    a = (-root - uy) / k["t"]                         # it lands while going DOWN
    return [a] if a < -1e-9 else []


def _u_quad(k):
    """u from theta, a, t, v  (a quadratic, so there can be two answers)."""
    sn, cs = math.sin(k["th"]), math.cos(k["th"])
    root = _safe_sqrt(k["v"] ** 2 - (k["a"] * k["t"] * cs) ** 2, k["v"] ** 2)
    if root is None:
        return []
    return _roots_to_u(-k["a"] * k["t"] * sn, root)


def _u_quad_no_a(k):
    """u from theta, s, t, v when a is unknown (also a quadratic)."""
    sn, cs = math.sin(k["th"]), math.cos(k["th"])
    root = _safe_sqrt(k["v"] ** 2 - (2 * k["s"] * cs / k["t"]) ** 2, k["v"] ** 2)
    if root is None:
        return []
    return _roots_to_u(2 * k["s"] * sn / k["t"], root)


# (what it finds, what it needs, function, message if the numbers are impossible)
RULES = [
    ("t", ("u", "th", "a", "s"), _t_land,
     "With these numbers the fireball never comes down to the landing height. "
     "Try a faster launch or a steeper angle."),
    ("s", ("u", "th", "a", "t"), _s_from_t, ""),
    ("v", ("u", "a", "s"), _v_from_s,
     "The fireball runs out of speed before it reaches that height. "
     "Try a faster launch or a smaller height."),
    ("u", ("v", "a", "s"), _u_from_v,
     "That final speed is too small for that displacement. Try a bigger final velocity."),
    ("s", ("u", "a", "v"), _s_from_v, ""),
    ("th", ("u", "a", "s", "t"), _th_from_t,
     "No launch angle fits those values (it would need sin θ above 1). "
     "Check the speed, time and displacement."),
    ("u", ("th", "a", "s", "t"), _u_from_t,
     "Those values would need a negative launch speed. Check the sign of theta and the time."),
    ("a", ("u", "th", "s", "t"), _a_from_t,
     "Those values would need gravity to pull UP. Check the numbers (a should come out negative)."),
    ("a", ("u", "s", "v"), _a_from_v,
     "Those values would need gravity to pull UP. Check the numbers (a should come out negative)."),
    ("a", ("u", "th", "t", "v"), _a_from_tv,
     "Those values would need gravity to pull UP. Check the numbers (a should come out negative)."),
    ("u", ("th", "a", "t", "v"), _u_quad,
     "No launch speed fits that combination of theta, time and final velocity."),
    ("u", ("th", "s", "t", "v"), _u_quad_no_a,
     "No launch speed fits that combination of theta, displacement, time and final velocity."),
]


def _expand(known, problems):
    """Apply rules until nothing new can be found. Returns a list of possible states."""
    k = dict(known)
    if "u" in k and "th" not in k and k["u"] < 1e-9:
        k["th"] = 0.0                      # speed 0: the angle doesn't matter
    for unknown, needs, func, why in RULES:
        if unknown in k or any(n not in k for n in needs):
            continue
        candidates = func(k)
        if candidates is None:
            continue
        if not candidates:
            problems.append(why)
            return []
        out = []
        for value in candidates:
            nxt = dict(k)
            nxt[unknown] = value
            out.extend(_expand(nxt, problems))
        return out
    return [k]


def _solvable(names):
    """Would these variables be enough? (used to suggest what to type next)"""
    names = set(names)
    grew = True
    while grew:
        grew = False
        for unknown, needs, _func, _why in RULES:
            if unknown not in names and all(n in names for n in needs):
                names.add(unknown)
                grew = True
    return all(n in names for n in ALL)


def _close(x, y, scale):
    return abs(x - y) <= 0.02 * scale + 1e-9


def _validate(st, case):
    """Check a complete set of six values. Returns None if fine, else a message."""
    u, th, a, s, t, v = (st[n] for n in ("u", "th", "a", "s", "t", "v"))
    ux, uy = u * math.cos(th), u * math.sin(th)
    s_calc = uy * t + 0.5 * a * t * t
    vy = uy + a * t
    v_calc = math.hypot(ux, vy)
    fit = (f"These numbers don't fit together: with u = {u:.2f} m/s, θ = {math.degrees(th):.2f}°, "
           f"a = {a:.2f} m/s² and t = {t:.2f} s")
    if not _close(s, s_calc, max(abs(uy * t), abs(0.5 * a * t * t), abs(s), 1.0)):
        return f"{fit}, the displacement would be {s_calc:.2f} m, not {s:.2f} m."
    if not _close(v, v_calc, max(v, v_calc, 1.0)):
        return f"{fit}, the final velocity would be {v_calc:.2f} m/s, not {v:.2f} m/s."
    if vy > 0.02 * max(abs(uy), abs(a * t), 1.0):
        return (f"At t = {t:.2f} s the fireball is still going up ({vy:.2f} m/s), so it hasn't "
                "landed yet. It can only land while coming down - try a larger time.")
    if case == "H2G" and s > -1e-9:
        return (f"Height → Ground needs the fireball to land lower than it started, but these "
                f"numbers give s = {s:.2f} m. Try world 1-1 or 1-3 instead.")
    if case == "G2H" and s < 1e-9:
        return (f"Ground → Height needs the fireball to land higher than it started, but these "
                f"numbers give s = {s:.2f} m. Try world 1-1 or 1-2 instead.")
    if case == "G2H" and ux < 1e-6 * max(u, 1.0):
        return ("A straight-up shot (θ = 90°) can't land on a platform - it would hit the "
                "underside. Use a smaller angle.")
    return None


def solve(case, typed):
    """
    case  : "G2G", "H2G" or "G2H"
    typed : dict with any of v, u, a, s, t, th  (th in degrees)
    Returns a dict with all six values plus extras, or raises SolveError.
    """
    try:
        return _solve(case, typed)
    except (OverflowError, ZeroDivisionError, ValueError):
        raise SolveError("Those numbers are too extreme to calculate. Try smaller ones.") from None


def _solve(case, typed):
    k = dict(typed)
    notes = []

    # --- tidy up what was typed --------------------------------------
    for n in ("u", "v"):
        if n in k and k[n] < 0:
            raise SolveError(f"The {NAME[n]} is a speed, so it can't be negative.")
    if "t" in k and k["t"] <= 0:
        raise SolveError("Time must be bigger than 0.")
    if "th" in k:
        if not -90.0 <= k["th"] <= 90.0:
            raise SolveError("Theta must be between -90° and 90° (measured up from the horizontal).")
        k["th"] = math.radians(k["th"])
    if "a" in k:
        if k["a"] == 0:
            raise SolveError("Acceleration can't be 0 - with no gravity the fireball never lands.")
        if k["a"] > 0:
            notes.append(f"Gravity pulls down, so I used a = -{k['a']:g} m/s².")
        k["a"] = -abs(k["a"])
    if case == "G2G":
        k["s"] = 0.0                                   # same height at start and end
    elif "s" in k:
        if k["s"] == 0:
            raise SolveError("Displacement can't be 0 in this world. Type the height difference "
                             "as a positive number.")
        k["s"] = -abs(k["s"]) if case == "H2G" else abs(k["s"])

    # --- solve ---------------------------------------------------------
    problems = []
    finals = _expand(k, problems)
    complete = [st for st in finals if all(n in st for n in ALL)]
    if not complete:
        if problems:
            raise SolveError(problems[0])
        stuck = [NAME[n] for n in ALL if n not in finals[0]]
        hints = [f"{NAME[n]} ({SYMBOL[n]})" for n in ALL
                 if n not in k and _solvable(set(k) | {n})]
        if hints:
            raise SolveError(f"I can't work out the {', '.join(stuck)} yet. Type one more "
                             f"value, for example: {', '.join(hints)}.")
        raise SolveError("I need more values to solve this. Type at least three of the boxes.")

    good, why_not = [], []
    for st in complete:
        why = _validate(st, case)
        if why is None:
            good.append(st)
        else:
            why_not.append(why)
    if not good:
        msg = why_not[0]
        if "a" in typed and msg.startswith("These numbers don't fit"):
            msg += " (Clear the acceleration box if you want me to solve for it.)"
        raise SolveError(msg)

    unique = []
    for st in good:
        if all(any(abs(st[n] - o[n]) > 1e-6 * max(1.0, abs(o[n])) for n in ALL) for o in unique):
            unique.append(st)
    st = unique[0]
    alternatives = unique[1:]

    # --- extras for the picture ------------------------------------------
    u, th, a, s, t, v = (st[n] for n in ("u", "th", "a", "s", "t", "v"))
    ux, uy = u * math.cos(th), u * math.sin(th)
    land = _t_land(st)
    t_land = land[0] if land else t                    # exact landing time for the animation
    d = uy * uy + 2 * a * s
    t_first = (-uy + math.sqrt(max(d, 0.0))) / a       # first time at height s (going up)
    vy_end = uy + a * t_land
    g = -a
    rise = uy * uy / (2 * g) if uy > 0 else 0.0
    y0 = -s if s < 0 else 0.0                          # launch height above the floor

    if "t" in typed and abs(t - t_land) > 0.01 * t_land:
        notes.append(f"Your time ({t:.2f} s) is a little off what the other values give "
                     f"({t_land:.2f} s). I animated the exact path.")
    if alternatives:
        diffs = []
        for n in ALL:
            if abs(alternatives[0][n] - st[n]) > 1e-6 * max(1.0, abs(st[n])):
                val = math.degrees(alternatives[0][n]) if n == "th" else alternatives[0][n]
                diffs.append(f"{SYMBOL[n]} = {val:.2f} {UNIT[n]}")
        notes.append("Two answers fit these numbers. Another one is " + ", ".join(diffs)
                     + ". I'm showing the first.")

    res = {n: st[n] for n in ALL}
    res.update(
        th_deg=math.degrees(th), ux=ux, uy=uy, vy_end=vy_end, R=ux * t_land, y0=y0,
        rise=rise, t_peak=(uy / g if uy > 0 else 0.0), peak_y=y0 + rise,
        impact=max(0.0, math.degrees(math.atan2(-vy_end, ux))),
        t_land=t_land, t_first=t_first, given=set(typed), notes=notes,
        alternatives=[{n: o[n] for n in ALL} for o in alternatives],
    )
    sizes = (res["R"], res["t_land"], res["peak_y"], res["u"], res["v"])
    if not all(math.isfinite(x) for x in sizes) or max(sizes) > 1e9:
        raise SolveError("That flight is too big to draw. Try smaller numbers.")
    return res


# ======================================================================
# 2.  LOOK AND FEEL  (colours and pixel-art sprites drawn with code)
# ======================================================================
SKY = "#5C94FC"
RED = "#D82800"
YELLOW = "#FCC800"
BLACK = "#000000"
WHITE = "#FFFFFF"
BRICK = "#C84C0C"
MORTAR = "#5A1E00"
HILL = "#00A800"
HILL_DARK = "#005800"
GUIDE = "#9DBDFF"

FONT = ("Courier New", 10, "bold")
SMALL = ("Courier New", 9, "bold")

# One letter = one pixel.  "." is see-through.
MARIO = [
    "....RRRRR...",
    "...RRRRRRRRR",
    "...KKKSSKS..",
    "..KSKSSSKSSS",
    "..KSKKSSSKSS",
    "..KKSSSSKKKK",
    "....SSSSSSS.",
    "...RRBRRR...",
    "..RRRBRRBRRR",
    ".RRRRBBBBRRR",
    ".WWRBYBBYBWW",
    ".WWWBBBBBBWW",
    ".WWBBBBBBBB.",
    "...BBB..BBB.",
    "..KKK....KKK",
    ".KKKK..KKKK.",
]
MARIO_COLORS = {"R": "#E52521", "S": "#FFB07C", "K": "#6B3A0A",
                "B": "#2038EC", "Y": "#FCD800", "W": "#FFFFFF"}

FIRE = [
    "..RR...",
    ".ROOR..",
    "ROYYOR.",
    "ROYWYOR",
    ".ROYYOR",
    "..ROOR.",
    "...RR..",
]
FIRE_COLORS = {"R": "#D82800", "O": "#FC9838", "Y": "#FCD800", "W": "#FFFFFF"}


def _rotate(grid):
    """Turn a sprite 90 degrees (this is what makes the fireball spin)."""
    return ["".join(row[i] for row in reversed(grid)) for i in range(len(grid[0]))]


FIRE_FRAMES = [FIRE]
for _ in range(3):
    FIRE_FRAMES.append(_rotate(FIRE_FRAMES[-1]))

CASES = (
    ("G2G", "1-1  Ground → Ground"),
    ("H2G", "1-2  Height → Ground"),
    ("G2H", "1-3  Ground → Height"),
)
WORLD = {"G2G": "1-1", "H2G": "1-2", "G2H": "1-3"}
FIELDS = (            # key, symbol, label, unit
    ("v", "v", "Final velocity", "m/s"),
    ("u", "u", "Initial velocity", "m/s"),
    ("a", "a", "Acceleration", "m/s²"),
    ("s", "s", "Displacement", "m"),
    ("t", "t", "Time", "s"),
    ("th", "θ", "Theta", "°"),
)


def nice_step(target):
    """Smallest 1, 2 or 5 times a power of ten that is >= target (for the ruler)."""
    if target <= 0:
        return 1.0
    exp = math.floor(math.log10(target))
    for m in (1, 2, 5, 10):
        if m * 10 ** exp >= target:
            return m * 10 ** exp
    return 10 ** (exp + 1)


def num(x):
    if x == 0:
        return "0.00"
    if abs(x) >= 1e6 or abs(x) < 0.005:
        return f"{x:.3e}"
    return f"{x:.2f}"


# ======================================================================
# 3.  THE APP
# ======================================================================
class SuperProjectileApp:
    CW, CH = 800, 450                  # drawing area (pixels)
    GROUND_H = 64                      # thickness of the brick floor
    LEFT, RIGHT, TOP = 125, 75, 100    # space kept free around the flight path
    MARIO_PX = 3                       # one Mario "pixel" = 3 screen pixels
    FIRE_PX = 4

    def __init__(self, root):
        self.root = root
        root.title("Super Projectile Bros. - Fireball Physics")
        root.configure(bg=RED)
        root.resizable(False, False)
        self.job = None                # the pending animation step, if any
        self.anim = None
        self.geo = {"scale": 1.0}
        self.vars = {key: tk.StringVar() for key in ALL}
        self.vars["a"].set(f"-{DEFAULT_G}")
        self.case = tk.StringVar(value="G2G")
        self._build_left()
        self._build_right()
        root.bind("<Return>", lambda _event: self.fire())
        self.on_case_change()
        self.entries["u"].focus_set()

    # ---------------------------------------------------------------- widgets
    def _build_left(self):
        left = tk.Frame(self.root, bg=RED, padx=14, pady=10)
        left.grid(row=0, column=0, sticky="ns")

        tk.Label(left, text="SUPER PROJECTILE\nBROS.", font=("Courier New", 16, "bold"),
                 fg=YELLOW, bg=RED, justify="left").pack(anchor="w")
        tk.Label(left, text="Fireball physics lab", font=SMALL, fg=WHITE,
                 bg=RED).pack(anchor="w", pady=(0, 8))

        tk.Label(left, text="Choose a world", font=SMALL, fg=YELLOW, bg=RED).pack(anchor="w")
        for value, text in CASES:
            tk.Radiobutton(left, text=text, value=value, variable=self.case,
                           command=self.on_case_change, font=FONT, fg=WHITE, bg=RED,
                           activebackground=RED, activeforeground=YELLOW, selectcolor=YELLOW,
                           anchor="w").pack(anchor="w")

        tk.Label(left, text="What do you know?", font=SMALL, fg=YELLOW,
                 bg=RED).pack(anchor="w", pady=(12, 2))
        grid = tk.Frame(left, bg=RED)
        grid.pack(anchor="w")
        self.entries = {}
        for row, (key, sym, label, unit) in enumerate(FIELDS):
            tk.Label(grid, text=f"{sym}  {label}", font=FONT, fg=WHITE, bg=RED, anchor="w",
                     width=19).grid(row=row, column=0, sticky="w", pady=3)
            entry = tk.Entry(grid, textvariable=self.vars[key], width=9, font=FONT,
                             justify="right", bg=WHITE, fg=BLACK, insertbackground=BLACK,
                             disabledbackground="#C8C8C8", disabledforeground="#303030",
                             relief="sunken", bd=3)
            entry.grid(row=row, column=1, padx=6)
            unit_label = tk.Label(grid, text=unit, font=FONT, fg=YELLOW, bg=RED, anchor="w",
                                  width=12)
            unit_label.grid(row=row, column=2, sticky="w")
            self.entries[key] = entry
            if key == "s":
                self.s_unit = unit_label

        tk.Label(left, text=("Type 3 or more values and leave the rest blank.\n"
                             "Type heights as positive numbers.\n"
                             "Acceleration starts as Earth's gravity;\n"
                             "clear it if you want to solve for it."),
                 font=SMALL, fg=WHITE, bg=RED, justify="left").pack(anchor="w", pady=(8, 0))

        buttons = tk.Frame(left, bg=RED)
        buttons.pack(anchor="w", pady=(10, 8))
        tk.Button(buttons, text="Fire!", command=self.fire, font=("Courier New", 13, "bold"),
                  bg=YELLOW, fg=BLACK, activebackground="#FFE266", relief="raised", bd=4,
                  width=9).pack(side="left", padx=(0, 8))
        tk.Button(buttons, text="Clear", command=self.reset, font=("Courier New", 13, "bold"),
                  bg=YELLOW, fg=BLACK, activebackground="#FFE266", relief="raised", bd=4,
                  width=7).pack(side="left")

        self.message = tk.Label(left, text="", font=SMALL, bg=BLACK, fg=WHITE, justify="left",
                                anchor="nw", wraplength=290, width=40, height=9, padx=6, pady=4)
        self.message.pack(anchor="w")

    def _build_right(self):
        right = tk.Frame(self.root, bg=BLACK)
        right.grid(row=0, column=1, sticky="n")
        self.canvas = tk.Canvas(right, width=self.CW, height=self.CH, bg=SKY,
                                highlightthickness=0)
        self.canvas.pack()
        row = tk.Frame(right, bg=BLACK)
        row.pack(fill="x")
        self.txt_vars = self._make_text(row, 44)
        self.txt_more = self._make_text(row, 50)

    @staticmethod
    def _make_text(parent, width):
        box = tk.Text(parent, width=width, height=8, bg=BLACK, fg=WHITE, font=FONT, bd=0,
                      highlightthickness=0, padx=10, pady=8, state="disabled",
                      cursor="arrow", wrap="none")
        box.pack(side="left", fill="both")
        box.tag_configure("head", foreground="#A8A8A8")
        box.tag_configure("you", foreground=WHITE)
        box.tag_configure("solved", foreground=YELLOW)
        box.tag_configure("more", foreground="#9CFC9C")
        return box

    @staticmethod
    def _set_text(box, lines):
        box.config(state="normal")
        box.delete("1.0", "end")
        for text, tag in lines:
            box.insert("end", text + "\n", tag)
        box.config(state="disabled")

    def show_message(self, text, kind="note"):
        colour = {"error": "#FF9C9C", "ok": "#9CFC9C"}.get(kind, "#FFE9A8")
        self.message.config(text=text, fg=colour)

    # ---------------------------------------------------------------- buttons
    def on_case_change(self):
        self.stop()
        case = self.case.get()
        entry = self.entries["s"]
        if case == "G2G":
            self.vars["s"].set("0")
            entry.config(state="disabled")
            self.s_unit.config(text="m (always 0)")
        else:
            if self.vars["s"].get() == "0":
                self.vars["s"].set("")
            entry.config(state="normal")
            self.s_unit.config(text="m (drop)" if case == "H2G" else "m (climb)")
        self.show_message("")
        self._set_text(self.txt_vars, [("  Your answers appear here after you press Fire!", "head")])
        self._set_text(self.txt_more, [])
        self.draw_scene()

    def reset(self):
        self.stop()
        for key in ALL:
            self.vars[key].set("")
        self.vars["a"].set(f"-{DEFAULT_G}")
        self.on_case_change()

    def read_inputs(self):
        typed = {}
        for key, _sym, label, _unit in FIELDS:
            raw = self.vars[key].get().strip().replace(",", ".").replace("\u2212", "-")
            if not raw:
                continue
            try:
                value = float(raw)
            except ValueError:
                raise SolveError(f"'{self.vars[key].get()}' isn't a number. "
                                 f"Fix the {label} box.") from None
            if not math.isfinite(value) or abs(value) > 1e7:
                raise SolveError(f"The {label} box needs an ordinary number "
                                 "(smaller than 10,000,000).")
            typed[key] = value
        return typed

    def fire(self):
        self.stop()
        try:
            res = solve(self.case.get(), self.read_inputs())
        except SolveError as err:
            self.show_message(str(err), "error")
            return
        except Exception as err:                       # a bug, not the user's fault
            self.show_message(f"Something unexpected went wrong: {err}", "error")
            traceback.print_exc()
            return
        if res["notes"]:
            self.show_message("\n\n".join(res["notes"]), "note")
        else:
            self.show_message("Fireball away!", "ok")
        self.show_results(res)
        self.start_animation(res)

    def show_results(self, res):
        case = self.case.get()
        lines = [("  Variable            Value        Source", "head")]
        for key, sym, label, unit in FIELDS:
            value = res["th_deg"] if key == "th" else res[key]
            if key == "s" and case == "G2G":
                source, tag = "fixed", "you"
            elif key in res["given"]:
                source, tag = "you", "you"
            else:
                source, tag = "solved", "solved"
            lines.append((f" {sym}  {label:<16}{num(value):>9} {unit:<4} {source}", tag))
        self._set_text(self.txt_vars, lines)

        more = [(" Extra results", "head"),
                (f" Horizontal range     R  = {num(res['R'])} m", "more"),
                (f" Launch height           = {num(res['y0'])} m", "more"),
                (f" Highest point (floor)   = {num(res['peak_y'])} m", "more"),
                (f" Time to highest point   = {num(res['t_peak'])} s", "more"),
                (f" Horizontal speed    vx = {num(res['ux'])} m/s (constant)", "more"),
                (f" Hits at {num(res['impact'])}° below the horizontal", "more")]
        self._set_text(self.txt_more, more)

    # ------------------------------------------------------------ animation
    def stop(self):
        if self.job is not None:
            self.root.after_cancel(self.job)
            self.job = None

    def start_animation(self, res):
        self.draw_scene(res)
        duration = min(max(res["t_land"], 1.6), 6.5)    # real seconds on screen
        self.anim = {"res": res, "t0": time.perf_counter(), "T": duration}
        self._frame()

    def _frame(self):
        a = self.anim
        res = a["res"]
        now = time.perf_counter()
        frac = min(1.0, (now - a["t0"]) / a["T"])
        ts = frac * res["t_land"]                       # simulated seconds
        x = res["ux"] * ts
        y = res["y0"] + res["uy"] * ts + 0.5 * res["a"] * ts * ts
        px, py = self._to_px(x, y)
        self.canvas.delete("fb")
        self._sprite(FIRE_FRAMES[int((now - a["t0"]) * 14) % 4], FIRE_COLORS,
                     px - 3.5 * self.FIRE_PX, py - 3.5 * self.FIRE_PX, self.FIRE_PX, "fb")
        self._hud_set(x, y, ts)
        if frac < 1.0:
            self.job = self.root.after(16, self._frame)
        else:
            self.canvas.delete("fb")
            self._boom(px, py, 0)

    def _boom(self, px, py, step):
        c = self.canvas
        c.delete("boom")
        if step < 8:
            r = 5 + 4 * step
            for k in range(7):                          # a burst thrown upwards
                ang = k * math.pi / 6
                cx, cy = px + math.cos(ang) * r, py - math.sin(ang) * r
                c.create_rectangle(cx - 3, cy - 3, cx + 3, cy + 3,
                                   fill=YELLOW if k % 2 else "#E52521", outline="", tags="boom")
            self.job = self.root.after(35, self._boom, px, py, step + 1)
        else:
            self.job = None
            self._markers(self.anim["res"])

    def _markers(self, res):
        c = self.canvas
        if res["uy"] > 0 and res["rise"] > 0:
            ax, ay = self._to_px(res["ux"] * res["t_peak"], res["peak_y"])
            c.create_oval(ax - 4, ay - 4, ax + 4, ay + 4, fill=YELLOW, outline=BLACK, width=2)
            self._tag_point(ax, ay, f"highest {num(res['peak_y'])} m", lift=22)
        lx, ly = self._to_px(res["R"], res["y0"] + res["s"])
        self._tag_point(lx, ly, f"lands at x = {num(res['R'])} m")

    def _tag_point(self, px, py, text, lift=10):
        """Write a label beside a dot, on whichever side keeps it inside the picture."""
        if px + 8 + 7.4 * len(text) <= self.CW - 4:
            self._label(px + 8, py - lift, text, anchor="sw")
        else:
            self._label(px - 8, py - lift, text, anchor="se")

    # -------------------------------------------------------------- drawing
    def _to_px(self, x, y):
        """Metres -> screen pixels (x to the right of Mario, y up from the floor)."""
        return (self.LEFT + x * self.geo["scale"],
                self.CH - self.GROUND_H - y * self.geo["scale"])

    def _label(self, x, y, text, anchor="center", size=9, colour=WHITE, tags=""):
        font = ("Courier New", size, "bold")
        self.canvas.create_text(x + 1, y + 1, text=text, anchor=anchor, font=font, fill=BLACK,
                                tags=tags)
        return self.canvas.create_text(x, y, text=text, anchor=anchor, font=font, fill=colour,
                                       tags=tags)

    def _sprite(self, grid, palette, x, y, px, tag=""):
        """Draw a pixel-art sprite, merging runs of the same colour into one rectangle."""
        c = self.canvas
        for r, row in enumerate(grid):
            c0 = 0
            while c0 < len(row):
                c1 = c0
                while c1 + 1 < len(row) and row[c1 + 1] == row[c0]:
                    c1 += 1
                if row[c0] != ".":
                    c.create_rectangle(x + c0 * px, y + r * px, x + (c1 + 1) * px,
                                       y + (r + 1) * px, fill=palette[row[c0]], outline="",
                                       tags=tag)
                c0 = c1 + 1

    def _bricks(self, x1, y1, x2, y2):
        c = self.canvas
        c.create_rectangle(x1, y1, x2, y2, fill=BRICK, outline=BLACK, width=2)
        row, y = 0, y1
        while y < y2:
            if row:
                c.create_line(x1, y, x2, y, fill=MORTAR, width=2)
            x = x1 + (16 if row % 2 else 32)
            while x < x2:
                c.create_line(x, y, x, min(y + 16, y2), fill=MORTAR, width=2)
                x += 32
            y += 16
            row += 1

    def _scenery(self, yg):
        c = self.canvas
        for cx, w, h in ((250, 220, 70), (560, 300, 110), (770, 170, 55)):
            c.create_oval(cx - w / 2, yg - h, cx + w / 2, yg + h, fill=HILL, outline=HILL_DARK,
                          width=2)
        for cx, cy, s in ((180, 120, 1.0), (450, 92, 1.3), (690, 130, 0.9)):
            for dx, dy, r in ((-28, 4, 16), (0, -6, 22), (30, 4, 17), (0, 6, 20)):
                c.create_oval(cx + (dx - r) * s, cy + (dy - r) * s, cx + (dx + r) * s,
                              cy + (dy + r) * s, fill=WHITE, outline="")

    def _fit_scale(self, res):
        room_w = self.CW - self.LEFT - self.RIGHT
        room_h = self.CH - self.GROUND_H - self.TOP
        scale = 80.0
        if res["R"] > 1e-9:
            scale = min(scale, room_w / res["R"])
        if res["peak_y"] > 1e-9:
            scale = min(scale, room_h / res["peak_y"])
        return scale

    def _ruler(self, sc, yg):
        c = self.canvas
        step = nice_step(70.0 / sc)
        k = 0
        while self.LEFT + k * step * sc <= self.CW - 20:
            x = self.LEFT + k * step * sc
            c.create_line(x, yg, x, yg + 10, fill=WHITE, width=2)
            self._label(x, yg + 22, f"{k * step:g}")
            k += 1
        self._label(self.CW - 8, yg + 46, "distance in m", anchor="e")
        k = 1
        while yg - k * step * sc >= self.TOP - 30:
            y = yg - k * step * sc
            c.create_line(self.LEFT, y, self.CW - 6, y, fill=GUIDE, dash=(2, 6))
            self._label(self.CW - 8, y - 8, f"{k * step:g} m", anchor="e")
            k += 1

    def _target_platform(self, res, sc, yg):
        """A block the fireball lands on. Its left edge sits between the two times the
        path crosses the platform height, so the path never clips the side of the block."""
        x_first = res["ux"] * max(res["t_first"], 0.0)
        x_left = (x_first + res["R"]) / 2
        left = self.LEFT + x_left * sc
        right = self.LEFT + (2 * res["R"] - x_left) * sc
        right = min(max(right, left + 64), self.CW - 4)
        self._bricks(left, yg - res["s"] * sc, right, yg)

    def _path(self, res):
        """Yellow dots along the exact path."""
        pts, last = [], None
        n = 400
        for i in range(n + 1):
            ts = res["t_land"] * i / n
            x = res["ux"] * ts
            y = res["y0"] + res["uy"] * ts + 0.5 * res["a"] * ts * ts
            pts.append(self._to_px(x, y))
        for i, (px, py) in enumerate(pts):
            if last is None or math.hypot(px - last[0], py - last[1]) >= 14 or i == n:
                self.canvas.create_rectangle(px - 3, py - 3, px + 3, py + 3, fill=YELLOW,
                                             outline=BLACK)
                last = (px, py)

    def _hud(self):
        self._label(20, 6, "MARIO", "nw", 11)
        self._label(20, 22, "x 0.00 m", "nw", 11, tags="hud_x")
        self._label(220, 6, "HEIGHT", "nw", 11)
        self._label(220, 22, "y 0.00 m", "nw", 11, tags="hud_y")
        self._label(430, 6, "WORLD", "nw", 11)
        self._label(430, 22, WORLD[self.case.get()], "nw", 11)
        self._label(600, 6, "TIME", "nw", 11)
        self._label(600, 22, "t 0.00 s", "nw", 11, tags="hud_t")

    def _hud_set(self, x, y, t):
        c = self.canvas
        c.itemconfigure("hud_x", text=f"x {x:.2f} m")
        c.itemconfigure("hud_y", text=f"y {y:.2f} m")
        c.itemconfigure("hud_t", text=f"t {t:.2f} s")

    def draw_scene(self, res=None):
        c = self.canvas
        c.delete("all")
        case = self.case.get()
        yg = self.CH - self.GROUND_H
        x0 = self.LEFT
        self.geo = {"scale": 1.0}
        self._scenery(yg)
        self._bricks(0, yg, self.CW, self.CH)
        feet = yg                                       # surface Mario stands on
        if res is not None:
            sc = self._fit_scale(res)
            self.geo = {"scale": sc}
            feet = yg - res["y0"] * sc
            self._ruler(sc, yg)
            if case == "H2G":
                self._bricks(x0 - 100, feet, x0, yg)
            elif case == "G2H":
                self._target_platform(res, sc, yg)
        else:                                           # a preview of the chosen world
            if case == "H2G":
                feet = yg - 120
                self._bricks(x0 - 100, feet, x0, yg)
            elif case == "G2H":
                self._bricks(x0 + 330, yg - 80, x0 + 450, yg)
            self._label(self.CW / 2, 190, "Pick a world, type what you know,",
                        size=14, tags="intro")
            self._label(self.CW / 2, 214, "then press Fire!", size=14, tags="intro")
        self._sprite(MARIO, MARIO_COLORS, x0 - 8 - 12 * self.MARIO_PX,
                     feet - 16 * self.MARIO_PX, self.MARIO_PX)
        if res is not None:
            self._path(res)
            tip = (x0 + 46 * math.cos(res["th"]), feet - 46 * math.sin(res["th"]))
            c.create_line(x0, feet, *tip, fill=BLACK, width=6, arrow="last")
            c.create_line(x0, feet, *tip, fill=WHITE, width=3, arrow="last")
        self._hud()


def main():
    root = tk.Tk()
    SuperProjectileApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()