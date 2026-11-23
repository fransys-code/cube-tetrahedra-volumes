# Cutting a cube into tetrahedra of nearly equal volume

By Mead's theorem (1979) the unit cube can be cut into m tetrahedra of equal volume only if m is a
multiple of 6. For the other values of m, how close can one get? Let **Δ₃(m)** be the smallest
possible difference between the largest and the smallest volume (the *range*) in a dissection of
the unit cube into m tetrahedra. Dissections are general: the vertices of the tetrahedra are
arbitrary points of the cube, and the dissection need not be face-to-face (a vertex of one
tetrahedron may lie inside an edge or a face of another). This is the three-dimensional analogue
of the *quantitative Monsky problem* for the square cut into an odd number of triangles.

| m | Δ₃(m) | status |
|---|---|---|
| 5 | **= 1/6** | proved; the 5-piece dissection is unique up to symmetry |
| 6 | 0 | classical |
| 7 | **= 1/18** ≈ 0.0556 | proved; two different dissections attain it |
| 8 | 1/21 ≤ Δ₃ ≤ 1/12 | lower bound proved, upper bound by an explicit dissection |
| 9 | 1/32 ≤ Δ₃ ≤ 1/12 | idem |
| 10 | 1/54 ≤ Δ₃ ≤ 1/12 | idem |
| 11 | 1/120 ≤ Δ₃ ≤ 1/36 | idem |
| 12 | 0 | classical |
| 13 | ≤ 1/60 | explicit dissection |
| 14 | ≤ 0.0196723315 | explicit dissection |
| 15 | ≤ 0.0075141620 | explicit dissection; ≈ (5√5 − 11)/24 = Δ₂(5)/3 |

The lower bounds for m = 8 to 11 come from a theorem: **every dissection of the cube into 8, 9, 10
or 11 tetrahedra contains a tetrahedron of volume at most 1/12** (although the average volume 1/m
is larger). We conjecture that every dissection into at most 10 tetrahedra contains a tetrahedron
of volume at least 1/6; this would give Δ₃(8) = Δ₃(9) = Δ₃(10) = 1/12. More generally
Δ₃(3n) ≤ Δ₂(n)/3 (prisms over a dissection of the square into n triangles).

The proofs are in [PROOFS.md](PROOFS.md); they are elementary (areas, volumes, a covering lemma
for the faces, a case analysis) and use a few finite enumerations done by `verify.py`.

> **Status.** The proofs were written with the help of an AI assistant and checked line by line by a
> second, independent AI agent, which also re-verified every dissection with a program of its own.
> **No human referee has read them**, and the case analysis for m = 8 to 11 is long: an error is
> possible. The dissections themselves are verified exactly, so the upper bounds do not depend on
> the proofs. Novelty is not confirmed by experts. A web search on 23 November 2026 (search engine,
> arXiv, MathWorld's "Quantitative Monsky Problem", Wikipedia's "Equidissection") found no published
> value of Δ₃(m) and no statement of this question in dimension 3. For m = 5, it is classical that
> the cube has a single dissection into 5 tetrahedra *whose vertices are corners of the cube*
> (Crum Brown, 1893–94; we read a summary, not the scanned text), and the literature on minimal dissections of the cube (Hughes and Anderson
> 1996; Below, Brehm, De Loera, Richter-Gebert 2000; De Loera, Santos, Takeuchi 2000) works in that
> setting; we found no statement for arbitrary vertices, though it may well be folklore. We could
> not read the full text of the 1996 and 2000 papers (only abstracts and companion papers).
> Corrections and pointers to prior work are welcome: please open an issue.

*Résumé en français : on découpe le cube unité en m tétraèdres (sommets libres, contacts face à
face non exigés) et on cherche le plus petit écart possible Δ₃(m) entre le plus grand et le plus
petit volume. Nous démontrons Δ₃(5) = 1/6 (le découpage en 5 tétraèdres est unique à symétrie
près) et Δ₃(7) = 1/18 ; pour m = 8, 9, 10, 11, tout découpage contient un tétraèdre de volume au
plus 1/12, d'où les minorants 1/21, 1/32, 1/54, 1/120, à comparer aux meilleurs découpages trouvés
(1/12, 1/12, 1/12, 1/36) ; majorants pour m = 13, 14, 15. Les découpages sont vérifiés en
arithmétique exacte par un programme autonome. Les preuves ont été rédigées avec l'aide d'une IA
et relues par un second agent indépendant, mais par aucun mathématicien ; nouveauté non
confirmée par des spécialistes.*

Figures (French / English): https://totocaedres.fransys.io/pistes/monsky-cube/notre-travail

## Files

- `PROOFS.md` — the proofs of the three theorems and of the bounds.
- `data/m05.json`, `m07_I.json`, `m07_II.json`, `m08.json` … `m11.json`, `m13.json`, `m14.json`,
  `m15.json` — the dissections. Fields:
  - `vertices` — exact rational coordinates (strings `"p/q"`);
  - `tetrahedra` — quadruples of vertex indices;
  - `volumes` — the exact volume of each tetrahedron, in the same order;
  - `range` — largest volume minus smallest;
  - `m`, `status`, `statement`, `note` — description.
- `verify.py` — standalone verifier (Python 3 standard library only).

The extremal dissections, with O = (0,0,0), A = (1,1,0), B = (1,0,1), D = (0,1,1), E = (1,1,1):

- m = 5: the corner tetrahedra at (1,0,0), (0,1,0), (0,0,1), (1,1,1), of volume 1/6, and the
  regular tetrahedron OABD, of volume 1/3.
