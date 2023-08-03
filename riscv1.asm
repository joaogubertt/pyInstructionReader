.text

addi a0, zero, 10
addi a1, zero, 7

bne a0, a1, not_equal

equal:
	add a2, a0, a1
	j final
not_equal:
	mul a2, a0, a1
final:
