# Technical-screen
# Package Sorter – Technical Screen Solution

This project implements a package classification function used to determine how a robotic arm should sort incoming packages. The classification is based on the package's **dimensions**, **volume**, and **mass**.

## Classification Rules

A package is considered **bulky** if:

- Its volume (width × height × length) is **≥ 1,000,000 cm³**, **OR**
- Any of its dimensions is **≥ 150 cm**

A package is considered **heavy** if:

- Its mass is **≥ 20 kg**

## Return Values

The function returns one of four classifications:

- `"Both"` – if the package is both bulky and heavy  
- `"Bulky"` – if the package is bulky only  
- `"Heavy"` – if the package is heavy only  
- `"Neither"` – if it is neither bulky nor heavy  

## Function Signature

```python
sort(width: int, height: int, length: int, mass: int) -> str
