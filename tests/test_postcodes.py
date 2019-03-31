from uk_postcodes.postcodes import format_postcode, deep_validaion, load_postcodes
import pytest
import sys
import os
sys.path.insert(1, os.getcwd())

demo_code = [
    'BA1 0GL'
]

valid_values = ['BA10GL','B11DD', 'CH11DQ', 'G1 1DW']

invalid_values = ['V25 1PT', 'AI2 9AA', 'BA4 0MO']

load_postcodes() # load the postcodes.pkl file first


@pytest.fixture(params=demo_code)
def demo_code(request):
    return request.param


@pytest.fixture(params=valid_values)
def valid_code(request):
    return request.param


@pytest.fixture(params=invalid_values)
def invalid_code(request):
    return request.param


#  Test functions
def test_format_code(demo_code):
    code = format_postcode(demo_code)
    assert code == 'BA10GL'


def test_deep_validate_code(valid_code):
    dv = deep_validaion(valid_code)
    assert dv == True, 'These codes are not valid codes'


def test_deep_invalidate_code(invalid_code):
    div = deep_validaion(invalid_code)
    assert div == False, 'These codes are not invalid codes'