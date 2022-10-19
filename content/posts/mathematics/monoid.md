---
title: "Serge Lang Algebra: Groups: Monoid"
date: 20x22-10-09T21:00:26+08:00
draft: true
math: true
---

## Definition of Monoid 1.1

### Law of Composition 1.1.1

Let $S$ be a set. A mapping $S \times S \to S$ is a **law of composition**. If $x, y \in S$, the *image* of the pair $(x, y)$ is a **product** denoted $xy$.

### Equipment of Monoid 1.1.2

Let $G$ be a monoid. It is equipped with an **associative** law of composition with **identity element**:

1. Associativity: $\forall x, y, z \in G$, $(xy)z = x(yz) = xyz$ 1.1.2.1
2. Identity element: $\exists! e \in G$ such that $\forall x \in G$, $ex = xe = x$ 1.1.2.2

#### Uniqueness of Identity Element 1.1.3

Let $G$ be a monoid. Let $e \in G$ be the identity element. Suppose $e^\prime$ is another identity element. By 1.1.2.2, the definition of the identity element, $ee^\prime = e^\prime = e$. Therefore $e = e^\prime$ and $e$ is unique.

#### Definition of Product of Elements of Monoid 1.1.4

Let $G$ be a monoid, and $x_1, \dots, x_n \in G$ where $n \geq 0$, the product of them is defined inductively:

$$
\prod_{v = 1}^{0} x_v = e;
$$

where $e$ is the identity element and 

$$
\prod_{v = 1}^{n} x_v = (\prod_{v = 1}^{n - 1} x_v)x_n
$$

#### Rule of Product of Elements of Monoid 1.1.5

Let $G$ be a monoid, and $x_1, \dots, x_m, \dots, x_{m + n} \in G$ where $m + n \geq 0$, we can prove the following rule inductively:

$$
\prod_{\mu = 1}^{m} x_{\mu} \prod_{v = m + 1}^{m + n} x_v = \prod_{v = 1}^{m + n} x_v
$$

We induct on $n$. Base case: $n = 0$.

$$
\prod_{\mu = 1}^{m} x_{\mu} \prod_{v = m + 1}^{m} x_v = (\prod_{\mu = 1}^{m} x_{\mu})e = \prod_{v = 1}^{m} x_v
$$

by 1.1.4 the definition of the product of elements of monoid and 1.1.2.2 the definition of an identity element.

Induction step: assume that:

$$
\prod_{\mu = 1}^{m} x_{\mu} \prod_{v = m + 1}^{m + n} x_v = \prod_{v = 1}^{m + n} x_v
$$

By 1.1.4 and the assumption:

$$
\prod_{\mu = 1}^{m} x_{\mu} \prod_{v = m + 1}^{m + n + 1} x_v = (\prod_{\mu = 1}^{m} x_{\mu} \prod_{v = m + 1}^{m + n} x_v)x_{m + n + 1} =  (\prod_{v = 1}^{m + n} x_v)x_{m + n + 1} = \prod_{v = 1}^{m + n + 1} x_v
$$

Therefore, the rule is justified.

