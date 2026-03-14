def sort(width: int, height: int, length: int, mass: int) -> str:
    """
    Classify a package as Bulky, Heavy, Both, or Neither based on:
      - Volume threshold
      - Dimension threshold
      - Mass threshold
    """

    # Compute volume
    volume = width * height * length

    # Bulky rules
    bulky = (
        volume >= 1_000_000 or
        width >= 150 or
        height >= 150 or
        length >= 150
    )

    # Heavy rule
    heavy = mass >= 20

    # Classification logic
    if bulky and heavy:
        return "Both"
    elif bulky:
        return "Bulky"
    elif heavy:
        return "Heavy"
    else:
        return "Neither"
