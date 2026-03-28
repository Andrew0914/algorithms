# Mistakes Log

Track mistakes per problem to find patterns in what trips you up.

---

## Template

Copy this for each new entry:

```
### Problem — [problem name]

**Date:** YYYY-MM-DD
**Pattern:** (e.g., two pointers, BFS, dynamic programming)
**Difficulty:** Easy / Medium / Hard

**What went wrong:**
- (Describe where you got stuck or what you did incorrectly)

**Why it happened:**
- (Root cause — did you misread the problem? Pick the wrong pattern? Forget an edge case?)

**What I should have done:**
- (The correct approach or thinking process)

**Tags:** #tag1 #tag2
```

Use tags to categorize your mistakes so you can search for recurring ones later. Suggested tags:

- `#misread-problem` — Missed a constraint or misunderstood the ask
- `#wrong-pattern` — Picked the wrong data structure or algorithm
- `#edge-case` — Solution worked but failed on edge cases
- `#off-by-one` — Index or boundary errors
- `#overcomplicated` — Made it harder than it needed to be
- `#froze` — Knew the tools but couldn't start
- `#time-complexity` — Solution was too slow
- `#syntax` — Knew the logic but struggled with implementation

---

## Log

<!-- Paste new entries below, most recent first -->

### Problem — Convert Sorted Array to BST

**Date:** 2026-03-22
**Pattern:** DFS, Recursion
**Difficulty:** Easy

**What went wrong:**
- Solution was almost correct but didn't produce a height-balanced BST. Picked the middle as root but then inserted remaining elements one by one, which created unbalanced subtrees.

**Why it happened:**
- Didn't fully understand what a balanced BST is — the left and right subtrees of every node must differ in height by at most 1.

**What I should have done:**
- Review what a balanced tree looks like before coding. The correct approach is to recursively pick the middle of each subarray as the subtree root, not just the middle of the full array.

**Tags:** #misread-problem

### Problem — Add Binary

**Date:** 2026-03-21
**Pattern:** Two pointers (same direction)
**Difficulty:** Easy

**What went wrong:**
- Got stuck handling the carry by comparing possible combinations of 0 and 1 manually, resulting in an overcomplicated solution

**Why it happened:**
- Jumped straight into coding without thinking through the approach first

**What I should have done:**
- Pause and think before coding. Use `%` and `//` operators to handle carry and digit sum cleanly (e.g., `carry, digit = divmod(sum, 2)`)

**Tags:** #overcomplicated
