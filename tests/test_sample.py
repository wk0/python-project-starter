from app.sample.sample import Sample
from .context import sample


def test_sample_class_init():
    sample_var = "sample_var"
    s = sample.Sample(sample_var=sample_var)

    assert s.sample_var == sample_var


def test_sample_func():
    sample_var = "sample_var"
    s = sample.Sample(sample_var=sample_var)

    s.sample_func(sample_item="x")
    s.sample_func(sample_item="y")
    s.sample_func(sample_item="z")

    assert s.sample_list == ["x", "y", "z"]
