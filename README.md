# DSA Interview Prep Framework

A battle-tested system for solving coding problems under pressure. Not a collection of tips — a repeatable decision-making process.

---

## The Core Loop

Every problem follows the same loop. Internalize this until it's automatic:

```
UNDERSTAND --> PLAN --> IMPLEMENT --> VERIFY --> OPTIMIZE
     ^                                             |
     |_____________________________________________|
              (repeat if needed)
```

Each phase has a specific job. Skipping a phase is how you get stuck.

---

## Phase 1: UNDERSTAND (2-3 min)

Your only goal here is to **eliminate ambiguity**. You should not be thinking about solutions yet.

### 1.1 Read for structure, then for detail

- **First pass**: What are the inputs? What is the output? What transformation connects them?
- **Second pass**: Constraints, edge cases, gotchas hiding in the wording.

### 1.2 Restate the problem in one sentence

If you can't, you don't understand it yet. Force yourself:

> "Given X, find/return/compute Y such that Z."

This sentence is also exactly how you'd open in an interview.

### 1.3 Constrain the solution space

**This is the single most important skill most people never develop.** The constraints _tell you_ what complexity is expected:

| Input size (n)     | Target complexity   | What this rules out              |
|--------------------|---------------------|----------------------------------|
| n <= 10            | O(n!) or O(2^n)     | Nothing — brute force is fine    |
| n <= 20            | O(2^n)              | Must be exponential or better    |
| n <= 500           | O(n^3)              | Nested triple loops are ok       |
| n <= 10,000        | O(n^2)              | No cubic solutions               |
| n <= 1,000,000     | O(n) or O(n log n)  | No quadratic solutions           |
| n <= 100,000,000   | O(n) or O(log n)    | Must be linear or sub-linear     |

Before you think about _how_ to solve it, you already know _how fast_ your solution needs to be.

### 1.4 Clarify with questions

In interviews, asking good questions shows maturity. Always ask:

- Can the input be empty? Contain negatives? Have duplicates?
- Is the input sorted or can I sort it?
- Should I optimize for time or space?
- Can I modify the input in place?
- Is there guaranteed to be a valid answer?

### 1.5 Trace 2-3 examples by hand

Pick deliberately:

| Example type | Purpose                                      |
|-------------|-----------------------------------------------|
| Happy path  | Verify your understanding of the core task     |
| Small input | n=1 or n=2 — reveals base cases               |
| Edge case   | Empty, all same, duplicates, negative, max size|

**Write down intermediate states, not just input/output.** The intermediate states reveal the algorithm.

> **Example — "Find two numbers in an array that sum to target"**
>
> ```
> Input: [2, 7, 11, 15], target = 9
>
> Step through:
>   i=0: value=2, need 9-2=7, seen={}          --> 7 not in seen, add 2
>   i=1: value=7, need 9-7=2, seen={2:0}       --> 2 IS in seen at index 0!
>   Return [0, 1]
> ```
>
> Notice: writing the intermediate state _led_ to the hash map approach naturally.

---

## Phase 2: PLAN (3-5 min)

Now — and only now — think about solutions. This phase has two tracks depending on whether you recognize the problem pattern.

### Track A: You recognize the pattern

Go straight to the right approach. You've studied these patterns; use them.

**Pattern Recognition Decision Tree:**

```
Is it asking about subarrays/substrings with a condition?
  --> Sliding Window

Is the input sorted, or could sorting help?
  --> Two Pointers / Binary Search

Do I need O(1) lookup or frequency counting?
  --> Hash Map / Hash Set

Is it "find all combinations/permutations/subsets"?
  --> Backtracking

Does it involve a tree or graph traversal?
  --> DFS (recursion/stack) or BFS (queue)

Is it "find min/max/count of ways" with overlapping choices?
  --> Dynamic Programming

Is it "K largest/smallest" or "merge K sorted"?
  --> Heap

Is it "next greater/smaller element" or nested intervals?
  --> Monotonic Stack

Is it about matching/nesting/undo?
  --> Stack

Does it involve connected components or shortest path?
  --> Graph (BFS for shortest, DFS/Union-Find for components)
```

### Track B: You don't recognize the pattern

**Don't panic.** Follow this escalation:

1. **Brute force first.** What's the simplest, most naive way to solve this? Even O(n^3) is fine as a starting point. Name it, state its complexity.

