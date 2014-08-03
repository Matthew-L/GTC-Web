def calculate_tension(scale_length, frequency, unit_weight):
    """
    Method of tension calculation provided by D'Addario
    @return: the calculated tension using  (UnitWeight x (2 x ScaleLength x Frequency)^2)/TensionConstant
    """
    tension_constant = 386.4
    tension = (unit_weight * (2 * scale_length * frequency) ** 2) / tension_constant
    return tension