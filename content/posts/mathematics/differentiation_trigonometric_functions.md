---
title: "Differentiation of Trigonometric Functions"
date: 2022-10-10T11:09:34+08:00
draft: false
math: true
---

## Differentiation of Trigonometric Function

### Limit of $\frac{\sin x}{x}$ and $\frac{1 - \cos x}{x}$ as $x \to 0$

The proofs of $\lim_{x \to 0} \frac{\sin x}{x} = 1$ is obvious by squeeze theorem.

### Derivatives of $\sin x$ and $\cos x$

$$
\frac{d}{d x}(\sin x) = \cos x
$$

$$
\frac{d}{d x}(\cos x) = -\sin x
$$

Proofs:

We prove it from the first principle:

$$
\frac{d}{d x}(\sin x) = \lim_{h \to 0} \frac{\sin (x + h) - \sin x}{h}
$$

By double angle identity, this is equivalent to:

$$
\lim_{h \to 0} \frac{\sin x \cos h + \sin h \cos x - \sin x}{h}
$$

We simplify it with the two previously computed limits:

$$
\lim_{h \to 0} \frac{-\sin x(\cos h - 1)}{h} + \frac{\sin h \cos x}{h}
$$

and therefore equivalent to:

$$
\cos x
$$

The proof for $\frac{d}{dx} \cos x = -\sin x$ is similar.

### Derivatives of other Trigonometric Functions

$$
\frac{d}{dx} \tan x = \frac{d}{dx} (\frac{\sin x}{\cos x}) = 1 + \tan^2 x = sec^
$$
