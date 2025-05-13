# import pytest
from musculoskeletal_system import MusculoskeletalSystem

# Starting tests...
def test_01():
    a = MusculoskeletalSystem(bones=213, skeletal_muscles=650)
    assert a.check_move() == True
  
def test_02():
    a = MusculoskeletalSystem(bones=10, skeletal_muscles=30)
    assert a.check_move() == False
  
def test_03():
    a = MusculoskeletalSystem(bones=206, skeletal_muscles=100)
    assert a.check_move() == False
  
def test_04():
    a = MusculoskeletalSystem(bones=10, skeletal_muscles=600)
    assert a.check_move() == False

def test_05():
    a = MusculoskeletalSystem(bones=206, skeletal_muscles=600)
    assert a.check_move() == True
