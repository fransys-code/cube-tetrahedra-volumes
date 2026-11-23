#!/usr/bin/env python3
"""Standalone exact verifier for the dissections of the unit cube into tetrahedra in data/,
and for the finite checks quoted in PROOFS.md.

Python 3 standard library only; knows nothing about how the dissections were found.
All arithmetic is exact (fractions.Fraction).

Part 1, for each data file:
  - every vertex is in the closed unit cube;
  - every tetrahedron has positive volume, and the volumes are the ones listed;
  - the interiors are pairwise disjoint, by two independent tests that must agree:
      (a) separating axis test (8 face normals and 36 edge-edge cross products);
      (b) the intersection polytope is computed from its 8 half-spaces (vertices = feasible
          intersections of 3 planes) and has no interior point;
  - the volumes sum to exactly 1.
  Tetrahedra inside the cube with pairwise disjoint interiors and total volume 1 tile the cube.
  The exact range (largest volume minus smallest) is then compared with the stated value.

Part 2: the finite enumerations used in PROOFS.md (tetrahedra with vertices at the corners of
the cube, corner tetrahedra, counting cases, volume formulas).

usage: verify.py [file.json ...]      (default: data/m*.json and the lemmas)
"""
import glob
import itertools
import json
import os
import sys
from fractions import Fraction as Fr

EXPECTED = {
    'm05.json': ('==', Fr(1, 6)), 'm07_I.json': ('==', Fr(1, 18)), 'm07_II.json': ('==', Fr(1, 18)),
    'm08.json': ('==', Fr(1, 12)), 'm09.json': ('==', Fr(1, 12)), 'm10.json': ('==', Fr(1, 12)),
    'm11.json': ('==', Fr(1, 36)), 'm13.json': ('==', Fr(1, 60)),
    'm14.json': ('<', Fr('0.0196723315')), 'm15.json': ('<', Fr('0.0075141620')),
}


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def volume(T):
    return abs(Fr(dot(sub(T[1], T[0]), cross(sub(T[2], T[0]), sub(T[3], T[0]))), 6))


def separated(A, B):
    """Separating axis test: True if some plane separates the two tetrahedra."""
    axes = []
    for T in (A, B):
        for i, j, k in itertools.combinations(range(4), 3):
            axes.append(cross(sub(T[j], T[i]), sub(T[k], T[i])))
    ea = [sub(A[j], A[i]) for i, j in itertools.combinations(range(4), 2)]
    eb = [sub(B[j], B[i]) for i, j in itertools.combinations(range(4), 2)]
    axes += [cross(u, v) for u in ea for v in eb]
    for n in axes:
        if n == (0, 0, 0):
            continue
        pa = [dot(n, p) for p in A]
        pb = [dot(n, p) for p in B]
        if max(pa) <= min(pb) or max(pb) <= min(pa):
            return True
    return False


def half_spaces(T):
    """The 4 half-spaces n.p <= c whose intersection is the tetrahedron."""
    out = []
    for i in range(4):
        f = [T[j] for j in range(4) if j != i]
        n = cross(sub(f[1], f[0]), sub(f[2], f[0]))
        c = dot(n, f[0])
        if dot(n, T[i]) > c:
            n = tuple(-a for a in n)
            c = -c
        assert dot(n, T[i]) < c, 'degenerate tetrahedron'
        out.append((n, c))
    return out


def solve3(planes):
    (a, d1), (b, d2), (c, d3) = planes
    det = dot(a, cross(b, c))
    if det == 0:
        return None
    bc, ca, ab = cross(b, c), cross(c, a), cross(a, b)
    return tuple((d1 * bc[i] + d2 * ca[i] + d3 * ab[i]) / det for i in range(3))


def interiors_meet(A, B):
    H = half_spaces(A) + half_spaces(B)
    pts = set()
    for tr in itertools.combinations(H, 3):
        p = solve3(tr)
        if p is not None and all(dot(n, p) <= c for n, c in H):
            pts.add(p)
    if len(pts) < 4:
        return False
    g = tuple(sum(p[i] for p in pts) / len(pts) for i in range(3))
    return all(dot(n, g) < c for n, c in H)


