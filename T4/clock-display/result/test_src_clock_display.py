# Automatically generated by Pynguin.
import src.clock_display as module_0


def test_case_0():
    bytes_0 = b'\x9c\x13\x1c\x83E\xf6\x8a\xc3\xdfSE^\x0b\x92'
    clock_display_0 = module_0.ClockDisplay(bytes_0)
    assert len(clock_display_0.numbers) == 14
    var_0 = clock_display_0.increment()
    assert var_0 == 13


def test_case_1():
    bytes_0 = b'\xdd(\x10fj\x14\x81\x10\x83.'
    clock_display_0 = module_0.ClockDisplay(bytes_0)
    assert len(clock_display_0.numbers) == 10
    var_0 = clock_display_0.invariant()


def test_case_2():
    str_0 = '0'
    clock_display_0 = module_0.ClockDisplay(str_0)
    assert len(clock_display_0.numbers) == 1
    var_0 = clock_display_0.clone()
    assert len(var_0.numbers) == 1
