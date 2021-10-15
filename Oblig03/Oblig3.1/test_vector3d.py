from vector3d import Vector3D

def test_constructor():
    v = Vector3D(1, 2, 3)
    assert type(v) == Vector3D
    assert v.x == 1
    assert v.y == 2
    assert v.z == 3

def test_addition():
    v1 = Vector3D(1,2,3)
    v2 = Vector3D(5,7,3)
    v3 = v1 + v2
    assert v3.x == 6
    assert v3.y == 9
    assert v3.z == 6

def test_subtraction():
    v1 = Vector3D(5,6,2)
    v2 = Vector3D(2,5,10)
    v3 = v1 - v2
    assert v3.x == 3
    assert v3.y == 1
    assert v3.z == -8

def test_multiplication():
    v1 = Vector3D(2,2,2)
    v2 = Vector3D(4,2,1)
    v3 = v1 * v2
    assert v3.x == 8
    assert v3.y == 4
    assert v3.z == 2

def test_equality():
    v1 = Vector3D(1,2,3)
    v2 = Vector3D(1,2,3)
    assert v1 == v2

def test_string():
    v1 = Vector3D(1,2,3)
    assert str(v1) == "[1,2,3]"

def test_repr():
    v1 = Vector3D(1,2,3)
    assert repr(v1) == "Vector3D(1,2,3)"

def test_length():
    v1 = Vector3D(10,0,0)
    assert v1.length() == 10
    v2 = Vector3D(2,2,2)
    # Tolerance used due to floating point
    assert v2.length() > 3.46 and v2.length() < 3.47

def test_dot():
    v1 = Vector3D(3,2,5)
    v2 = Vector3D(7,2,1)
    dot = v1.dot(v2)
    assert dot == 30

def test_cross():
    v1 = Vector3D(1,2,3)
    v2 = Vector3D(5,4,3)
    v3 = v1.cross(v2)
    assert v3.x == -6
    assert v3.y == 12
    assert v3.z == -6