- m = 7, I: the same four corners, and OABD cut into three tetrahedra of volume 1/9 from the
  centroid (2/3, 2/3, 2/3) of its face ABD.
- m = 7, II: the corner tetrahedra at (1,0,0), (0,1,0), (0,0,1), then ABEw (1/6), OABw, ADEw, BDEw
  (1/9 each) with w = (0, 1/3, 1/3).
- m = 8: the four corners (1/6), and OABD cut into four tetrahedra of volume 1/12 from its centre.

## Verification

```bash
python3 verify.py
```

`verify.py` knows nothing about how the dissections were found. For each file it checks, in exact
rational arithmetic: every vertex is in the closed unit cube; every tetrahedron has positive
volume, equal to the listed one; the interiors are pairwise disjoint (two independent tests that
must agree: separating axes, and explicit computation of the intersection polytope); the volumes
sum to exactly 1 — so the tetrahedra tile the cube; the range equals the stated value. It then
runs the finite enumerations quoted in `PROOFS.md`.

Output obtained (about 5 seconds):

```
m05.json     m =  5  valid dissection of the unit cube  range = 1/6
             volumes: 1/6 x 4  1/3 x 1
m07_I.json   m =  7  valid dissection of the unit cube  range = 1/18
             volumes: 1/9 x 3  1/6 x 4
m07_II.json  m =  7  valid dissection of the unit cube  range = 1/18
             volumes: 1/9 x 3  1/6 x 4
m08.json     m =  8  valid dissection of the unit cube  range = 1/12
             volumes: 1/12 x 4  1/6 x 4
m09.json     m =  9  valid dissection of the unit cube  range = 1/12
             volumes: 1/12 x 4  1/9 x 3  1/6 x 2
m10.json     m = 10  valid dissection of the unit cube  range = 1/12
             volumes: 1/12 x 8  1/6 x 2
m11.json     m = 11  valid dissection of the unit cube  range = 1/36
             volumes: 1/12 x 8  1/9 x 3
m13.json     m = 13  valid dissection of the unit cube  range = 1/60
             volumes: 1/15 x 5  1/12 x 8
m14.json     m = 14  valid dissection of the unit cube  range = 0.0196723314583... (exact rational in the file)
             volumes between 0.0636610018750... and 0.0833333333333...
m15.json     m = 15  valid dissection of the unit cube  range = 0.0075141619791... (exact rational in the file)
             volumes between 0.0636610018750... and 0.0711751638541...
lemma 1: corner-vertex tetrahedra have volume 0, 1/6 or 1/3; 1/6 if they have a face on the boundary
lemma 6: corner tetrahedra overlap iff their corners are adjacent; 3 or 4 pairwise non-adjacent corners have the same parity
lemma 8: the plane of D_c contains no other corner; half-squares of two corner tetrahedra are distinct
counting: the cases (n3, n2, n1, n0) of theorems 2 and 3 and the lower bounds (12 - m)/(12 (m - 1))
formulas: volumes and planes of the case analysis, checked at sample rational parameters
ALL CHECKS PASSED (10 dissection(s))
```

The verifier rejects deliberately corrupted data (a moved vertex, a changed volume, a duplicated
tetrahedron).

## How it was found

The search programs are not published here; nothing above depends on them. In outline: the
conjectured values came from a numerical search (random families of dissections with free vertices,
including non face-to-face ones, optimised for the range) and from exhaustive enumerations of the
dissections with vertices on the grids {0, 1/k, …, 1}³. These enumerations are evidence, not
proofs. They found no dissection beating the records on the grid k = 2 (m = 8 to 11) and k = 3
(m = 8, 9, 11), none with range < 1/18 on the grid k = 4 for m = 7, and none with all volumes
> 1/12 for m = 8 to 11 on the grids k = 2, 3, 4, in agreement with the theorems. The proofs were
then written by hand.

## References

- D. G. Mead, Dissection of the hypercube into simplexes, Proc. Amer. Math. Soc. 76 (1979) 302–304.
- P. Monsky, On dividing a square into triangles, Amer. Math. Monthly 77 (1970) 161–164.
- A. Crum Brown, On the division of a parallelepiped into tetrahedra without making new corners,
  Proc. Edinburgh Math. Soc. 12 (1893–94) 106–107.
- R. B. Hughes, M. R. Anderson, Simplexity of the cube, Discrete Math. 158 (1996) 99–150.
- A. Below, U. Brehm, J. A. De Loera, J. Richter-Gebert, Minimal simplicial dissections and
  triangulations of convex 3-polytopes, Discrete Comput. Geom. 24 (2000) 35–48.
- J. A. De Loera, F. Santos, F. Takeuchi, Extremal properties for dissections of convex 3-polytopes,
  [arXiv:math/0012169](https://arxiv.org/abs/math/0012169).
- J.-P. Labbé, G. Rote, G. M. Ziegler, Area difference bounds for dissections of a square into an odd
  number of triangles, Experimental Mathematics (2018), [arXiv:1708.02891](https://arxiv.org/abs/1708.02891).
- M. Li, [arXiv:2609.22693](https://arxiv.org/abs/2609.22693) (September 2026): Δ₂(5) = (5√5 − 11)/8
  for the square (preprint).

## Acknowledgements

The proofs, the search and the verification code were written with the help of Claude (Anthropic).

## Licence

Code: MIT (`LICENSE`). Data in `data/`: CC BY 4.0 (`LICENSE-DATA.md`).
