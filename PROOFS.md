# Proofs

Status: these proofs were written with the help of an AI assistant and checked line by line by a
second, independent AI agent. **No human referee has read them.** Please report any gap by opening
an issue.

## Setting and results

C = [0, 1]³ is the unit cube; its 8 *corners* are the points with coordinates 0 or 1, its 6
*facets* are its square faces. A *dissection* of C into m tetrahedra is a set of m non-degenerate
tetrahedra with pairwise disjoint interiors whose union is C. The vertices of the tetrahedra are
arbitrary points of C, and the dissection need not be face-to-face: a vertex of one tetrahedron
may lie inside an edge or a face of another.

The *range* of a dissection is the largest volume minus the smallest, and Δ₃(m) is the infimum of
the range over all dissections of C into m tetrahedra. By Mead's theorem, the range can be 0 only
if m is a multiple of 6.

- **Theorem 1.** The cube has exactly one dissection into 5 tetrahedra up to symmetry: four
  corner tetrahedra of volume 1/6 and a regular tetrahedron of volume 1/3. Hence Δ₃(5) = 1/6.
  (And there is no dissection into fewer than 5.)
- **Theorem 2.** Δ₃(7) = 1/18, and the value is attained.
- **Theorem 3.** For m = 8, 9, 10, 11, every dissection of the cube into m tetrahedra contains a
  tetrahedron of volume at most 1/12.
- **Corollary 4.** Δ₃(8) ≥ 1/21, Δ₃(9) ≥ 1/32, Δ₃(10) ≥ 1/54, Δ₃(11) ≥ 1/120; and a dissection
  into 8, 9, 10 or 11 tetrahedra that contains a tetrahedron of volume ≥ 1/6 has range ≥ 1/12.
- **Upper bounds** (explicit dissections in `data/`): Δ₃(8), Δ₃(9), Δ₃(10) ≤ 1/12, Δ₃(11) ≤ 1/36,
  Δ₃(13) ≤ 1/60, Δ₃(14) ≤ 0.0196723315, Δ₃(15) ≤ 0.0075141620; in general Δ₃(3n) ≤ Δ₂(n)/3,
  where Δ₂(n) is the corresponding quantity for the unit square cut into n triangles.

The finite enumerations quoted below ("by enumeration") are done by `verify.py`.

Notation. For a corner c, its three *neighbours* are the corners joined to c by an edge of the
cube. The *corner tetrahedron* at c is the convex hull of c and its three neighbours; its volume
is 1/6. A *half-square* is one of the two triangles obtained by cutting a facet along a diagonal.
A *boundary face* of a tetrahedron of a dissection is a face contained in a facet of C; b denotes
the number of boundary faces of a tetrahedron.

## Lemmas

**Lemma 1.** A tetrahedron contained in C has volume at most 1/3. A non-degenerate tetrahedron
whose vertices are corners of C has volume 1/6 or 1/3, and 1/6 if it has a boundary face.

*Proof.* The volume is the absolute value of an affine function of each vertex, hence a convex
function of each vertex: its maximum over C is attained with all vertices at corners. The 70
quadruples of corners give the volumes 0, 1/6, 1/3, and those with a face in a facet give 1/6
(by enumeration). ∎

**Lemma 2.** A tetrahedron contained in C with a boundary face of area A has volume at most
A/3 ≤ 1/6. If the boundary face is a half-square, the volume is h/6, where h ≤ 1 is the distance
from the fourth vertex to the facet.

*Proof.* Volume = A h/3, with A ≤ 1/2 (a triangle in a unit square) and h ≤ 1. ∎

**Lemma 3.** In a dissection, each facet F of C is tiled by the boundary faces contained in F.

*Proof.* A tetrahedron contained in C lies on one side of the plane of F, so it meets F in a
face, an edge, a vertex or the empty set. The tetrahedra cover F, and edges and vertices have
area zero, so the faces contained in F cover F. Two such faces cannot overlap in a set of
positive area: their tetrahedra, both on the same side of F, would have a common interior
point. ∎

**Lemma 4.** A tetrahedron contained in C has at most 3 boundary faces. If it has 3, it is
conv(c, c + α e₁, c + β e₂, c + γ e₃), where c is a corner and e₁, e₂, e₃ are the unit vectors
along the edges of C at c, and its volume is αβγ/6.

*Proof.* Two faces of a tetrahedron share an edge, so they lie neither in the same plane nor in
parallel planes; the facets of C have only 3 directions. Three boundary faces lie in the three
facet planes through one corner c; their common vertex is c and their common edges lie on the
three edges of C at c. ∎

**Lemma 5 (covering of interior faces).** Let φ be a face of a tetrahedron T of a dissection, not
contained in a facet of C. Then φ is covered, up to a set of area zero, by faces of other
tetrahedra of the dissection that lie in the plane of φ, on the side opposite to T.

