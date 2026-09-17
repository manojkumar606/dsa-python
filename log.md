# DSA Practice Log

My re-solve journal. One line per problem attempt. The rule: a problem is **mastered** only when I can re-solve it **cold** (from memory, no hints).

**How to use:** after each session, add a row. Be honest in "Result" — the blanks are the signal, not the wins.

- ⭐ = solved cleanly, cold
- 🔁 = solved but needed a hint / recovered from a blank → re-solve later
- ❌ = blanked, couldn't finish → must redo cold

---

## Sessions

| Date | Problem | Step | Result | Time / Space | Notes (what tripped me) |
|------|---------|------|--------|--------------|-------------------------|
| 2026-09-16 | reverse_array | Step 1 | 🔁 | O(n) / O(1) | Blanked at first, recovered. Forgot Big-O notation — revise O(1) vs O(n). |
| 2026-09-17 | reverse_array | Step 1 | ⭐ | O(n) / O(1) | Two-pointer swap correct cold. Slipped on `==` vs `=` and type-hint order (`arr: list`, not `list: arr`) — syntax, not logic. |
| 2026-09-17 | character_hashing | Step 1 | ⭐ | O(n) build / O(1) query, O(1) space | Logic correct throughout. Syntax slips: `str` not `string`/`char`, `ord()` for char→index, `[]` not `()` for list indexing. Nailed build-vs-query time split. |

---

## Re-solve queue (redo these cold)

Problems marked 🔁 or ❌ land here until I clear them cold.

- [ ] character_hashing / hash_map — next session's warm-up

---

## Quick reference — Big-O (my cheat corner)

| Notation | Name | Means |
|----------|------|-------|
| O(1) | constant | Extra memory/time never grows with input size |
| O(log n) | logarithmic | Halves the problem each step (binary search) |
| O(n) | linear | Grows in step with input |
| O(n log n) | linearithmic | Good sorting (merge, quick avg) |
| O(n²) | quadratic | Nested loops over the input — avoid when possible |
