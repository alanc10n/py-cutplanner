py-cutplanner
=============

**Status: Work in progress, currently unusable**

This module is intended to generate cut lists for relatively small projects, such as installing baseboard trim in a home. Given a list of required piece lengths and a list of available stock, the problem is to determine how to cut those pieces from the stock while minimizing waste.

This is of course a variation of the Cutting Stock Problem and is related to the Bin Packing Problem. These are NP-Hard, so optimal solutions in general aren't practical to obtain. Given the intended applications, relatively good approximations are fine and optimal solutions are possible.

In addition to being a practical tool I'll use for my own home improvement projects, this is also intended as a programming exercise and playground. I'll likely implement a number of different algorithms for solving this problem, and also probably build some tools to make it usable.
