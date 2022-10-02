---
title: "Even and Odd Functions"
description: "All properties and theorems regarding even and odd functions"
date: 2022-10-01T22:49:04+08:00
draft: false
math: true
tags: ["function", "calculus"]
---

## Definition of Even and Odd Functions

A function $f$ is even if:

$$
f(x) = f(-x)
$$

and is odd if:

$$
-f(x) = f(-x)
$$

### Properties of Even and Odd Functions

|$\pm$ |Odd | Even|
|----|----|-----|
|Odd| Odd | N/A|
|Even| N/A| Even|

|$\times$| Odd | Even |
|----|----|----|
|Odd| Even | Odd|
|Even| Odd | Even|

### Even Function Odd Derivative; Vice Versa

If a differentiable function $f$ is even, then $\frac{df}{dx}$ is odd; if $f$ is odd, then $\frac{df}{dx}$ is even.

Proof:

Let $f$ be a differentiable function. Suppose $f$ is even, let $y = -x$ such that $f(x) = f(y)$, then:

$$
\frac{df}{dx} = \frac{df}{dy} \times \frac{dy}{dx} = -\frac{df}{dy}
$$

Therefore, $\frac{df}{dx}$ is odd.

Similarly, suppose $f$ is odd, that is, $-f(x) = f(y)$, then:

$$
\frac{df}{dx} = -\frac{df}{dy} \times \frac{dy}{dx} = \frac{df}{dy}
$$

Therefore, $\frac{df}{dx}$ is even.
