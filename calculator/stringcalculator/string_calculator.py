def calculate_tension(length, pitch, string):
    """
    Method of tension calculation provided by D'Addario
    @return: the calculated tension using  (UnitWeight x (2 x ScaleLength x Frequency)^2)/TensionConstant
    """

    tension_constant = 386.4
    tension = (string.unit_weight * (2 * length.scale_length * pitch.frequency) ** 2) / tension_constant
    return tension