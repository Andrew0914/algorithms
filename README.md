# Interview Prep Guide

A structured approach to solving coding problems consistently — even when the solution is simple but your brain feels stuck.

---

## Why You Get Stuck (Even on Easy Problems)

Getting stuck is rarely about intelligence. It usually happens because:

- You jump straight into coding without a plan.
- You try to hold the entire problem in your head instead of writing things down.
- You freeze when the first idea doesn't work, instead of iterating.
- You confuse "I don't see the answer instantly" with "I can't solve this."

The fix is **a repeatable process**, not more talent.

---

## Before You Start a Problem

### 1. Read the problem twice

First read: understand _what_ is being asked. Second read: catch constraints, edge cases, and input/output format.

### 2. Restate it in your own words

Write a one-sentence summary. If you can't explain the problem simply, you don't understand it yet.

### 3. Clarify constraints

Ask yourself (or the interviewer):

- What is the input size? (This hints at the expected time complexity)
- Can the input be empty? Negative? Duplicates?
- Is the input sorted? Can I modify it in place?
- What should I return if there's no valid answer?

### 4. Work through 1-2 examples

Pick a simple case and an edge case. Write down the input, what the expected output is, and _why_ that's the answer. The _why_ is what matters — it forces you to reason about the problem and naturally leads you toward the right approach.

> **Example — "Given a linked list, determine if it has a cycle."**
>
> | Case      | Input                                | Output  | Why                                                         |
> | --------- | ------------------------------------ | ------- | ----------------------------------------------------------- |
> | Simple    | `1 -> 2 -> 3 -> 4 -> None`           | `False` | The list ends at `None`, no cycle                           |
> | Has cycle | `1 -> 2 -> 3 -> 4 -> back to node 2` | `True`  | Node 4's next points to node 2, so traversing loops forever |
> | Edge case | `None` (empty list)                  | `False` | No nodes, no cycle                                          |
>
> Notice how writing _"traversing loops forever"_ already makes you think: _how would I detect that?_ — and that leads you to the fast/slow pointer pattern in step 5.

### 5. Identify the pattern before writing code

Match the problem to a known pattern:

| Pattern            | Signals                                                                                          | Classic LeetCode Problems                                              |
| ------------------ | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| Two pointers       | Sorted array, find a pair, compare from both ends, palindrome, remove duplicates in place        | Two Sum, 3Sum, Container With Most Water, Valid Palindrome             |
| Sliding window     | Subarray/substring with a condition, max/min of contiguous elements, "at most K" constraint      | Longest Substring Without Repeating Characters, Minimum Window Substring, Max Consecutive Ones III |
| Stack              | Matching brackets, nesting depth, next greater/smaller element, undo operations, monotonic order | Valid Parentheses, Daily Temperatures, Min Stack, Largest Rectangle in Histogram |
| Queue / BFS        | Level-order traversal, shortest path in unweighted graph, process layer by layer                 | Binary Tree Level Order Traversal, Rotting Oranges, Word Ladder        |
| Binary search      | Sorted input, "find min/max that satisfies", search space can be halved, answer in a range       | Search in Rotated Sorted Array, Find Minimum in Rotated Sorted Array, Koko Eating Bananas |
| Recursion / DFS    | Tree traversal, graph exploration, generate all subsets/permutations, "return all possible"      | Maximum Depth of Binary Tree, Symmetric Tree, Subsets, Number of Islands |
| Linked list tricks | Reverse a list, detect cycle, find middle, merge two lists, fast/slow pointer                    | Reverse Linked List, Linked List Cycle, Merge Two Sorted Lists, Reorder List |
| Divide & conquer   | Split problem in halves, merge sorted results, tree construction from traversal                  | Merge Sort, Sort an Array, Construct Binary Tree from Preorder and Inorder |
| Bit manipulation   | XOR to find unique, check powers of 2, count bits, binary representation                        | Single Number, Number of 1 Bits, Add Binary, Power of Two              |
| Hash map           | Count frequencies, find duplicates, group elements, O(1) lookup to replace nested loop           | Two Sum, Group Anagrams, Top K Frequent Elements, Contains Duplicate   |
| Dynamic programming| Overlapping subproblems, optimal substructure, "min/max cost", "number of ways"                  | Climbing Stairs, Coin Change, Longest Common Subsequence, House Robber |
| Heap               | "K largest/smallest", merge K sorted things, running median, schedule by priority                | Kth Largest Element, Merge K Sorted Lists, Find Median from Data Stream |

If you can't identify the pattern, that's fine — move to brute force first.

---

## During the Problem

### 6. Pick your approach

If you recognized the pattern in step 5, go directly with the right tool — you've studied these data structures and algorithms, use that knowledge. No need to force a brute force solution when you already know a hash map or two pointers is the way.

If you _can't_ identify the pattern, then fall back to brute force. A slow working solution is still better than nothing, and it often reveals the optimization path.

### 7. Write pseudocode before code

3-5 lines of plain English. This is your outline. It prevents you from getting lost in syntax while still thinking about logic.

```
# for each element
#   check if complement exists in hash map
#   if yes, return indices
#   if no, add current to hash map
```

### 8. Code it up, one piece at a time

- Write the skeleton first (function signature, return statement).
- Fill in the main logic.
- Handle edge cases last.

### 9. When you feel stuck mid-problem

**Stop coding. Go back to an example.** Trace through your current code with a specific input. The bug or the missing insight will usually show up.

Other unblocking strategies:

- Simplify the problem (solve for n=1, then n=2, then generalize).
- Think about what data structure would make the hard part easy.
- Draw it: arrays as boxes, trees as nodes, graphs as circles with arrows.

---

## After You Solve It

### 10. Test with edge cases

Always check:

- Empty input (`[]`, `""`, `None`)
- Single element
- All same elements
- Already sorted / reverse sorted
- Very large input (does your complexity hold?)

### 11. Analyze time and space complexity

State both. Practice saying: _"This is O(n) time and O(1) space because..."_

### 12. Review and reflect (most people skip this)

After solving, spend 2 minutes answering:

- What pattern did this use?
- Where did I get stuck and why?
- What would I do differently next time?
- Can I solve it a different way?

Write a short comment at the top of your file:

```python
# Pattern: hash map lookup
# Complexity: O(n) time, O(n) space
# Lesson: when looking for pairs, think hash map before nested loop
```

### 13. Revisit problems that were hard

Use spaced repetition:

- Solve again after 1 day
- Solve again after 1 week
- If it's still hard, solve again after 2 weeks

If you solved it easily the second time, you actually learned it. If not, repeat.

---

## Daily Practice Structure

```
1. Warm-up (5 min)    — Re-solve a problem you did last week from memory
2. New problem (25 min) — Follow the full process above
3. Review (5 min)      — Write your reflection comment
```

Consistency beats volume. One problem per day with full reflection is better than five problems with no review.

---

## Common Mistakes to Avoid

| Mistake                                    | Fix                                                       |
| ------------------------------------------ | --------------------------------------------------------- |
| Jumping straight to code                   | Write pseudocode first                                    |
| Not recognizing the pattern first          | Identify the pattern, then pick the right tool directly   |
| Not testing edge cases                     | Keep a mental checklist (empty, single, duplicates)       |
| Spending 40+ minutes stuck on one approach | After 15 min stuck, step back and try a different pattern |
| Only solving, never reviewing              | The reflection step is where learning happens             |
| Memorizing solutions                       | Understand the _why_ — the pattern, not the code          |

---

_The goal is not to solve every problem — it's to build a process you trust so that when you sit down in the interview, you know exactly how to start._
