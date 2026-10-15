<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Super Projectile Bros. - Fireball Physics</title>
<style>
  /* HTML version of mario_projectile.py. The Python file is unchanged; this is the same
     game with the same physics, messages, colours and drawing, written for a browser. */
  html, body { margin: 0; background: #D82800; }
  body { font: bold 10pt "Courier New", Courier, monospace; color: #fff; }
  #app { display: grid; grid-template-columns: auto 800px; align-items: start; width: max-content; }

  /* ---------- left panel (the red column) ---------- */
  #left { background: #D82800; padding: 10px 14px; align-self: stretch; }
  .title { font-size: 16pt; color: #FCC800; }
  .small { font-size: 9pt; }
  .yellow { color: #FCC800; }
  .sub { margin: 0 0 8px; }
  .h2 { margin: 12px 0 2px; }
  .radio { display: flex; align-items: center; height: 21px; cursor: pointer; white-space: pre; }
  .radio:hover { color: #FCC800; }
  .radio input { appearance: none; -webkit-appearance: none; flex: none; margin: 0 6px 0 0;
                 width: 13px; height: 13px; border: 2px solid #000; border-radius: 50%;
                 background: #fff; display: grid; place-content: center; }
  .radio input:checked { background: #FCC800; }
  .radio input:checked::before { content: ""; width: 5px; height: 5px; border-radius: 50%; background: #000; }
  .grid { display: grid; grid-template-columns: 19ch auto 12ch; align-items: center; }
  .grid > * { margin: 3px 0; }
  .grid label { white-space: pre; }
  .grid > .e { margin: 3px 6px; }
  .e { box-sizing: content-box; width: 9ch; height: 19px; padding: 0 2px; border: 3px inset #8a8a8a;
       background: #fff; color: #000; text-align: right; font: inherit; }
  .e:disabled { background: #C8C8C8; color: #303030; }
  .unit { color: #FCC800; white-space: pre; }
  .hint { margin-top: 8px; white-space: nowrap; }
  .buttons { display: flex; gap: 8px; margin: 10px 0 8px; }
  button { box-sizing: content-box; padding: 4px 11px; border: 4px outset #FCC800; background: #FCC800;
           color: #000; font: bold 13pt "Courier New", Courier, monospace; cursor: pointer; }
  button:hover { background: #FFE266; }
  button:active { border-style: inset; }
  #fire { width: 9ch; }
  #clear { width: 7ch; }
  #message { box-sizing: content-box; width: 40ch; height: 126px; padding: 4px 6px; background: #000;
             color: #fff; font-size: 9pt; line-height: 14px; white-space: pre-wrap; overflow: hidden; }

  /* ---------- right: the picture and the results ---------- */
  #right { background: #000; width: 800px; }
  #scene { display: block; width: 800px; height: 450px; }
  #texts { display: flex; }
  .txt { box-sizing: content-box; height: 120px; padding: 8px 10px; background: #000; overflow: hidden;
         white-space: pre; font-size: 10pt; line-height: 15px; }
  #txt_vars { width: 44ch; }
  #txt_more { width: 50ch; }
  .head { color: #A8A8A8; }
  .you { color: #FFFFFF; }
  .solved { color: #FCC800; }
  .more { color: #9CFC9C; }
</style>
</head>
<body>
<noscript>This game needs JavaScript turned on.</noscript>
<div id="app">
  <div id="left">
    <div class="title">SUPER PROJECTILE<br>BROS.</div>
    <div class="small sub">Fireball physics lab</div>

    <div class="small yellow">Choose a world</div>
    <label class="radio"><input type="radio" name="case" value="G2G" checked autocomplete="off"><span>1-1  Ground → Ground</span></label>
    <label class="radio"><input type="radio" name="case" value="H2G" autocomplete="off"><span>1-2  Height → Ground</span></label>
    <label class="radio"><input type="radio" name="case" value="G2H" autocomplete="off"><span>1-3  Ground → Height</span></label>

    <div class="small yellow h2">What do you know?</div>
    <div class="grid">
      <label for="e-v">v  Final velocity</label>
      <input class="e" id="e-v" type="text" autocomplete="off" spellcheck="false" autocapitalize="off">
      <span class="unit">m/s</span>

      <label for="e-u">u  Initial velocity</label>
      <input class="e" id="e-u" type="text" autocomplete="off" spellcheck="false" autocapitalize="off">
      <span class="unit">m/s</span>

      <label for="e-a">a  Acceleration</label>
      <input class="e" id="e-a" type="text" autocomplete="off" spellcheck="false" autocapitalize="off">
      <span class="unit">m/s²</span>

      <label for="e-s">s  Displacement</label>
      <input class="e" id="e-s" type="text" autocomplete="off" spellcheck="false" autocapitalize="off">
      <span class="unit" id="s-unit">m</span>

      <label for="e-t">t  Time</label>
      <input class="e" id="e-t" type="text" autocomplete="off" spellcheck="false" autocapitalize="off">
      <span class="unit">s</span>

      <label for="e-th">θ  Theta</label>
      <input class="e" id="e-th" type="text" autocomplete="off" spellcheck="false" autocapitalize="off">
      <span class="unit">°</span>
    </div>

    <div class="small hint">Type 3 or more values and leave the rest blank.<br>Type heights as positive numbers.<br>Acceleration starts as Earth's gravity;<br>clear it if you want to solve for it.</div>

    <div class="buttons">
      <button type="button" id="fire">Fire!</button>
      <button type="button" id="clear">Clear</button>
    </div>

    <div id="message" aria-live="polite"></div>
  </div>

  <div id="right">
    <canvas id="scene" width="800" height="450" role="img" aria-label="Mario shooting a fireball"></canvas>
    <div id="texts">
      <div class="txt" id="txt_vars"></div>
      <div class="txt" id="txt_more"></div>
    </div>
  </div>
</div>

<script>
"use strict";

/* ======================================================================
   1.  THE PHYSICS      (same rules, same tolerances, same messages as the Python)
   ======================================================================
   Horizontal speed never changes; vertical motion has constant acceleration a:

     (E1)  s   = u*sin(th)*t + 0.5*a*t^2
     (E2)  v^2 = (u*cos(th))^2 + (u*sin(th) + a*t)^2      -> same as  v^2 = u^2 + 2*a*s

   Only TWO equations link SIX variables, so you need FOUR known values in total.
   That works out because gravity is pre-filled (a = -9.81) and, in Ground -> Ground,
   s = 0 is known from the world itself.

   The solver below is a list of small "rules".  Each rule rearranges the equations
   to find ONE unknown from other known values.  It applies rules until nothing
   new can be found, then double-checks that every value fits both equations.
*/
const ALL = ["v", "u", "a", "s", "t", "th"];
const NAME = {v: "final velocity", u: "initial velocity", a: "acceleration",
              s: "displacement", t: "time", th: "theta"};
const SYMBOL = {v: "v", u: "u", a: "a", s: "s", t: "t", th: "θ"};
const UNIT = {v: "m/s", u: "m/s", a: "m/s²", s: "m", t: "s", th: "°"};
const DEFAULT_G = 9.81;

class SolveError extends Error {}      // a friendly message for the person at the keyboard
class PyArithError extends Error {}    // stands in for Python's OverflowError / ZeroDivisionError / ValueError

// --- small helpers so the maths behaves exactly like the Python version -----
const radians = (x) => x * (Math.PI / 180);
const degrees = (x) => x * (180 / Math.PI);
const pyMax = (a, b) => (b > a ? b : a);               // Python's max(a, b)
const pyMin = (a, b) => (b < a ? b : a);               // Python's min(a, b)
const div = (x, y) => { if (y === 0) throw new PyArithError(); return x / y; };
const sq = (x) => { const r = x * x; if (!Number.isFinite(r) && Number.isFinite(x)) throw new PyArithError(); return r; };
const sqrt = (x) => { if (x < 0) throw new PyArithError(); return Math.sqrt(x); };
const asin = (x) => { if (x > 1 || x < -1) throw new PyArithError(); return Math.asin(x); };
const hypot = (x, y) => { const r = Math.hypot(x, y); if (!Number.isFinite(r) && Number.isFinite(x) && Number.isFinite(y)) throw new PyArithError(); return r; };
const f2 = (x) => (Object.is(x, -0) ? "-" : "") + x.toFixed(2);   // Python's f"{x:.2f}"

function fmtExp(x, digits) {                           // Python's f"{x:.3e}"
  const m = x.toExponential(digits).match(/^(-?[\d.]+)e([+-])(\d+)$/);
  return m[1] + "e" + m[2] + m[3].padStart(2, "0");
}

function fmtG(x) {                                     // Python's f"{x:g}"
  if (x === 0) return "0";
  const parts = x.toExponential(5).split("e");
  const exp = parseInt(parts[1], 10);
  if (exp < -4 || exp >= 6) {
    let mant = parts[0];
    if (mant.includes(".")) mant = mant.replace(/0+$/, "").replace(/\.$/, "");
    return mant + "e" + (exp < 0 ? "-" : "+") + String(Math.abs(exp)).padStart(2, "0");
  }
  let s = x.toFixed(5 - exp);
  if (s.includes(".")) s = s.replace(/0+$/, "").replace(/\.$/, "");
  return s;
}

function pyFloat(text) {                               // Python's float(text); null if it isn't a number
  if (/^[+-]?(?:inf|infinity|nan)$/i.test(text)) return text.includes("-") ? -Infinity : Infinity;
  const digits = "\\d(?:_?\\d)*";
  const re = new RegExp("^[+-]?(?:" + digits + "(?:\\.(?:" + digits + ")?)?|\\." + digits + ")(?:[eE][+-]?" + digits + ")?$");
  return re.test(text) ? parseFloat(text.replace(/_/g, "")) : null;
}

function _roots_to_u(base, r) {                        // both answers of a quadratic for u, keeping speeds >= 0
  const out = [];
  for (let x of [base + r, base - r]) {
    if (x >= -1e-9) {
      x = pyMax(x, 0.0);
      if (out.every((y) => Math.abs(x - y) > 1e-9)) out.push(x);
    }
  }
  return out;
}

function _safe_sqrt(d, ref, tol = 0.005) {             // sqrt(d), forgiving a tiny negative d from rounded inputs
  if (d < -tol * ref - 1e-9) return null;
  return sqrt(pyMax(d, 0.0));
}

// A rule returns:  null -> can't use it right now (it would divide by zero)
//                  []   -> the numbers are impossible
//                  [x]  -> the answer (or [x, y] when two answers are possible)

function _t_land(k) {                                  // landing time = the LATER time the fireball is at height s
  const uy = k.u * Math.sin(k.th);
  const root = _safe_sqrt(uy * uy + 2 * k.a * k.s, uy * uy + Math.abs(2 * k.a * k.s));
  if (root === null) return [];
  const t = div(-uy - root, k.a);
  return t > 1e-9 ? [t] : [];
}

function _s_from_t(k) {
  return [k.u * Math.sin(k.th) * k.t + 0.5 * k.a * sq(k.t)];
}

function _v_from_s(k) {
  const root = _safe_sqrt(sq(k.u) + 2 * k.a * k.s, sq(k.u) + Math.abs(2 * k.a * k.s));
  return root === null ? [] : [root];
}

function _u_from_v(k) {
  const root = _safe_sqrt(sq(k.v) - 2 * k.a * k.s, sq(k.v) + Math.abs(2 * k.a * k.s));
  return root === null ? [] : [root];
}

function _s_from_v(k) {
  return [div(sq(k.v) - sq(k.u), 2 * k.a)];
}

function _th_from_t(k) {
  if (k.u < 1e-9) return null;
  const x = div(k.s - 0.5 * k.a * sq(k.t), k.u * k.t);
  if (Math.abs(x) > 1.01) return [];                   // a little slack for rounded inputs (e.g. a straight-up shot)
  return [asin(pyMax(-1.0, pyMin(1.0, x)))];
}

function _u_from_t(k) {
  const sn = Math.sin(k.th);
  if (Math.abs(sn) < 1e-9) return null;                // a flat shot: time says nothing about the speed
  const u = div(k.s - 0.5 * k.a * sq(k.t), sn * k.t);
  return u < -1e-9 ? [] : [pyMax(u, 0.0)];
}

function _a_from_t(k) {
  const a = div(2 * (k.s - k.u * Math.sin(k.th) * k.t), sq(k.t));
  return a < -1e-9 ? [a] : [];
}

function _a_from_v(k) {
  if (Math.abs(k.s) < 1e-9) return null;
  const a = div(sq(k.v) - sq(k.u), 2 * k.s);
  return a < -1e-9 ? [a] : [];
}

function _a_from_tv(k) {
  const ux = k.u * Math.cos(k.th);
  const uy = k.u * Math.sin(k.th);
  const root = _safe_sqrt(sq(k.v) - sq(ux), sq(k.v));
  if (root === null) return [];
  const a = div(-root - uy, k.t);                      // it lands while going DOWN
  return a < -1e-9 ? [a] : [];
}

function _u_quad(k) {                                  // u from theta, a, t, v  (a quadratic: up to two answers)
  const sn = Math.sin(k.th), cs = Math.cos(k.th);
  const root = _safe_sqrt(sq(k.v) - sq(k.a * k.t * cs), sq(k.v));
  if (root === null) return [];
  return _roots_to_u(-k.a * k.t * sn, root);
}

function _u_quad_no_a(k) {                             // u from theta, s, t, v when a is unknown (also a quadratic)
  const sn = Math.sin(k.th), cs = Math.cos(k.th);
  const root = _safe_sqrt(sq(k.v) - sq(div(2 * k.s * cs, k.t)), sq(k.v));
  if (root === null) return [];
  return _roots_to_u(div(2 * k.s * sn, k.t), root);
}

// (what it finds, what it needs, function, message if the numbers are impossible)
const RULES = [
  ["t", ["u", "th", "a", "s"], _t_land,
   "With these numbers the fireball never comes down to the landing height. " +
   "Try a faster launch or a steeper angle."],
  ["s", ["u", "th", "a", "t"], _s_from_t, ""],
  ["v", ["u", "a", "s"], _v_from_s,
   "The fireball runs out of speed before it reaches that height. " +
   "Try a faster launch or a smaller height."],
  ["u", ["v", "a", "s"], _u_from_v,
   "That final speed is too small for that displacement. Try a bigger final velocity."],
  ["s", ["u", "a", "v"], _s_from_v, ""],
  ["th", ["u", "a", "s", "t"], _th_from_t,
   "No launch angle fits those values (it would need sin θ above 1). " +
   "Check the speed, time and displacement."],
  ["u", ["th", "a", "s", "t"], _u_from_t,
   "Those values would need a negative launch speed. Check the sign of theta and the time."],
  ["a", ["u", "th", "s", "t"], _a_from_t,
   "Those values would need gravity to pull UP. Check the numbers (a should come out negative)."],
  ["a", ["u", "s", "v"], _a_from_v,
   "Those values would need gravity to pull UP. Check the numbers (a should come out negative)."],
  ["a", ["u", "th", "t", "v"], _a_from_tv,
   "Those values would need gravity to pull UP. Check the numbers (a should come out negative)."],
  ["u", ["th", "a", "t", "v"], _u_quad,
   "No launch speed fits that combination of theta, time and final velocity."],
  ["u", ["th", "s", "t", "v"], _u_quad_no_a,
   "No launch speed fits that combination of theta, displacement, time and final velocity."],
];

function _expand(known, problems) {                    // apply rules until nothing new can be found
  const k = {...known};
  if ("u" in k && !("th" in k) && k.u < 1e-9) k.th = 0.0;     // speed 0: the angle doesn't matter
  for (const [unknown, needs, func, why] of RULES) {
    if (unknown in k || needs.some((n) => !(n in k))) continue;
    const candidates = func(k);
    if (candidates === null) continue;
    if (candidates.length === 0) {
      problems.push(why);
      return [];
    }
    const out = [];
    for (const value of candidates) {
      const nxt = {...k};
      nxt[unknown] = value;
      out.push(..._expand(nxt, problems));
    }
    return out;
  }
  return [k];
}

function _solvable(names) {                            // would these variables be enough? (used for hints)
  names = new Set(names);
  let grew = true;
  while (grew) {
    grew = false;
    for (const [unknown, needs] of RULES) {
      if (!names.has(unknown) && needs.every((n) => names.has(n))) {
        names.add(unknown);
        grew = true;
      }
    }
  }
  return ALL.every((n) => names.has(n));
}

function _close(x, y, scale) {
  return Math.abs(x - y) <= 0.02 * scale + 1e-9;
}

function _validate(st, case_) {                        // check a complete set of six values: null if fine, else a message
  const {u, th, a, s, t, v} = st;
  const ux = u * Math.cos(th), uy = u * Math.sin(th);
  const s_calc = uy * t + 0.5 * a * t * t;
  const vy = uy + a * t;
  const v_calc = hypot(ux, vy);
  const fit = `These numbers don't fit together: with u = ${f2(u)} m/s, θ = ${f2(degrees(th))}°, ` +
              `a = ${f2(a)} m/s² and t = ${f2(t)} s`;
  if (!_close(s, s_calc, Math.max(Math.abs(uy * t), Math.abs(0.5 * a * t * t), Math.abs(s), 1.0))) {
    return `${fit}, the displacement would be ${f2(s_calc)} m, not ${f2(s)} m.`;
  }
  if (!_close(v, v_calc, Math.max(v, v_calc, 1.0))) {
    return `${fit}, the final velocity would be ${f2(v_calc)} m/s, not ${f2(v)} m/s.`;
  }
  if (vy > 0.02 * Math.max(Math.abs(uy), Math.abs(a * t), 1.0)) {
    return `At t = ${f2(t)} s the fireball is still going up (${f2(vy)} m/s), so it hasn't ` +
           "landed yet. It can only land while coming down - try a larger time.";
  }
  if (case_ === "H2G" && s > -1e-9) {
    return "Height → Ground needs the fireball to land lower than it started, but these " +
           `numbers give s = ${f2(s)} m. Try world 1-1 or 1-3 instead.`;
  }
  if (case_ === "G2H" && s < 1e-9) {
    return "Ground → Height needs the fireball to land higher than it started, but these " +
           `numbers give s = ${f2(s)} m. Try world 1-1 or 1-2 instead.`;
  }
  if (case_ === "G2H" && ux < 1e-6 * Math.max(u, 1.0)) {
    return "A straight-up shot (θ = 90°) can't land on a platform - it would hit the " +
           "underside. Use a smaller angle.";
  }
  return null;
}

/*  case_ : "G2G", "H2G" or "G2H"
    typed : object with any of v, u, a, s, t, th  (th in degrees)
    Returns an object with all six values plus extras, or throws SolveError.  */
function solve(case_, typed) {
  try {
    return _solve(case_, typed);
  } catch (err) {
    if (err instanceof PyArithError) {
      throw new SolveError("Those numbers are too extreme to calculate. Try smaller ones.");
    }
    throw err;
  }
}

function _solve(case_, typed) {
  const k = {...typed};
  const notes = [];

  // --- tidy up what was typed ---------------------------------------
  for (const n of ["u", "v"]) {
    if (n in k && k[n] < 0) throw new SolveError(`The ${NAME[n]} is a speed, so it can't be negative.`);
  }
  if ("t" in k && k.t <= 0) throw new SolveError("Time must be bigger than 0.");
  if ("th" in k) {
    if (!(-90.0 <= k.th && k.th <= 90.0)) {
      throw new SolveError("Theta must be between -90° and 90° (measured up from the horizontal).");
    }
    k.th = radians(k.th);
  }
  if ("a" in k) {
    if (k.a === 0) throw new SolveError("Acceleration can't be 0 - with no gravity the fireball never lands.");
    if (k.a > 0) notes.push(`Gravity pulls down, so I used a = -${fmtG(k.a)} m/s².`);
    k.a = -Math.abs(k.a);
  }
  if (case_ === "G2G") {
    k.s = 0.0;                                         // same height at start and end
  } else if ("s" in k) {
    if (k.s === 0) {
      throw new SolveError("Displacement can't be 0 in this world. Type the height difference " +
                           "as a positive number.");
    }
    k.s = case_ === "H2G" ? -Math.abs(k.s) : Math.abs(k.s);
  }

  // --- solve ---------------------------------------------------------
  const problems = [];
  const finals = _expand(k, problems);
  const complete = finals.filter((st) => ALL.every((n) => n in st));
  if (complete.length === 0) {
    if (problems.length) throw new SolveError(problems[0]);
    const stuck = ALL.filter((n) => !(n in finals[0])).map((n) => NAME[n]);
    const hints = ALL.filter((n) => !(n in k) && _solvable(new Set([...Object.keys(k), n])))
                     .map((n) => `${NAME[n]} (${SYMBOL[n]})`);
    if (hints.length) {
      throw new SolveError(`I can't work out the ${stuck.join(", ")} yet. Type one more ` +
                           `value, for example: ${hints.join(", ")}.`);
    }
    throw new SolveError("I need more values to solve this. Type at least three of the boxes.");
  }

  const good = [], why_not = [];
  for (const st of complete) {
    const why = _validate(st, case_);
    if (why === null) good.push(st); else why_not.push(why);
  }
  if (good.length === 0) {
    let msg = why_not[0];
    if ("a" in typed && msg.startsWith("These numbers don't fit")) {
      msg += " (Clear the acceleration box if you want me to solve for it.)";
    }
    throw new SolveError(msg);
  }

  const unique = [];
  for (const st of good) {
    if (unique.every((o) => ALL.some((n) => Math.abs(st[n] - o[n]) > 1e-6 * Math.max(1.0, Math.abs(o[n]))))) {
      unique.push(st);
    }
  }
  const st = unique[0];
  const alternatives = unique.slice(1);

  // --- extras for the picture ------------------------------------------
  const {u, th, a, s, t, v} = st;
  const ux = u * Math.cos(th), uy = u * Math.sin(th);
  const land = _t_land(st);
  const t_land = land.length ? land[0] : t;            // exact landing time for the animation
  const d = uy * uy + 2 * a * s;
  const t_first = div(-uy + sqrt(pyMax(d, 0.0)), a);   // first time at height s (going up)
  const vy_end = uy + a * t_land;
  const g = -a;
  const rise = uy > 0 ? div(uy * uy, 2 * g) : 0.0;
  const y0 = s < 0 ? -s : 0.0;                         // launch height above the floor

  if ("t" in typed && Math.abs(t - t_land) > 0.01 * t_land) {
    notes.push(`Your time (${f2(t)} s) is a little off what the other values give ` +
               `(${f2(t_land)} s). I animated the exact path.`);
  }
  if (alternatives.length) {
    const diffs = [];
    for (const n of ALL) {
      if (Math.abs(alternatives[0][n] - st[n]) > 1e-6 * Math.max(1.0, Math.abs(st[n]))) {
        const val = n === "th" ? degrees(alternatives[0][n]) : alternatives[0][n];
        diffs.push(`${SYMBOL[n]} = ${f2(val)} ${UNIT[n]}`);
      }
    }
    notes.push("Two answers fit these numbers. Another one is " + diffs.join(", ") +
               ". I'm showing the first.");
  }

  const res = {};
  for (const n of ALL) res[n] = st[n];
  Object.assign(res, {
    th_deg: degrees(th), ux, uy, vy_end, R: ux * t_land, y0,
    rise, t_peak: (uy > 0 ? div(uy, g) : 0.0), peak_y: y0 + rise,
    impact: pyMax(0.0, degrees(Math.atan2(-vy_end, ux))),
    t_land, t_first, given: new Set(Object.keys(typed)), notes,
    alternatives: alternatives.map((o) => Object.fromEntries(ALL.map((n) => [n, o[n]]))),
  });
  const sizes = [res.R, res.t_land, res.peak_y, res.u, res.v];
  if (!sizes.every(Number.isFinite) || Math.max(...sizes) > 1e9) {
    throw new SolveError("That flight is too big to draw. Try smaller numbers.");
  }
  return res;
}

/* ======================================================================
   2.  LOOK AND FEEL  (colours and pixel-art sprites drawn with code)
   ====================================================================== */
const SKY = "#5C94FC";
const RED = "#D82800";
const YELLOW = "#FCC800";
const BLACK = "#000000";
const WHITE = "#FFFFFF";
const BRICK = "#C84C0C";
const MORTAR = "#5A1E00";
const HILL = "#00A800";
const HILL_DARK = "#005800";
const GUIDE = "#9DBDFF";
const MONO = "'Courier New', Courier, monospace";

// One letter = one pixel.  "." is see-through.
const MARIO = [
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
];
const MARIO_COLORS = {R: "#E52521", S: "#FFB07C", K: "#6B3A0A",
                      B: "#2038EC", Y: "#FCD800", W: "#FFFFFF"};

const FIRE = [
  "..RR...",
  ".ROOR..",
  "ROYYOR.",
  "ROYWYOR",
  ".ROYYOR",
  "..ROOR.",
  "...RR..",
];
const FIRE_COLORS = {R: "#D82800", O: "#FC9838", Y: "#FCD800", W: "#FFFFFF"};

function _rotate(grid) {                               // turn a sprite 90 degrees (this is what makes the fireball spin)
  return Array.from({length: grid[0].length},
                    (_, i) => [...grid].reverse().map((row) => row[i]).join(""));
}

const FIRE_FRAMES = [FIRE];
for (let i = 0; i < 3; i++) FIRE_FRAMES.push(_rotate(FIRE_FRAMES[FIRE_FRAMES.length - 1]));

const WORLD = {G2G: "1-1", H2G: "1-2", G2H: "1-3"};
const FIELDS = [                                       // key, symbol, label, unit
  ["v", "v", "Final velocity", "m/s"],
  ["u", "u", "Initial velocity", "m/s"],
  ["a", "a", "Acceleration", "m/s²"],
  ["s", "s", "Displacement", "m"],
  ["t", "t", "Time", "s"],
  ["th", "θ", "Theta", "°"],
];

function nice_step(target) {                           // smallest 1, 2 or 5 times a power of ten that is >= target
  if (target <= 0) return 1.0;
  const exp = Math.floor(Math.log10(target));
  for (const m of [1, 2, 5, 10]) {
    if (m * Math.pow(10, exp) >= target) return m * Math.pow(10, exp);
  }
  return Math.pow(10, exp + 1);
}

function num(x) {
  if (x === 0) return "0.00";
  if (Math.abs(x) >= 1e6 || Math.abs(x) < 0.005) return fmtExp(x, 3);
  return f2(x);
}

/* ======================================================================
   3.  THE DRAWING AREA
   ======================================================================
   Python's tkinter Canvas keeps a list of drawn items (create_rectangle, delete,
   itemconfigure ...).  This small class does the same on an HTML canvas, so the
   drawing code below can stay almost line-for-line the same as the Python.   */
const CW = 800, CH = 450;                              // drawing area (pixels)
const GROUND_H = 64;                                   // thickness of the brick floor
const LEFT = 125, RIGHT = 75, TOP = 100;               // space kept free around the flight path
const MARIO_PX = 3;                                    // one Mario "pixel" = 3 screen pixels
const FIRE_PX = 4;

const ANCHORS = {center: ["center", "m"], nw: ["left", "n"], n: ["center", "n"], ne: ["right", "n"],
                 w: ["left", "m"], e: ["right", "m"], sw: ["left", "s"], s: ["center", "s"], se: ["right", "s"]};

function tkArrowLast(x1, y1, x2, y2, width) {          // the arrow head Tk draws for  arrow="last"
  const w = Math.max(width, 1);
  const shapeA = 8 + 0.001, shapeB = 10 + 0.001, shapeC = 3 + w / 2 + 0.001;
  const fracHeight = (w / 2) / shapeC;
  const backup = fracHeight * shapeB + shapeA * (1 - fracHeight) / 2;
  const dx = x2 - x1, dy = y2 - y1, len = Math.hypot(dx, dy);
  const sinT = len === 0 ? 0 : dy / len, cosT = len === 0 ? 0 : dx / len;
  const vertX = x2 - shapeA * cosT, vertY = y2 - shapeA * sinT;
  let temp = shapeC * sinT;
  const p2x = x2 - shapeB * cosT + temp, p8x = p2x - 2 * temp;
  temp = shapeC * cosT;
  const p3y = y2 - shapeB * sinT - temp, p9y = p3y + 2 * temp;
  const p4x = p2x * fracHeight + vertX * (1 - fracHeight), p4y = p3y * fracHeight + vertY * (1 - fracHeight);
  const p6x = p8x * fracHeight + vertX * (1 - fracHeight), p6y = p9y * fracHeight + vertY * (1 - fracHeight);
  return {poly: [[x2, y2], [p2x, p3y], [p4x, p4y], [p6x, p6y], [p8x, p9y]],
          end: [x2 - backup * cosT, y2 - backup * sinT]};
}

class TkCanvas {
  constructor(el) {
    this.el = el;
    this.ctx = el.getContext("2d");
    this.dpr = window.devicePixelRatio || 1;           // sharp on high-resolution screens
    el.width = Math.round(CW * this.dpr);
    el.height = Math.round(CH * this.dpr);
    this.items = [];
    this.queued = false;
    this.metrics = {};
  }

  create_rectangle(x1, y1, x2, y2, opts = {}) { return this._add("rect", [x1, y1, x2, y2], opts); }
  create_oval(x1, y1, x2, y2, opts = {}) { return this._add("oval", [x1, y1, x2, y2], opts); }
  create_line(coords, opts = {}) { return this._add("line", coords, opts); }
  create_text(x, y, opts = {}) { return this._add("text", [x, y], opts); }

  delete(tag) {
    this.items = tag === "all" ? [] : this.items.filter((it) => it.tags !== tag);
    this._queue();
  }

  itemconfigure(tag, opts) {
    for (const it of this.items) if (it.tags === tag) Object.assign(it.opts, opts);
    this._queue();
  }

  _add(kind, coords, opts) {
    this.items.push({kind, coords, opts: {...opts}, tags: opts.tags || ""});
    this._queue();
    return this.items.length;
  }

  _queue() {                                           // draw once per screen refresh, however many items changed
    if (this.queued) return;
    this.queued = true;
    requestAnimationFrame(() => { this.queued = false; this.render(); });
  }

  _font_metrics(font) {
    if (!this.metrics[font]) {
      this.ctx.font = font;
      const m = this.ctx.measureText("Mg");
      const px = parseFloat(font.match(/([\d.]+)pt/)[1]) * 4 / 3;
      this.metrics[font] = {ascent: m.fontBoundingBoxAscent ?? px * 0.83,
                            descent: m.fontBoundingBoxDescent ?? px * 0.3};
    }
    return this.metrics[font];
  }

  render() {
    const ctx = this.ctx;
    ctx.setTransform(this.dpr, 0, 0, this.dpr, 0, 0);
    ctx.setLineDash([]);
    ctx.fillStyle = SKY;
    ctx.fillRect(0, 0, CW, CH);
    for (const it of this.items) {
      const o = it.opts, c = it.coords;
      if (it.kind === "rect") {
        const x1 = Math.round(c[0]), y1 = Math.round(c[1]), x2 = Math.round(c[2]), y2 = Math.round(c[3]);
        if (o.fill) { ctx.fillStyle = o.fill; ctx.fillRect(x1, y1, x2 - x1, y2 - y1); }
        const outline = o.outline === undefined ? BLACK : o.outline;     // Tk's default outline is black
        if (outline) {
          const w = o.width === undefined ? 1 : o.width;
          const off = w % 2 === 1 ? 0.5 : 0;           // keeps thin outlines crisp
          ctx.lineWidth = w; ctx.strokeStyle = outline;
          ctx.strokeRect(x1 + off, y1 + off, x2 - x1, y2 - y1);
        }
      } else if (it.kind === "oval") {
        ctx.beginPath();
        ctx.ellipse((c[0] + c[2]) / 2, (c[1] + c[3]) / 2, Math.abs(c[2] - c[0]) / 2, Math.abs(c[3] - c[1]) / 2, 0, 0, Math.PI * 2);
        if (o.fill) { ctx.fillStyle = o.fill; ctx.fill(); }
        const outline = o.outline === undefined ? BLACK : o.outline;
        if (outline) { ctx.lineWidth = o.width === undefined ? 1 : o.width; ctx.strokeStyle = outline; ctx.stroke(); }
      } else if (it.kind === "line") {
        const pts = c.slice();
        const w = o.width === undefined ? 1 : o.width;
        let head = null;
        if (o.arrow === "last") {
          const n = pts.length;
          head = tkArrowLast(pts[n - 4], pts[n - 3], pts[n - 2], pts[n - 1], w);
          pts[n - 2] = head.end[0]; pts[n - 1] = head.end[1];
        }
        ctx.beginPath();
        ctx.moveTo(pts[0], pts[1]);
        for (let i = 2; i < pts.length; i += 2) ctx.lineTo(pts[i], pts[i + 1]);
        ctx.lineWidth = w; ctx.strokeStyle = o.fill || BLACK; ctx.setLineDash(o.dash || []);
        ctx.stroke();
        ctx.setLineDash([]);
        if (head) {
          ctx.fillStyle = o.fill || BLACK;
          ctx.beginPath();
          head.poly.forEach(([x, y], i) => (i ? ctx.lineTo(x, y) : ctx.moveTo(x, y)));
          ctx.closePath();
          ctx.fill();
        }
      } else if (it.kind === "text") {
        const [align, vert] = ANCHORS[o.anchor || "center"];
        const m = this._font_metrics(o.font);
        ctx.font = o.font; ctx.fillStyle = o.fill; ctx.textAlign = align; ctx.textBaseline = "alphabetic";
        const y = vert === "n" ? c[1] + m.ascent : vert === "s" ? c[1] - m.descent : c[1] + (m.ascent - m.descent) / 2;
        ctx.fillText(o.text, c[0], y);
      }
    }
  }
}

/* ======================================================================
   4.  THE APP
   ====================================================================== */
const now = () => performance.now() / 1000;           // seconds, like time.perf_counter()

class SuperProjectileApp {
  constructor() {
    this.job = null;                                   // the pending animation step, if any
    this.anim = null;
    this.geo = {scale: 1.0};
    this.canvas = new TkCanvas(document.getElementById("scene"));
    this.entries = {};
    for (const key of ALL) { this.entries[key] = document.getElementById("e-" + key); this.entries[key].value = ""; }
    this.entries.a.value = `-${DEFAULT_G}`;
    this.s_unit = document.getElementById("s-unit");
    this.message = document.getElementById("message");
    this.txt_vars = document.getElementById("txt_vars");
    this.txt_more = document.getElementById("txt_more");
    this.radios = [...document.querySelectorAll('input[name="case"]')];
    this.radios.forEach((r) => { r.checked = r.value === "G2G"; r.addEventListener("change", () => this.on_case_change()); });
    document.getElementById("fire").addEventListener("click", () => this.fire());
    document.getElementById("clear").addEventListener("click", () => this.reset());
    document.addEventListener("keydown", (e) => {      // the Enter key fires, wherever you are
      if (e.key === "Enter") { e.preventDefault(); this.fire(); }
    });
    this.on_case_change();
    this.entries.u.focus();
  }

  get_case() { return this.radios.find((r) => r.checked).value; }

  // ---------------------------------------------------------------- widgets
  _set_text(box, lines) {
    box.replaceChildren();
    for (const [text, tag] of lines) {
      const line = document.createElement("div");
      line.className = tag;
      line.textContent = text;
      box.appendChild(line);
    }
  }

  show_message(text, kind = "note") {
    const colour = {error: "#FF9C9C", ok: "#9CFC9C"}[kind] || "#FFE9A8";
    this.message.textContent = text;
    this.message.style.color = colour;
  }

  // ---------------------------------------------------------------- buttons
  on_case_change() {
    this.stop();
    const case_ = this.get_case();
    const entry = this.entries.s;
    if (case_ === "G2G") {
      entry.value = "0";
      entry.disabled = true;
      this.s_unit.textContent = "m (always 0)";
    } else {
      if (entry.value === "0") entry.value = "";
      entry.disabled = false;
      this.s_unit.textContent = case_ === "H2G" ? "m (drop)" : "m (climb)";
    }
    this.show_message("");
    this._set_text(this.txt_vars, [["  Your answers appear here after you press Fire!", "head"]]);
    this._set_text(this.txt_more, []);
    this.draw_scene();
  }

  reset() {
    this.stop();
    for (const key of ALL) this.entries[key].value = "";
    this.entries.a.value = `-${DEFAULT_G}`;
    this.on_case_change();
  }

  read_inputs() {
    const typed = {};
    for (const [key, , label] of FIELDS) {
      const raw = this.entries[key].value.trim().replaceAll(",", ".").replaceAll("\u2212", "-");
      if (!raw) continue;
      const value = pyFloat(raw);
      if (value === null) {
        throw new SolveError(`'${this.entries[key].value}' isn't a number. Fix the ${label} box.`);
      }
      if (!Number.isFinite(value) || Math.abs(value) > 1e7) {
        throw new SolveError(`The ${label} box needs an ordinary number (smaller than 10,000,000).`);
      }
      typed[key] = value;
    }
    return typed;
  }

  fire() {
    this.stop();
    let res;
    try {
      res = solve(this.get_case(), this.read_inputs());
    } catch (err) {
      if (err instanceof SolveError) {
        this.show_message(err.message, "error");
      } else {                                         // a bug, not the user's fault
        this.show_message(`Something unexpected went wrong: ${err.message}`, "error");
        console.error(err);
      }
      return;
    }
    if (res.notes.length) {
      this.show_message(res.notes.join("\n\n"), "note");
    } else {
      this.show_message("Fireball away!", "ok");
    }
    this.show_results(res);
    this.start_animation(res);
  }

  show_results(res) {
    const case_ = this.get_case();
    const lines = [["  Variable            Value        Source", "head"]];
    for (const [key, sym, label, unit] of FIELDS) {
      const value = key === "th" ? res.th_deg : res[key];
      let source, tag;
      if (key === "s" && case_ === "G2G") { source = "fixed"; tag = "you"; }
      else if (res.given.has(key)) { source = "you"; tag = "you"; }
      else { source = "solved"; tag = "solved"; }
      lines.push([` ${sym}  ${label.padEnd(16)}${num(value).padStart(9)} ${unit.padEnd(4)} ${source}`, tag]);
    }
    this._set_text(this.txt_vars, lines);

    const more = [[" Extra results", "head"],
      [` Horizontal range     R  = ${num(res.R)} m`, "more"],
      [` Launch height           = ${num(res.y0)} m`, "more"],
      [` Highest point (floor)   = ${num(res.peak_y)} m`, "more"],
      [` Time to highest point   = ${num(res.t_peak)} s`, "more"],
      [` Horizontal speed    vx = ${num(res.ux)} m/s (constant)`, "more"],
      [` Hits at ${num(res.impact)}° below the horizontal`, "more"]];
    this._set_text(this.txt_more, more);
  }

  // ------------------------------------------------------------ animation
  stop() {
    if (this.job !== null) {
      clearTimeout(this.job);
      this.job = null;
    }
  }

  start_animation(res) {
    this.draw_scene(res);
    const duration = Math.min(Math.max(res.t_land, 1.6), 6.5);   // real seconds on screen
    this.anim = {res, t0: now(), T: duration};
    this._frame();
  }

  _frame() {
    const a = this.anim;
    const res = a.res;
    const t_now = now();
    const frac = Math.min(1.0, (t_now - a.t0) / a.T);
    const ts = frac * res.t_land;                      // simulated seconds
    const x = res.ux * ts;
    const y = res.y0 + res.uy * ts + 0.5 * res.a * ts * ts;
    const [px, py] = this._to_px(x, y);
    this.canvas.delete("fb");
    this._sprite(FIRE_FRAMES[Math.floor((t_now - a.t0) * 14) % 4], FIRE_COLORS,
                 px - 3.5 * FIRE_PX, py - 3.5 * FIRE_PX, FIRE_PX, "fb");
    this._hud_set(x, y, ts);
    if (frac < 1.0) {
      this.job = setTimeout(() => this._frame(), 16);
    } else {
      this.canvas.delete("fb");
      this._boom(px, py, 0);
    }
  }

  _boom(px, py, step) {
    const c = this.canvas;
    c.delete("boom");
    if (step < 8) {
      const r = 5 + 4 * step;
      for (let k = 0; k < 7; k++) {                    // a burst thrown upwards
        const ang = k * Math.PI / 6;
        const cx = px + Math.cos(ang) * r, cy = py - Math.sin(ang) * r;
        c.create_rectangle(cx - 3, cy - 3, cx + 3, cy + 3,
                           {fill: k % 2 ? YELLOW : "#E52521", outline: "", tags: "boom"});
      }
      this.job = setTimeout(() => this._boom(px, py, step + 1), 35);
    } else {
      this.job = null;
      this._markers(this.anim.res);
    }
  }

  _markers(res) {
    const c = this.canvas;
    if (res.uy > 0 && res.rise > 0) {
      const [ax, ay] = this._to_px(res.ux * res.t_peak, res.peak_y);
      c.create_oval(ax - 4, ay - 4, ax + 4, ay + 4, {fill: YELLOW, outline: BLACK, width: 2});
      this._tag_point(ax, ay, `highest ${num(res.peak_y)} m`, 22);
    }
    const [lx, ly] = this._to_px(res.R, res.y0 + res.s);
    this._tag_point(lx, ly, `lands at x = ${num(res.R)} m`);
  }

  _tag_point(px, py, text, lift = 10) {                // write a label beside a dot, on whichever side stays inside the picture
    if (px + 8 + 7.4 * text.length <= CW - 4) {
      this._label(px + 8, py - lift, text, "sw");
    } else {
      this._label(px - 8, py - lift, text, "se");
    }
  }

  // -------------------------------------------------------------- drawing
  _to_px(x, y) {                                       // metres -> screen pixels (x to the right of Mario, y up from the floor)
    return [LEFT + x * this.geo.scale, CH - GROUND_H - y * this.geo.scale];
  }

  _label(x, y, text, anchor = "center", size = 9, colour = WHITE, tags = "") {
    const font = `bold ${size}pt ${MONO}`;
    this.canvas.create_text(x + 1, y + 1, {text, anchor, font, fill: BLACK, tags});
    return this.canvas.create_text(x, y, {text, anchor, font, fill: colour, tags});
  }

  _sprite(grid, palette, x, y, px, tag = "") {         // draw a pixel-art sprite, merging runs of the same colour
    const c = this.canvas;
    grid.forEach((row, r) => {
      let c0 = 0;
      while (c0 < row.length) {
        let c1 = c0;
        while (c1 + 1 < row.length && row[c1 + 1] === row[c0]) c1 += 1;
        if (row[c0] !== ".") {
          c.create_rectangle(x + c0 * px, y + r * px, x + (c1 + 1) * px, y + (r + 1) * px,
                             {fill: palette[row[c0]], outline: "", tags: tag});
        }
        c0 = c1 + 1;
      }
    });
  }

  _bricks(x1, y1, x2, y2) {
    const c = this.canvas;
    c.create_rectangle(x1, y1, x2, y2, {fill: BRICK, outline: BLACK, width: 2});
    let row = 0, y = y1;
    while (y < y2) {
      if (row) c.create_line([x1, y, x2, y], {fill: MORTAR, width: 2});
      let x = x1 + (row % 2 ? 16 : 32);
      while (x < x2) {
        c.create_line([x, y, x, Math.min(y + 16, y2)], {fill: MORTAR, width: 2});
        x += 32;
      }
      y += 16;
      row += 1;
    }
  }

  _scenery(yg) {
    const c = this.canvas;
    for (const [cx, w, h] of [[250, 220, 70], [560, 300, 110], [770, 170, 55]]) {
      c.create_oval(cx - w / 2, yg - h, cx + w / 2, yg + h, {fill: HILL, outline: HILL_DARK, width: 2});
    }
    for (const [cx, cy, s] of [[180, 120, 1.0], [450, 92, 1.3], [690, 130, 0.9]]) {
      for (const [dx, dy, r] of [[-28, 4, 16], [0, -6, 22], [30, 4, 17], [0, 6, 20]]) {
        c.create_oval(cx + (dx - r) * s, cy + (dy - r) * s, cx + (dx + r) * s, cy + (dy + r) * s,
                      {fill: WHITE, outline: ""});
      }
    }
  }

  _fit_scale(res) {
    const room_w = CW - LEFT - RIGHT;
    const room_h = CH - GROUND_H - TOP;
    let scale = 80.0;
    if (res.R > 1e-9) scale = Math.min(scale, room_w / res.R);
    if (res.peak_y > 1e-9) scale = Math.min(scale, room_h / res.peak_y);
    return scale;
  }

  _ruler(sc, yg) {
    const c = this.canvas;
    const step = nice_step(70.0 / sc);
    let k = 0;
    while (LEFT + k * step * sc <= CW - 20) {
      const x = LEFT + k * step * sc;
      c.create_line([x, yg, x, yg + 10], {fill: WHITE, width: 2});
      this._label(x, yg + 22, fmtG(k * step));
      k += 1;
    }
    this._label(CW - 8, yg + 46, "distance in m", "e");
    k = 1;
    while (yg - k * step * sc >= TOP - 30) {
      const y = yg - k * step * sc;
      c.create_line([LEFT, y, CW - 6, y], {fill: GUIDE, dash: [2, 6]});
      this._label(CW - 8, y - 8, `${fmtG(k * step)} m`, "e");
      k += 1;
    }
  }

  _target_platform(res, sc, yg) {
    /* A block the fireball lands on. Its left edge sits between the two times the
       path crosses the platform height, so the path never clips the side of the block. */
    const x_first = res.ux * pyMax(res.t_first, 0.0);
    const x_left = (x_first + res.R) / 2;
    const left = LEFT + x_left * sc;
    let right = LEFT + (2 * res.R - x_left) * sc;
    right = Math.min(Math.max(right, left + 64), CW - 4);
    this._bricks(left, yg - res.s * sc, right, yg);
  }

  _path(res) {                                         // yellow dots along the exact path
    const pts = [];
    let last = null;
    const n = 400;
    for (let i = 0; i <= n; i++) {
      const ts = res.t_land * i / n;
      const x = res.ux * ts;
      const y = res.y0 + res.uy * ts + 0.5 * res.a * ts * ts;
      pts.push(this._to_px(x, y));
    }
    pts.forEach(([px, py], i) => {
      if (last === null || Math.hypot(px - last[0], py - last[1]) >= 14 || i === n) {
        this.canvas.create_rectangle(px - 3, py - 3, px + 3, py + 3, {fill: YELLOW, outline: BLACK});
        last = [px, py];
      }
    });
  }

  _hud() {
    this._label(20, 6, "MARIO", "nw", 11);
    this._label(20, 22, "x 0.00 m", "nw", 11, WHITE, "hud_x");
    this._label(220, 6, "HEIGHT", "nw", 11);
    this._label(220, 22, "y 0.00 m", "nw", 11, WHITE, "hud_y");
    this._label(430, 6, "WORLD", "nw", 11);
    this._label(430, 22, WORLD[this.get_case()], "nw", 11);
    this._label(600, 6, "TIME", "nw", 11);
    this._label(600, 22, "t 0.00 s", "nw", 11, WHITE, "hud_t");
  }

  _hud_set(x, y, t) {
    const c = this.canvas;
    c.itemconfigure("hud_x", {text: `x ${f2(x)} m`});
    c.itemconfigure("hud_y", {text: `y ${f2(y)} m`});
    c.itemconfigure("hud_t", {text: `t ${f2(t)} s`});
  }

  draw_scene(res = null) {
    const c = this.canvas;
    c.delete("all");
    const case_ = this.get_case();
    const yg = CH - GROUND_H;
    const x0 = LEFT;
    this.geo = {scale: 1.0};
    this._scenery(yg);
    this._bricks(0, yg, CW, CH);
    let feet = yg;                                     // surface Mario stands on
    if (res !== null) {
      const sc = this._fit_scale(res);
      this.geo = {scale: sc};
      feet = yg - res.y0 * sc;
      this._ruler(sc, yg);
      if (case_ === "H2G") {
        this._bricks(x0 - 100, feet, x0, yg);
      } else if (case_ === "G2H") {
        this._target_platform(res, sc, yg);
      }
    } else {                                           // a preview of the chosen world
      if (case_ === "H2G") {
        feet = yg - 120;
        this._bricks(x0 - 100, feet, x0, yg);
      } else if (case_ === "G2H") {
        this._bricks(x0 + 330, yg - 80, x0 + 450, yg);
      }
      this._label(CW / 2, 190, "Pick a world, type what you know,", "center", 14, WHITE, "intro");
      this._label(CW / 2, 214, "then press Fire!", "center", 14, WHITE, "intro");
    }
    this._sprite(MARIO, MARIO_COLORS, x0 - 8 - 12 * MARIO_PX, feet - 16 * MARIO_PX, MARIO_PX);
    if (res !== null) {
      this._path(res);
      const tip = [x0 + 46 * Math.cos(res.th), feet - 46 * Math.sin(res.th)];
      c.create_line([x0, feet, ...tip], {fill: BLACK, width: 6, arrow: "last"});
      c.create_line([x0, feet, ...tip], {fill: WHITE, width: 3, arrow: "last"});
    }
    this._hud();
  }
}

const app = new SuperProjectileApp();
</script>
</body>
</html>
