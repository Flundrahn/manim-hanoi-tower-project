# Tower of Hanoi Puzzle Project
A visualization of the Tower of Hanoi Puzzle. 
Invented by French mathematician Édouard Lucas in the 19th century.

The objective of the puzzle is to move an entire stack
of discs to the last rod, obeying the following rules:
1. Only one disk may be moved at a time.
2. Only the disk at the top of a stack may be moved.
3. No disk may be placed on top of a smaller disc.

The puzzle can be solved using an elegant recursive algorithm:

```python
def hanoi_algorithm(n_discs, A, B, C):
    if n_discs > 0:
        hanoi_algorithm(n_discs-1, A, C, B)
        move_disc(from = A, to = C)
        hanoi_algorithm(n_discs-1, B, A, C)
```

Inspired by the following Numberphile videos:

- https://www.youtube.com/watch?v=8lhxIOAfDss
- https://www.youtube.com/watch?v=PGuRmqpr6Oo

Resulting video:
- https://www.youtube.com/watch?v=8XQmuPKOgy8

Made with [ManimCE](https://www.manim.community/) in Python by Fredrik Lundström February 2022

## Screenshots
[![Tower of Hanoi video screenshot](/Screenshot_2022-02-26.png)](https://www.youtube.com/watch?v=8XQmuPKOgy8)