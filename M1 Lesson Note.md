# Solutions and Explanations: Data Structures and Algorithms

This document contains solutions and detailed explanations for three distinct problems covering stack operations, combinatorics with constraints, and circular queue operations.

---

## 1. The Stack TMA: LIFO Principle

**Problem Description:**
Given a stack `S` that has undergone three push operations resulting in the state containing elements A, B, and C (with C at the top), determine the state of the stack after an `S.POP()` operation is executed.

### Explanation

A stack is a linear data structure that follows the **LIFO (Last-In, First-Out)** principle. This means the very last element added to the stack is the first one that will be removed.

1.  **Current State:** The stack has 'C' at the top (last element pushed), 'B' below it, and 'A' at the bottom.
2.  **The Operation:** `S.POP()` removes the element currently at the top of the stack.
3.  **The Result:** 'C' is removed. The element immediately below it, 'B', becomes the new top of the stack.

### Diagram Illustration

**State BEFORE `S.POP()`**
(As shown in the problem description)
```text
+---+
| C | <-- Top
+---+
| B |
+---+
| A |
+---+
```


---

**State AFTER S.POP()** (C is removed, B becomes the new Top)
```
+---+
|   |
+---+
| B | <-- New Top
+---+
| A |
+---+
```
The stack now contains only two elements: **A** at the 
bottom and **B** at the top.

---

## 2. The 77-Digit Integer Problem

**Problem Description:**
There are $N$ integers with 77 digits such that the sum of any three consecutive digits within the integer is at most 7. Find $N$ and input the last three digits as your answer.

### Solution and Explanation

This is a combinatorial problem constrained by local conditions extended over a long sequence. We solve this using **Matrix Exponentiation** to handle the large number of digits efficiently.

#### 1. Analyzing Constraints
Let the integer be represented by digits $d_1 d_2 d_3 ... d_{77}$.
* **Constraint A:** The integer has 77 digits, so the leading digit cannot be 0 ($d_1 \in \{1, ..., 9\}$).
* **Constraint B:** The sum of any three consecutive digits is at most 7 ($d_i + d_{i+1} + d_{i+2} \le 7$).
* **Derived Constraint:** Since digits are non-negative, if the sum of three digits is $\le 7$, no single digit can be greater than 7. Therefore, all digits $d_i \in \{0, 1, 2, 3, 4, 5, 6, 7\}$.

#### 2. Defining States
To ensure the condition $d_i + d_{i+1} + d_{i+2} \le 7$ is met when adding a new digit $d_{i+2}$, we strictly track the sum of the previous two digits $(d_i, d_{i+1})$.
* We define a "state" as the pair of the last two digits added: $(u, v)$.
* A state is valid only if $u + v \le 7$. If $u+v > 7$, it is impossible to add a next non-negative digit $w$ such that the sum is $\le 7$.

#### 3. Calculation Method
* We construct an adjacency matrix $M$ where $M_{ij} = 1$ if a transition from pair $(u, v)$ to $(v, w)$ is valid (i.e., $u+v+w \le 7$).
* We start with 2 digits and need to reach 77 digits (75 transitions).
* We compute the total paths of length 75 using matrix exponentiation ($M^{75}$).

#### 4. Final Answer
After performing the calculation (modulo 1000), the last three digits of $N$ are:
**718**

---

## 3. Explanation of Circular Queue Operations

The image below illustrates a sequence of operations on a Queue data structure implemented using a fixed-size array.

### Detailed Walkthrough

A Queue works on the **FIFO (First-In, First-Out)** principle: items are added to the back (Tail) and removed from the front (Head). This specific implementation is a **Circular Queue**, meaning when the Tail pointer reaches the end of the array, it wraps around to the beginning if space is available.

* **Head Pointer:** Indicates the index of the front element (the next one to be removed).
* **Tail Pointer:** Indicates the index where the next element will be inserted (or the last element inserted, depending on specific implementation nuance—here it tracks insertion).

**Step-by-Step Analysis:**

* **`Add(A, Q)`, `Add(D, Q)`, `Add(Z, Q)`**
    * The queue starts empty. 'A', 'D', and 'Z' are added sequentially.
    * **State:** `[A, D, Z, _, _]`, Head: 0, Tail: 2 (pointing to last element).

* **`RemoveQ()`**
    * The FIFO principle applies. The element at the Head index (0), 'A', is removed.
    * The Head pointer advances to index 1.
    * **State:** `[_, D, Z, _, _]`, Head: 1.

* **`Add(X, Q)`, `Add(C, Q)`**
    * 'X' and 'C' are added to the next available slots.
    * The array is now physically full at the back end.
    * **State:** `[_, D, Z, X, C]`, Tail: 4.

* **`Remove(Q)`**
    * The element at current Head (index 1), 'D', is removed.
    * The Head pointer advances to index 2.
    * **State:** `[_, _, Z, X, C]`, Head: 2.

* **`Add(F, Q)` - (The Circular Step)**
    * We attempt to add 'F'. The Tail is currently at index 4 (end of array).
    * Because it is a Circular Queue, the logic checks the beginning of the array. Since index 0 is empty (from the earlier removal of 'A'), the pointer wraps around.
    * 'F' is inserted at index 0.
    * **State:** `[F, _, Z, X, C]`, Head: 2, Tail: 0.

* **`Remove(Q)`**
    * The element at current Head (index 2), 'Z', is removed.
    * The Head pointer advances to index 3.
    * **Final State:** `[F, _, _, X, C]`, Head: 3, Tail: 0.