*Proof.* The relative interior of φ lies in the interior of C (a triangle in C that touches a
facet at a relatively interior point lies in that facet). Let q be a relatively interior point
of φ. Points close to q, strictly on the side opposite to T, belong to tetrahedra other than T;
as there are finitely many closed tetrahedra, one of them, T′, contains q. T′ contains no point r
strictly on the side of T: otherwise the segment from q to r would lie in T′ and enter the
interior of T, and T′, T would have a common interior point. So T′ lies in the closed half-space
opposite to T, and meets the plane of φ in a face, an edge or a vertex. Edges and vertices of
the finitely many tetrahedra have area zero in the plane. ∎

The covering faces may extend beyond φ when the dissection is not face-to-face; only the
covering property is used. Two covering faces of the same φ cannot overlap in positive area
(their tetrahedra are on the same side of the plane).

**Lemma 6.** The corner tetrahedra at two corners c, c′ overlap if and only if c and c′ are
adjacent. Four pairwise non-adjacent corners form one of the two parity classes (x + y + z even,
or odd); three pairwise non-adjacent corners have the same parity.

*Proof.* By enumeration. ∎

**Lemma 7 (structure when all volumes exceed 1/12).** Consider a dissection of C in which every
tetrahedron has volume > 1/12. Then:

1. every facet of C is cut by one diagonal into two half-squares, each a boundary face; there
   are exactly 12 boundary faces;
2. a tetrahedron with b ≥ 2 has its four vertices at corners of C and volume exactly 1/6
   (for b = 3 it is a corner tetrahedron);
3. a tetrahedron with b = 1 is the convex hull of a half-square and a point p, of volume
   h(p)/6 ≤ 1/6;
4. if n_b denotes the number of tetrahedra with b boundary faces, then 3n₃ + 2n₂ + n₁ = 12 and
   n₀ + n₁ + n₂ + n₃ = m.

*Proof.* 1. By Lemma 2 a boundary face has area A ≥ 3 × volume > 1/4, so by Lemma 3 a facet is
tiled by 2 or 3 boundary faces (one triangle cannot fill a square). Suppose a unit square is tiled
by 3 triangles. Their angles sum to 3π. The four corners of the square absorb 2π. Any other
point that is a vertex of some triangle absorbs π (if it lies on a side of the square, or in the
interior of an edge of another triangle) or 2π. So there is exactly one such point q, and it
absorbs π. If q lies on a side of the square, the opposite side contains no vertex other than
its endpoints, so it is an edge of a triangle whose third vertex lies on the side containing q:
that triangle has area 1/2. If q is interior to the square, it lies in the interior of an edge
of a triangle; the endpoints of this edge are corners, so the edge is a diagonal and the
triangle is a half-square of area 1/2. In both cases the two other triangles have total area
1/2, and one of them has area ≤ 1/4: excluded. So each facet is tiled by 2 triangles, whose
angles sum to 2π: all their vertices are corners of the square, and they are the two halves cut
by a diagonal.

2. Two boundary faces of a tetrahedron lie in two adjacent facets, and their common edge lies on
the common edge of these facets; as they are half-squares, this edge is an entire edge of the
cube and the four vertices are corners of C. By Lemma 1 the volume is 1/6. If b = 3, Lemma 4
with volume 1/6 gives α = β = γ = 1.

3. Lemma 2. 4. Count the 12 boundary faces and the m tetrahedra. ∎

**Lemma 8 (the inner face of a corner tetrahedron).** In the situation of Lemma 7, suppose that
the corner tetrahedron at c belongs to the dissection, let X, Y, Z be the neighbours of c and
D_c the triangle XYZ (the face of the corner tetrahedron that is not a boundary face). Then:

1. D_c is the whole section of C by its plane, and X, Y, Z are the only corners of C in this
   plane;
2. D_c is tiled by faces of other tetrahedra of the dissection, each with b = 1 or b = 0;
3. a tetrahedron with b = 1 that has a face in the plane of D_c is conv(X′, Y′, c′, p), where
   X′, Y′ are two of X, Y, Z, c′ is the corner opposite to c in the facet containing c, X′, Y′,
   and p ∈ D_c; its face in the plane is τ = X′Y′p and its volume is
   (area(τ)/area(D_c))/6;
4. consequently, if D_c is tiled only by faces of tetrahedra with b = 1, then either one of them
   has volume exactly 1/6 (and τ = D_c), or one of them has volume ≤ 1/12, contradicting the
   hypothesis of Lemma 7. More generally, at most one face τ can occur, and it occupies more than
   half of the area of D_c;