2. **Identify the bottleneck.** What's the expensive part? Usually it's a nested loop or repeated search.

3. **Eliminate the bottleneck.** Ask: _"What data structure would make the slow part fast?"_
   - Repeated search? --> Hash map (O(1) lookup)
   - Finding min/max repeatedly? --> Heap or monotonic structure
   - Recomputing overlapping work? --> DP / memoization / prefix sum

4. **Check against constraint.** Does your improved approach hit the target complexity from Phase 1? If yes, go. If no, repeat.

### 2.1 State your approach out loud

In an interview, say:

> "My approach is to use [technique] because [reason]. This will be O(X) time and O(Y) space. Before I code, does that sound reasonable?"

This does three things: confirms alignment with the interviewer, demonstrates structured thinking, and gives you a verbal outline to follow.

### 2.2 Write pseudocode (3-5 lines max)

```
# build frequency map of characters in target
# expand window: move right pointer, update counts
# when window contains all target chars, shrink from left
# track minimum valid window seen
```

This is your contract. Code should follow this structure exactly.

---

## Phase 3: IMPLEMENT (10-15 min)

### 3.1 Skeleton first

Write the function signature, initialize your data structures, and write the return statement. Now you have a frame to fill in.

```python
def two_sum(nums, target):
    seen = {}

    # main logic goes here

    return []
```

### 3.2 Fill in the logic from your pseudocode

Translate each pseudocode line to code, one at a time. Don't jump ahead.

### 3.3 Code habits that prevent bugs

- **Name variables clearly.** `left`, `right`, `count`, `result` — not `i`, `j`, `c`, `r`.
- **Get loop boundaries right the first time.** Think: does this need `<` or `<=`? Does `right` start at 0 or 1?
- **Handle the base case explicitly** at the top of the function, not buried in logic.
- **Don't clever-code.** In interviews, readable beats clever every time.

### 3.4 When you're stuck mid-implementation

**Stop typing. Go back to a concrete example.** Trace your current code with a specific input, line by line. The bug reveals itself.

Other unblocking moves:
- Solve the smallest version first (n=1, n=2), then generalize
- Draw the data structure's state at each step
- Ask: "What information do I need that I don't currently have?"

---

## Phase 4: VERIFY (2-3 min)

### 4.1 Trace through your code with an example

Don't just re-read the code — execute it mentally with a specific input. Track every variable's value. This catches off-by-one errors and wrong conditions.

### 4.2 Test edge cases

Your go-to checklist:

```
[ ] Empty input ([], "", None, 0)
[ ] Single element
[ ] Two elements (minimum for "pair" problems)
[ ] All identical elements
[ ] Already sorted / reverse sorted
[ ] Negative numbers (if applicable)
[ ] Answer doesn't exist (return default)
[ ] Maximum input size (does complexity hold?)
```

### 4.3 Check for common bugs

- Off-by-one in loop bounds
- Returning the wrong thing (index vs value, list vs single element)
- Not handling the "not found" case
- Integer overflow (mostly Java/C++)
- Mutating input when you shouldn't be

---

## Phase 5: OPTIMIZE (only if needed)

Only enter this phase if:
- Your solution works but doesn't meet the target complexity
- The interviewer asks "can you do better?"

### Optimization strategies in order of impact

1. **Eliminate redundant work** — Are you computing the same thing twice? Cache it (hash map, memo table, prefix sum).
2. **Trade space for time** — A hash set/map often eliminates an inner loop.
3. **Change traversal order** — Sometimes processing right-to-left or bottom-up unlocks a simpler solution.
4. **Use a smarter data structure** — Heap for top-K, trie for prefix search, monotonic stack for next-greater.
5. **Reduce the search space** — Binary search on the answer, two pointers on sorted input.

---

## Pattern Reference

Quick reference for the core patterns. Know when to reach for each tool.

