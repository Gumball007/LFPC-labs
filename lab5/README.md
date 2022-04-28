# LL1 and Simple precedence parsing

## Variant 5

## Tasks:

For the given grammar

```
G = (VN, VT, P, S) VN = {S, A, B, C, D} VT = {a, b, c, d, e}
P = {
    1. S -> Ae       
    2. A -> baB          
    3. B -> Cd          
    4. C -> D   
    5. C -> CbD
    5. D -> c
}
implement algorithm of simple precedence parsing and analyze the `bacbcbcde`
Bonus point: provide as an additional output the derivation tree. 
```