5. if the corner tetrahedra at two non-adjacent corners c₁, c₂ both belong to the dissection,
   no tetrahedron with b = 1 has a face in both planes D_c₁ and D_c₂.

*Proof.* 1. For c = (0, 0, 0) the plane is x + y + z = 1; the general case follows by symmetry
(and by enumeration for the corners).

2. By Lemma 5, D_c is covered by faces of other tetrahedra lying in its plane, on the side
opposite to c. By 1 these faces are contained in D_c, and they do not overlap, so they tile
D_c. A tetrahedron with b ≥ 2 has its vertices at corners (Lemma 7); a face in the plane would
be XYZ itself, and the tetrahedron would be conv(X, Y, Z, x) with x a corner other than c, which
has at most one boundary face (by enumeration).

3. Three of the four vertices of the tetrahedron lie in the plane; at least two of them are
vertices of its half-square H, hence corners in the plane: two of X, Y, Z, say X′ and Y′. (Not
all three vertices of H: H is not D_c.) The segment X′Y′ is a diagonal of the facet containing
c, X′, Y′, which is the only facet containing both; this facet is cut along X′Y′, the half
containing c belongs to the corner tetrahedron, so H = X′Y′c′. The face in the plane is X′Y′p
with p ∈ D_c. The distance h from a point of D_c to that facet is an affine function on D_c,
equal to 0 on X′Y′ and to 1 at the third vertex Z′ of D_c: h(p) is the barycentric coordinate of
p relative to Z′, that is area(X′Y′p)/area(D_c). The volume is h(p)/6.

4. The areas of the faces τ tiling D_c add up to area(D_c), so the volumes add up to 1/6.
A volume > 1/12 means that τ covers more than half of D_c.

5. The half-square of such a tetrahedron would be of the form X′Y′c′ for c₁ and for c₂ at the
same time; the half-squares available for c₁ (those not belonging to the corner tetrahedron at
c₂) and for c₂ are distinct (by enumeration). ∎

## Theorem 1: five tetrahedra

Let k be the number of tetrahedra with at least one boundary face in a dissection into m ≤ 5
tetrahedra.

*Faces.* A boundary face has area ≤ 1/2, so by Lemma 3 each facet contains at least 2 boundary
faces: at least 12 in total. By Lemma 4, 12 ≤ 3k, so k ≥ 4.

*Volumes.* By Lemmas 1 and 2, 1 ≤ k/6 + (m − k)/3. For m ≤ 4 this fails (k = m = 4 gives 2/3).
For m = 5 it gives k ≤ 4.

So m = 5, k = 4, each of the four tetrahedra has exactly 3 boundary faces and volume exactly
1/6 (otherwise the total volume would be < 4/6 + 1/3 = 1), and the fifth has volume 1/3. By
Lemma 4, αβγ = 1 with α, β, γ ≤ 1: the four tetrahedra are corner tetrahedra. By Lemma 6 their
corners are pairwise non-adjacent, so they form a parity class, and the fifth tetrahedron, the
closure of the complement, is the regular tetrahedron on the other class. The two parity classes
are exchanged by a symmetry of the cube. The volumes are (1/6, 1/6, 1/6, 1/6, 1/3) and the
range is 1/6. ∎

## Theorem 2: seven tetrahedra

**Upper bound.** Two dissections of range 1/18 (`data/m07_I.json`, `data/m07_II.json`), with
O = (0,0,0), A = (1,1,0), B = (1,0,1), D = (0,1,1), E = (1,1,1):

- I. The four corner tetrahedra at (1,0,0), (0,1,0), (0,0,1), (1,1,1) (volume 1/6), and the
  regular tetrahedron OABD cut into three tetrahedra of volume 1/9 from the centroid of its
  face ABD.
- II. The three corner tetrahedra at (1,0,0), (0,1,0), (0,0,1) (volume 1/6), the tetrahedron
  ABEw (volume 1/6) and OABw, ADEw, BDEw (volume 1/9 each), with w = (0, 1/3, 1/3).

**Lower bound.** Suppose a dissection into 7 tetrahedra has range < 1/18.

(1) The largest volume is ≥ 1/7, so every volume is > 1/7 − 1/18 = 11/126 > 1/12, and Lemmas 7
and 8 apply.

(2) Let s = n₃ + n₂ be the number of tetrahedra with b ≥ 2; they have volume 1/6.
- s ≥ 6: the total volume would exceed 1.
- s = 5: the two others share a volume 1/6; one has volume ≤ 1/12.
- s = 4: the three others share 1/3; one has volume ≤ 1/9 and the range is ≥ 1/6 − 1/9 = 1/18.
- s ≤ 3: n₀ = 2n₃ + n₂ − 5 ≥ 0 forces (n₃, n₂, n₁, n₀) = (3, 0, 3, 1) or (2, 1, 4, 0).