| Pattern | Key Signal | Core Idea | Typical Complexity |
|---|---|---|---|
| Two Pointers | Sorted input, pairs, palindrome | Pointers moving inward or same direction | O(n) |
| Sliding Window | Contiguous subarray/substring with constraint | Expand right, shrink left, track window state | O(n) |
| Binary Search | Sorted data, "min that satisfies" | Halve search space each step | O(log n) |
| Hash Map | Frequency, pairs, grouping, O(1) lookup | Trade O(n) space for O(1) access | O(n) / O(n) |
| Stack | Matching pairs, nesting, next greater/smaller | LIFO for tracking open/pending items | O(n) |
| BFS | Shortest path (unweighted), level-order | Queue-based layer-by-layer exploration | O(V+E) |
| DFS | Tree/graph traversal, all paths, components | Recursion or explicit stack, go deep first | O(V+E) |
| Backtracking | All combinations/permutations/subsets | Build candidates, prune invalid branches | O(2^n) or O(n!) |
| Dynamic Programming | Overlapping subproblems, optimal substructure | Solve subproblems once, build up to answer | Varies |
| Heap | K largest/smallest, merge K sorted, median | Maintain partial order for efficient min/max | O(n log k) |
| Monotonic Stack | Next greater/smaller, histogram problems | Stack maintains increasing/decreasing order | O(n) |
| Union-Find | Connected components, cycle detection | Group elements, near-O(1) merge and find | O(n * a(n)) |
| Trie | Prefix matching, autocomplete, word search | Tree of characters for prefix operations | O(L) per word |
| Prefix Sum | Range sum queries, subarray sums | Precompute cumulative sums for O(1) range queries | O(n) build, O(1) query |

---

## Interview Communication

Solving the problem is only half the battle. How you communicate matters just as much.

### What interviewers are evaluating

1. **Problem solving process** — Do you have a systematic approach?
2. **Communication** — Can you explain your thinking clearly?
3. **Code quality** — Is your code clean and correct?
4. **Testing mindset** — Do you verify your work?
5. **Collaboration** — Do you respond well to hints?

### Talk track template

```
[UNDERSTAND] "Let me make sure I understand the problem..."
             "A few clarifying questions..."
             "Let me trace through this example..."

[PLAN]       "I'm thinking this is a [pattern] problem because..."
             "My approach would be... which gives us O(X) time, O(Y) space."
             "Does that direction sound good before I start coding?"

[IMPLEMENT]  "I'll start by setting up [structure]..."
             "Now I'll handle the main logic..."
             (narrate at decision points, not every line)

[VERIFY]     "Let me trace through with our example..."
             "Edge case to check: what if the input is empty..."

[OPTIMIZE]   "This works, but if we wanted to optimize..."
             "The bottleneck is [X], and we could improve it by..."
```

### Receiving hints gracefully

- "That's a great point, let me think about that..."
- "Oh I see — so if I [restate hint in your own words]..."
- Never ignore a hint. It's a lifeline, not a penalty.

---

## Deliberate Practice System

### Daily routine (35 min)

```
[5 min]  Re-solve one problem from last week — no looking at notes
[25 min] One new problem using the full framework above
[5 min]  Write reflection (pattern, where you got stuck, lesson)
```

### Reflection template (top of every solution file)

```python
# Pattern: <pattern name>
# Complexity: O(?) time, O(?) space
# Lesson: <the one thing to remember for next time>
```

### Spaced repetition schedule

```
Day 0: Solve the problem
Day 1: Re-solve from scratch
Day 3: Re-solve from scratch
Day 7: Re-solve from scratch
Day 14+: Only if it was still hard at Day 7
```

If you solve it cleanly at Day 3, you've learned it. Move on.

### Weekly review

Once a week, scan your solved problems and ask:
- Which patterns am I comfortable with?
- Which patterns keep tripping me up?
- What's my most common mistake? (Check `MISTAKES_LOG.md`)

Spend the next week's practice on your weak patterns, not your strong ones.

---

## When Things Go Wrong

| Situation | What to do |
|---|---|
| Can't understand the problem | Restate it simpler. Draw a picture. Trace a tiny example. |
| Can't find the pattern | Start with brute force. The bottleneck in brute force often reveals the pattern. |
| Stuck for 5+ minutes on one part | Step back. Re-read the problem. Try a different example. Ask: "What information am I missing?" |
| Code has a bug | Stop guessing. Trace through with a concrete input, tracking every variable. |
| Solution is too slow | Identify the bottleneck operation. What data structure makes that operation cheaper? |
| 15+ minutes with no progress | In practice: look at a hint, learn the pattern, re-solve later. In interview: ask for a nudge. |
| Interviewer gives a hint | Take it. Restate it. Build on it. It's collaboration, not failure. |

---

_The goal isn't to memorize solutions. It's to build a decision-making process you trust — so that under pressure, you know exactly what to do next._