def check_file(path):
    d = json.load(open(path))
    name = os.path.basename(path)
    V = [tuple(Fr(c) for c in p) for p in d['vertices']]
    assert all(len(p) == 3 and all(0 <= c <= 1 for c in p) for p in V), 'vertex outside the cube'
    assert all(len(t) == 4 and len(set(t)) == 4 for t in d['tetrahedra']), 'bad tetrahedron'
    T = [[V[i] for i in t] for t in d['tetrahedra']]
    vols = [volume(t) for t in T]
    assert len(T) == d['m'], 'wrong number of tetrahedra'
    assert all(v > 0 for v in vols), 'degenerate tetrahedron'
    assert vols == [Fr(v) for v in d['volumes']], 'listed volumes are wrong'
    for A, B in itertools.combinations(T, 2):
        s, i = separated(A, B), interiors_meet(A, B)
        assert s != i, 'the two disjointness tests disagree'
        assert s, 'two tetrahedra overlap'
    assert sum(vols) == 1, 'volumes do not sum to 1'
    rg = max(vols) - min(vols)
    assert rg == Fr(d['range']), 'listed range is wrong'
    if name in EXPECTED:
        op, val = EXPECTED[name]
        assert (rg == val) if op == '==' else (rg < val), 'range differs from the stated value'
    exact = all(v.denominator < 10 ** 6 for v in vols)
    print('%-12s m = %2d  valid dissection of the unit cube  range = %s' % (
        name, len(T), str(rg) if exact else '%.13f... (exact rational in the file)' % float(rg)))
    if exact:
        print('             volumes: ' + '  '.join('%s x %d' % (v, vols.count(v)) for v in sorted(set(vols))))
    else:
        print('             volumes between %.13f... and %.13f...' % (float(min(vols)), float(max(vols))))


