# Automatically generated by Pynguin.
import src.clock_factory as module_0


def test_case_0():
    try:
        bool_0 = False
        clock_factory_0 = module_0.ClockFactory()
        assert len(clock_factory_0.cache) == 3
        var_0 = clock_factory_0.create(bool_0)
    except BaseException:
        pass