(3) Case (2, 1, 4, 0). The two corner tetrahedra, at c₁ and c₂, are at non-adjacent corners
(Lemma 6). There is no tetrahedron with b = 0, so by Lemma 8 (2 and 4) each D_cᵢ is a face of a
tetrahedron with b = 1 and volume 1/6, and these two tetrahedra are distinct (Lemma 8.5). With
the three tetrahedra with b ≥ 2, five tetrahedra have volume 1/6; the two others share 1/6 and
one has volume ≤ 1/12: excluded.

(4) Case (3, 0, 3, 1). The three corner tetrahedra are at pairwise non-adjacent corners, of the
same parity (Lemma 6): say (1,0,0), (0,1,0), (0,0,1). The three remaining half-squares are ABE,
ADE, BDE, so the rest R = conv(O, A, B, D, E) of the cube is tiled by T_x = ABEp_x,
T_y = ADEp_y, T_z = BDEp_z and one tetrahedron T₀ with b = 0. The inner faces of the three
corner tetrahedra are L_a = OAB, L_b = OAD, L_c = OBD. By Lemma 8, each triangle L = Oe₁e₂ among
them is tiled by the face e₁e₂p of the corresponding T (if p lies in the plane) and at most one
face of T₀. So for each L:

- (a) p = O, and the corresponding T has volume 1/6; or
- (b) T₀ has a face in the plane of L, equal to L or to a triangle Ope with p on an edge of L
  from O (the complement of e₁e₂p in L must be a triangle).

If (a) holds three times, T₀ is empty. Twice: five tetrahedra have volume 1/6 and the two others
share 1/6. Once: four tetrahedra have volume 1/6, the three others share 1/3 and the range is
≥ 1/18. Never: T₀ has a face in each of the three planes, which meet only at O, so
T₀ = Ouvw with u, v, w on the segments OA, OB, OD (the pairwise intersections of the planes);
by (b), in each plane one of the two points is the far endpoint, so at least two of u = A,
v = B, w = D hold: say u = A and v = B. If w = D, T₀ is the regular tetrahedron, of volume 1/3,
and the range is ≥ 1/3 − 1/6. Otherwise w = (0, σ, σ) with 0 < σ < 1, p_y = p_z = w, T₀ has
volume σ/3, T_y and T_z have volume (1 − σ)/6, and the total volume gives vol(T_x) = 1/6.
A range < 1/18 would require σ/3 > 1/9 and (1 − σ)/6 > 1/9, that is σ > 1/3 and σ < 1/3.

All cases contradict the hypothesis, so Δ₃(7) ≥ 1/18. ∎

(The last case with σ = 1/3 is dissection II.)

## Theorem 3: eight to eleven tetrahedra

Suppose that a dissection into m tetrahedra, 8 ≤ m ≤ 11, has all its volumes > 1/12. Lemmas 7
and 8 apply.

**Counting.** Let s = n₃ + n₂. From 12 = 3n₃ + 2n₂ + n₁ ≤ 3s + (m − s) we get s ≥ (12 − m)/2 > 0.
Let u be the number of tetrahedra of volume ≥ 1/6. The tetrahedra with b ≥ 2 have volume 1/6,
so u ≥ s; and u/6 + (m − u)/12 < 1 gives u ≤ 11 − m.

By Lemma 8, when there is no tetrahedron with b = 0, each corner tetrahedron provides a
tetrahedron with b = 1 and volume 1/6, and two corner tetrahedra provide two distinct ones.
We call this *the tool*.

- m = 11: s ≥ 1 and u ≤ 0. Impossible.
- m = 10: s = u = 1, so (n₃, n₂, n₁, n₀) = (1, 0, 9, 0); by the tool u ≥ 2. Impossible.
- m = 9: s = 2, so (1, 1, 7, 0), excluded by the tool (u ≥ 3), or (2, 0, 6, 1).
- m = 8: s ∈ {2, 3}; (2, 0, 6, 0) and (1, 2, 5, 0) are excluded by the tool (u ≥ 4); there remain
  (2, 1, 4, 1) and (3, 0, 3, 2).