def check_lemmas():
    C = list(itertools.product((0, 1), repeat=3))
    adjacent = lambda a, b: sum(x != y for x, y in zip(a, b)) == 1
    neighbours = lambda c: [tuple(c[j] ^ (j == i) for j in range(3)) for i in range(3)]
    on_facet = lambda tri: any(all(p[a] == v for p in tri) for a in range(3) for v in (0, 1))
    boundary_faces = lambda T: sum(on_facet(t) for t in itertools.combinations(T, 3))
    corner_tet = lambda c: [c] + neighbours(c)

    # Lemma 1: tetrahedra with vertices at corners of the cube
    assert {volume(q) for q in itertools.combinations(C, 4)} == {0, Fr(1, 6), Fr(1, 3)}
    assert all(volume(q) == Fr(1, 6) for q in itertools.combinations(C, 4)
               if volume(q) and boundary_faces(q) >= 1)
    print('lemma 1: corner-vertex tetrahedra have volume 0, 1/6 or 1/3; 1/6 if they have a face on the boundary')

    # corner tetrahedra: overlap iff the corners are adjacent
    for a, b in itertools.combinations(C, 2):
        assert interiors_meet(corner_tet(a), corner_tet(b)) == adjacent(a, b)
        assert separated(corner_tet(a), corner_tet(b)) == (not adjacent(a, b))
    independent = lambda k: [s for s in itertools.combinations(C, k)
                             if not any(adjacent(a, b) for a, b in itertools.combinations(s, 2))]
    assert len(independent(4)) == 2 and all(len({sum(c) % 2 for c in s}) == 1 for s in independent(4))
    assert all(len({sum(c) % 2 for c in s}) == 1 for s in independent(3))
    print('lemma 6: corner tetrahedra overlap iff their corners are adjacent; 3 or 4 pairwise '
          'non-adjacent corners have the same parity')

    # plane of D_c: only the three neighbours of c; (X, Y, Z, x) has at most one boundary face
    for c in C:
        N = neighbours(c)
        n = cross(sub(N[1], N[0]), sub(N[2], N[0]))
        assert sorted(x for x in C if dot(n, sub(x, N[0])) == 0) == sorted(N)
        assert all(boundary_faces(tuple(N) + (x,)) <= 1 for x in C if x != c and x not in N)
    # two non-adjacent corner tetrahedra: the half-squares available to the tetrahedra tau are distinct
    for c1, c2 in itertools.combinations(C, 2):
        if adjacent(c1, c2):
            continue
        H = []
        for c, o in ((c1, c2), (c2, c1)):
            hs = set()
            for X, Y in itertools.combinations(neighbours(c), 2):
                far = tuple(X[i] + Y[i] - c[i] for i in range(3))
                if far != o:
                    hs.add(frozenset((X, Y, far)))
            H.append(hs)
        assert not (H[0] & H[1])
    print('lemma 8: the plane of D_c contains no other corner; half-squares of two corner tetrahedra are distinct')

    # counting cases (n3, n2, n1, n0): 3 n3 + 2 n2 + n1 = 12, total m, n3 + n2 <= bound
    def cases(m, bound):
        return sorted((n3, n2, 12 - 3 * n3 - 2 * n2, m - 12 + 2 * n3 + n2)
                      for n3 in range(5) for n2 in range(7)
                      if 12 - 3 * n3 - 2 * n2 >= 0 and m - 12 + 2 * n3 + n2 >= 0 and n3 + n2 <= bound)
    assert cases(7, 3) == [(2, 1, 4, 0), (3, 0, 3, 1)]
    assert cases(11, 0) == []
    assert cases(10, 1) == [(1, 0, 9, 0)]
    assert cases(9, 2) == [(1, 1, 7, 0), (2, 0, 6, 1)]
    assert cases(8, 3) == [(1, 2, 5, 0), (2, 0, 6, 0), (2, 1, 4, 1), (3, 0, 3, 2)]
    for m, lb in ((8, Fr(1, 21)), (9, Fr(1, 32)), (10, Fr(1, 54)), (11, Fr(1, 120))):
        assert Fr(12 - m, 12 * (m - 1)) == lb
    print('counting: the cases (n3, n2, n1, n0) of theorems 2 and 3 and the lower bounds (12 - m)/(12 (m - 1))')

    # volume formulas and planes used in the case analysis, at sample rational parameters
    lerp = lambda p, q, t: tuple(p[i] + t * (q[i] - p[i]) for i in range(3))
    a, b, c, d, e, f = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (1, 0, 1), (0, 1, 1)
    O, A, B, D, E = (0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)
    corners_in_plane = lambda P, Q, R: {x for x in C if dot(cross(sub(Q, P), sub(R, P)), sub(x, P)) == 0}
    for l in (Fr(13, 50), Fr(1, 3), Fr(2, 5), Fr(49, 100)):
        p2 = lerp(a, d, l)
        assert volume((a, b, c, p2)) == l / 3 and volume((b, d, f, p2)) == (1 - l) / 6
        p = lerp(a, b, l)
        assert volume((p, b, c, d)) == (1 - l) / 3 and volume((a, c, e, p)) == l / 6 == volume((a, d, e, p))
        w = lerp(O, D, l)
        assert volume((O, A, B, w)) == l / 3 and volume((A, D, E, w)) == (1 - l) / 6
        assert corners_in_plane(b, c, (1, l, l)) == {b, c} and corners_in_plane(b, f, (1, l, l)) == {b, f}
        assert corners_in_plane(a, c, (l, 1, l)) == {a, c} and corners_in_plane(a, e, (l, 1, l)) == {a, e}
        for t in (Fr(1, 2), Fr(3, 4)):
            u = lerp(O, A, l)
            assert volume((u, A, lerp(u, B, t), lerp(u, D, t))) == t * t * (1 - l) / 3
            x = tuple(l * B[i] + t * (1 - l) * D[i] for i in range(3))
            assert volume((O, A, B, x)) == t * (1 - l) / 3 and volume((O, A, x, D)) == l / 3
    print('formulas: volumes and planes of the case analysis, checked at sample rational parameters')


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(here, 'data', 'm*.json')))
    for path in files:
        check_file(path)
    if not sys.argv[1:]:
        check_lemmas()
    print('ALL CHECKS PASSED (%d dissection(s))' % len(files))


if __name__ == '__main__':
    main()
