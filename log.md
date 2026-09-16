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

---

## Re-solve queue (redo these cold)

Problems marked 🔁 or ❌ land here until I clear them cold.

- [ ] reverse_array — recovered from blank, re-solve to confirm
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
