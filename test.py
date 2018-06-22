import pytest
from hypothesis import given
import hypothesis.strategies as st
from main import compose_dict

def test_default():
    keys = ['1', '2', '3', '4', '5']
    values = ['M', 'A', 'S', 'H', 'A']
    expected = { '1': 'M', '2': 'A', '3': 'S', '4': 'H', '5': 'A' }

    assert compose_dict(keys, values) == expected

def test_fill_none():
    keys = ['1', '2', '3', '4', '5', '6']
    values = ['M', 'A', 'S', 'H', 'A']
    expected = { '1': 'M', '2': 'A', '3': 'S', '4': 'H', '5': 'A', '6':None }

    assert compose_dict(keys, values) == expected

@pytest.mark.parametrize('keys, values', [
    (['1'], 'MASHA'),
    ('2', ['QWER'])
])
def test_check_types(keys, values):
    with pytest.raises(TypeError):
        compose_dict(keys, values)

@given(st.lists(st.text()))
def test_skip_values(extra_values):
    keys = ['1', '2', '3', '4', '5']
    values = ['M', 'A', 'S', 'H', 'A']
    expected = { '1': 'M', '2': 'A', '3': 'S', '4': 'H', '5': 'A' }

    assert compose_dict(keys, values) == expected