In the three remaining cases s = 11 − m, hence u = s: every tetrahedron with b ≤ 1 has volume
in ]1/12, 1/6[.

**Two corner tetrahedra and one tetrahedron T₀ with b = 0** (cases (2, 0, 6, 1) and
(2, 1, 4, 1)). For each of the two corners c, the triangle D_c is not a single face τ (its
tetrahedron would have volume 1/6). So by Lemma 8, T₀ has a face φ in the plane of D_c, with
D_c = φ, or D_c = φ ∪ τ where τ is as in Lemma 8.3 (then p lies on a side of D_c, so that the
complement of τ is a triangle).

If c₁ and c₂ are opposite corners of the cube, the planes of D_c₁ and D_c₂ are parallel and T₀
cannot have a face in each. So, up to symmetry, c₁ = (0,0,0) and c₂ = (1,1,0). Put

  a = (1,0,0), b = (0,1,0), c = (0,0,1), d = (1,1,1), e = (1,0,1), f = (0,1,1),

so that D₁ = abc and D₂ = abd. The bottom facet is cut along ab and belongs to the two corner
tetrahedra. The free half-squares are bcf, ace, ade, bdf and the two halves of the top facet.
A face τ₁ in D₁ is acp (on the half-square ace) or bcp (on bcf); a face τ₂ in D₂ is adp (on ade)
or bdp (on bdf). (A face abp is impossible: its half-square would be in the bottom facet.)

The faces φ₁, φ₂ of T₀ share an edge of T₀, which lies on the line ab, the intersection of the
two planes, hence in the segment ab. Let λᵢ = area(φᵢ)/area(Dᵢ).

- (α) The common edge is ab. Then T₀ = abp₁p₂ with p₁ on ac or bc and p₂ on ad or bd, and
  vol(T₀) = λ₁λ₂/3, because vol(abcd) = 1/3. If λᵢ < 1, τᵢ exists and its tetrahedron has volume
  (1 − λᵢ)/6 > 1/12, so λᵢ < 1/2. As 1/12 < vol(T₀) < 1/6, λ₁λ₂ lies in ]1/4, 1/2[: exactly one
  of λ₁, λ₂ equals 1, and the other lies in ]1/4, 1/2[.
- (β) The common edge is pb or ap, with p = a + μ(b − a), 0 < μ < 1. For pb: T₀ = pbcd, of
  volume (1 − μ)/3, with τ₁ = acp and τ₂ = adp, carried by ace and ade, of volume μ/6 each.
  For ap: T₀ = apcd, with τ₁ = bcp and τ₂ = bdp carried by bcf and bdf.

*Case m = 9, (2, 0, 6, 1).* Each of the six free half-squares carries a tetrahedron with b = 1.

(α) Up to the symmetries exchanging x and y, or c₁ and c₂, we have p₁ = c and p₂ = (1, λ, λ) on
ad, with 1/4 < λ < 1/2. Then τ₂ = bdp₂ is a face of the tetrahedron U carried by bdf. Consider
the faces bcp₂ of T₀ and bfp₂ of U. Their planes are (1 − 2λ)x + y + z = 1 and (1 − λ)x + y = 1;
the only corners of C they contain are b, c and b, f respectively. Neither face is a boundary
face, so each must be covered from the other side (Lemma 5) by faces of tetrahedra having three
vertices in the plane. A tetrahedron with b ≥ 2 has only corners as vertices; a tetrahedron with
b = 1 would need two vertices of its half-square in the plane; T₀ = abcp₂ is the only one with
b = 0, and it has only the vertices b and p₂ in the plane of bfp₂.
The half-squares containing b and c are bcf and one that belongs to the corner tetrahedron at
c₁; those containing b and f are bcf and bdf (which carries U itself). So in both cases the only
candidate is the tetrahedron W = bcfq carried by bcf: p₂ lies in its faces bcq and bfq, hence on
their common edge bq. Since x(b) = 0, x(p₂) = 1 and x(q) ≤ 1, we get q = p₂, and W has volume
x(q)/6 = 1/6: then u ≥ 3. Excluded.

(β) The two corner tetrahedra, T₀ and the two tetrahedra carrying τ₁, τ₂ have total volume
1/3 + (1 − μ)/3 + 2μ/6 = 2/3. The four remaining tetrahedra share 1/3: one has volume ≤ 1/12.
Excluded.

*Case m = 8, (2, 1, 4, 1).* The tetrahedron with b = 2 is the union of two free half-squares
sharing an edge of the cube. The possible pairs give the corner tetrahedra at e or f (which
have b = 3: excluded here) or, the top facet being cut along ef, one of bcfe, acef, adef, bdfe.
These four are exchanged by the symmetries x ↔ y and (x, y, z) → (1 − y, 1 − x, z), which
preserve {c₁, c₂}. So we may assume that this tetrahedron is P = bcfe; this uses up the
symmetries. The four tetrahedra with b = 1 are carried by ace (call it X), ade (Y), bdf (U) and
def.

(α), p₁ = c and p₂ = (1, λ, λ) on ad. The face bcp₂ of T₀ lies in a plane containing only the
corners b, c; the only free half-square containing b and c is bcf, which belongs to P, and P has
no face in this plane. The face cannot be covered. Excluded.

(α), p₁ = c and p₂ = (λ, 1, λ) on bd. This is the mirror image of the case m = 9: τ₂ = adp₂ is a
face of Y; the planes x + (1 − 2λ)y + z = 1 and x + (1 − λ)y = 1 of the faces acp₂ of T₀ and
aep₂ of Y contain only the corners a, c and a, e; the only candidate to cover them is X, so
X = acep₂, of volume y(p₂)/6 = 1/6, and u ≥ 4. Excluded.

(α), p₂ = d and p₁ on ac. Then τ₁ = bcp₁ would be carried by bcf, which belongs to P. Excluded.

(α), p₂ = d and p₁ on bc. Then τ₁ = acp₁ and X = acep₁. The face bce of P lies in the plane
y + z = 1, with P on the side y + z ≥ 1. On the other side, the only tetrahedron with three
vertices in this plane is X, with the face cep₁: the corner tetrahedra and T₀ = abp₁d have at
most two vertices in it, and so have Y, U and the tetrahedron carried by def. The part bp₁e of
the face is not covered (p₁ ≠ b). Excluded.

(β), edge pb. The total volume of the two corner tetrahedra, P, T₀, X and Y is
1/3 + 1/6 + (1 − μ)/3 + 2μ/6 = 5/6; the two remaining tetrahedra share 1/6. Excluded.

(β), edge ap. τ₁ = bcp would be carried by bcf, which belongs to P. Excluded.

*Case m = 8, (3, 0, 3, 2).* As in the proof of Theorem 2, the corner tetrahedra are at (1,0,0),
(0,1,0), (0,0,1), and with O, A, B, D, E, L_a = OAB, L_b = OAD, L_c = OBD as there, the region
R = conv(O, A, B, D, E) is tiled by T_x = ABEp_x, T_y = ADEp_y, T_z = BDEp_z and two tetrahedra
S₁, S₂ with b = 0, all five of volume in ]1/12, 1/6[. By Lemma 8, each of L_a, L_b, L_c is tiled
by at most one face τ of the corresponding T (τ_x = ABp_x in L_a, and so on), covering more than
half of it, and by faces of S₁ and S₂.

O is an extreme point of R, so a tetrahedron of the tiling of R containing O has O as a vertex.
It is not T_x, T_y or T_z (p_x = O would give vol(T_x) = 1/6). So S₁ or S₂ has the vertex O.

For points P, Q on a ray from O we write P = σQ. Recall vol(OABD) = 1/3.

**I. Only S₁ has the vertex O.** Then S₁ alone fills a neighbourhood of O in R, so its cone at O
is the cone of R at O, spanned by A, B, D: S₁ = Ouvw with u = σ_u A, v = σ_v B, w = σ_w D on the
segments OA, OB, OD, and vol(S₁) = σ_u σ_v σ_w/3, so σ_u σ_v σ_w ∈ ]1/4, 1/2[. In particular each
σ is > 1/4. S₂ has faces in at most two of the planes L_a, L_b, L_c (three faces in these
planes would have the common vertex O). In a plane where S₂ has no face, the part of L not
covered by S₁ is empty or a single triangle τ; for L_a this means u = A or v = B, and similarly
for the others.

I.0. S₂ has a face in none of the planes. Then (u = A or v = B), (u = A or w = D),
(v = B or w = D): two of the σ equal 1, say u = A and v = B. Then p_y = p_z = w and
vol(S₁) + vol(T_y) + vol(T_z) = σ_w/3 + 2(1 − σ_w)/6 = 1/3. As vol(R) = 1/2,
vol(T_x) + vol(S₂) = 1/6: one of them is ≤ 1/12. Excluded.

I.1. S₂ has a face in exactly one of the planes, say L_a. Then (u = A or w = D) and
(v = B or w = D).
- If w ≠ D, then u = A and v = B: S₁ covers L_a and S₂ has no face in it. Contradiction.
- If w = D: one of u = A, v = B holds; otherwise the complements uAD in L_b and vBD in L_c would
  be faces τ, covering the fractions 1 − σ_u > 1/2 and 1 − σ_v > 1/2, and σ_u σ_v < 1/4. By the
  symmetry y ↔ z, which exchanges A and B and preserves L_a, say u = A; then v ≠ B, since
  vol(S₁) < 1/3. So S₁ = OAvD. The plane of its face AvD is x + (2σ_v − 1)y + z = 2σ_v; it leaves
  O on one side and B, E strictly on the other, so the section of R by this plane is the
  triangle AvD itself. By Lemma 5 this triangle is tiled by faces of tetrahedra lying on the
  other side: T_x and T_z have at most two vertices in the plane, so these faces belong to T_y
  (a face ADp_y) and S₂. If T_y alone covered it, then p_y = v and vol(T_y) = (1 − y(v))/6 = 1/6:
  excluded. So S₂ has a face χ in this plane, and AvD is χ, or χ together with ADp_y; in each
  case χ has the vertex v and another vertex on the segment vD (namely D or p_y). Likewise, in
  L_a the complement of the face OAv of S₁ is the triangle AvB, which is the face ψ of S₂, or ψ
  together with τ_x = ABp_x; in each case ψ has the vertex v and another vertex on the segment
  vB (namely B or p_x). So S₂ has three non-collinear vertices in the plane of L_c: it has a
  face in L_c. Contradiction.

I.2. S₂ has faces in exactly two of the planes, say L_a and L_b; then v = B or w = D. The two
faces ψ_a, ψ_b of S₂ share an edge of S₂ lying on the line OA. The face Ouv of S₁ contains the
segment Ou, so this edge lies in the segment uA, and u ≠ A. In L_a, the complement of Ouv is the
quadrilateral uABv (if v ≠ B) or the triangle uAB (if v = B); it is ψ_a, or ψ_a together with
τ_x = ABp_x. If v ≠ B, the only possibility with an edge of ψ_a on OA is ψ_a = uAv, τ_x = ABv.
If v = B: ψ_a = uAB; or ψ_a = uAp_x with p_x on uB; or ψ_a = up_xB with p_x on uA. The same
holds in L_b with w, D, p_y. So the common edge is uA, or up with p = p_x = p_y on uA.

- Edge uA, v = B and w = D. S₂ = uArr′ with r = u + t(B − u), r′ = u + t′(D − u), 0 < t, t′ ≤ 1,
  and vol(S₂) = t t′(1 − σ_u)/3. If t < 1, then τ_x = ABr covers the fraction (1 − t)(1 − σ_u)
  of L_a, which must be > 1/2; as 1 − σ_u < 3/4, this gives t < 1/3 and vol(S₂) < 1/12. So
  t = 1, and likewise t′ = 1: S₂ = uABD and S₁ = OuBD tile OABD, their volumes add up to 1/3
  and one of them is ≥ 1/6. Excluded.
- Edge uA, v = B and w ≠ D (the case v ≠ B, w = D is symmetric). In L_b, ψ_b = uAw and
  τ_y = ADw covers the fraction 1 − σ_w > 1/2, so σ_w < 1/2; then σ_u σ_w > 1/4 gives σ_u > 1/2.
  S₂ = uArw with r on uB, so vol(S₂) ≤ vol(uABw) = (1 − σ_u)σ_w/3 < 1/12. Excluded.
- Edge up. Then v = B, w = D, S₂ = upBD with p = u + κ(A − u), τ_x = ABp and τ_y = ADp.
  vol(S₂) = κ(1 − σ_u)/3 > 1/12 gives κ > 1/3, and the fraction (1 − κ)(1 − σ_u) > 1/2 covered by
  τ_x gives 1 − κ > 2/3. Excluded.

**II. S₁ and S₂ both have the vertex O.** Their cones at O have disjoint interiors and their
union is the cone of R at O, the cone over the triangle ABD. A plane through O separates them
and cuts the triangle ABD into two triangles, so it passes through a vertex of ABD: say it
contains OA. Then S₁ = Ou₁vx₁ and S₂ = Ou₂x₂w with u₁, u₂ on OA, v on OB, w on OD, and x₁, x₂ on
the same ray from O in the interior of the angle BOD, in L_c.

In L_a, S₂ has no face (only its vertices O and u₂ lie in this plane), so u₁ = A or v = B.
Likewise in L_b, u₂ = A or w = D.

In L_c, the faces Ovx₁ of S₁ and Ox₂w of S₂, and possibly τ_z = BDp_z, tile L_c. If x₁ ≠ x₂, the
segment x₁x₂ would lie in an edge of τ_z; but the edges of τ_z are BD and two segments from B
and from D, and none of them lies on a line through O interior to the angle BOD. So
x₁ = x₂ = x, and the complement of Ovx ∪ Oxw in L_c is the polygon vBDwx, which must be empty
or a triangle with side BD: either (v = B and w = D), or (w = D and x on vD), or
(v = B and x on Bw).

*u₁ = u₂.* Suppose not, say u₁ closer to O than u₂ (the other case is symmetric). The triangle
u₁u₂x, part of the face Ou₂x of S₂, is not covered by the face Ou₁x of S₁; by Lemma 5 it is
covered by faces of other tetrahedra lying in the plane Π = OAx, on the side of S₁, that is on
the side of B. Write x = βB + γD with β, γ > 0. The plane Π contains the corners O and A, and
no other corner unless β = γ, in which case Π is the plane x = y and also contains (0,0,1) and
E. A tetrahedron T_x, T_y or T_z with a face in Π has two of its three corner vertices in Π: so
β = γ, the tetrahedron is T_x or T_y, and the face is AEp. Only T_x lies on the side of B. The
section of R by Π is the quadrilateral with vertices O, A, E and the midpoint of BD, and OA is
one of its sides; the face AEp_x covers the part of u₁u₂x near the segment u₁u₂, which lies on
this side, so it has an edge on OA: p_x = (κ, κ, 0) with 0 ≤ κ < 1. In the coordinates (t, z)
of Π, where t = x = y, the triangle AEp_x is contained in z ≤ (t − κ)/(1 − κ) ≤ t. But
x = (β, β, 2β) has z = 2t > t: x and the points of u₁u₂x close to it are not covered.
Contradiction.

So S₁ = Ouvx and S₂ = Ouxw with u = σ_u A, x = βB + γD, and
vol(S₁) = σ_u σ_v γ/3, vol(S₂) = σ_u σ_w β/3, hence σ_u σ_v γ > 1/4 and σ_u σ_w β > 1/4; moreover
(u = A or v = B) and (u = A or w = D).

- v = B and w = D. If x is not on BD, τ_z = BDx covers the fraction 1 − β − γ > 1/2 of L_c,
  but β, γ > 1/4. So β + γ = 1. Adding the two inequalities gives σ_u > 1/2. If u ≠ A, then
  τ_x = ABu covers the fraction 1 − σ_u > 1/2 of L_a: contradiction. So u = A, S₁ and S₂ tile
  OABD and one of them has volume ≥ 1/6. Excluded.
- w = D, v ≠ B and x on vD. Then u = A, and τ_z = BDv covers the fraction 1 − σ_v > 1/2, so
  σ_v < 1/2. Now x = (1 − γ)v + γD, so β = (1 − γ)σ_v. From σ_v γ > 1/4 we get γ > 1/2; from
  β = (1 − γ)σ_v > 1/4 we get 1 − γ > 1/2. Excluded.
- v = B, w ≠ D and x on Bw: symmetric.

All cases are excluded: some tetrahedron has volume ≤ 1/12. ∎

## Corollary 4

Let v_min ≤ 1/12 and v_max be the extreme volumes. The m − 1 other tetrahedra have total volume
1 − v_min, so v_max ≥ (1 − v_min)/(m − 1) and

  range ≥ (1 − v_min)/(m − 1) − v_min ≥ (11/12)/(m − 1) − 1/12 = (12 − m)/(12(m − 1)),

which is 1/21, 1/32, 1/54, 1/120 for m = 8, 9, 10, 11. If some volume is ≥ 1/6, the range is
≥ 1/6 − 1/12 = 1/12. ∎

So for m = 8, 9, 10 the record 1/12 is the exact value if and only if no dissection has all its
volumes in an interval of length < 1/12, which would have to be contained in ]0, 1/6[.

**Conjecture.** Every dissection of the cube into at most 10 tetrahedra contains a tetrahedron
of volume ≥ 1/6. With Corollary 4 this would give Δ₃(8) = Δ₃(9) = Δ₃(10) = 1/12.

## Upper bounds

The dissections of `data/` are checked exactly by `verify.py`. Their structure:

- m = 8, 9, 10, 11: start from the 5-piece dissection. The regular tetrahedron is kept whole,
  cut into 3 equal parts from the centroid of a face, or into 4 equal parts from its centroid;
  each corner tetrahedron is kept whole or cut into 2 equal parts through the midpoint of an
  edge. m = 8: 4 corners (1/6) and 4 parts (1/12). m = 9: 2 corners (1/6), 2 halved (4 × 1/12),
  3 parts (1/9). m = 10: 2 corners (1/6), 2 halved and 4 parts (8 × 1/12). m = 11: 4 halved
  (8 × 1/12) and 3 parts (1/9), range 1/36.
- m = 13: range 1/60, volumes 1/15 (5 times) and 1/12 (8 times).
- m = 14 and m = 15: found by numerical optimisation, then written with rational coordinates;
  the range of each file is an exact rational number.
- **Prisms.** If the unit square is cut into n triangles of areas a₁, …, a_n, the prism over the
  triangle of area aᵢ has volume aᵢ and is cut into 3 tetrahedra of volume aᵢ/3 (a triangular
  prism PQR P′Q′R′ is the union of PQRR′, PQQ′R′ and PP′Q′R′). So Δ₃(3n) ≤ Δ₂(n)/3. With
  Δ₂(5) = (5√5 − 11)/8 (M. Li, 2026, preprint) this gives Δ₃(15) ≤ (5√5 − 11)/24 ≈
  0.00751416197912. The file `data/m15.json` is a different dissection, with rational
  coordinates, found independently by the optimisation; its range exceeds this value by less
  than 2 × 10⁻¹⁶, and it is the one that `verify.py` certifies (Δ₃(15) ≤ 0.0075141620).
