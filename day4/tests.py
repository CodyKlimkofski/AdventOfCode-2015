import pytest
import hashlib
from hasher import Hasher

@pytest.fixture(scope="module")
def hasher():
    return Hasher()

def test_md5_hash(hasher):
    assert hasher.md5_hash('a') == hashlib.md5('a'.encode()).hexdigest()
    assert hasher.md5_hash('abc') == hashlib.md5('abc'.encode()).hexdigest()
    assert hasher.md5_hash('hello world') == hashlib.md5('hello world'.encode()).hexdigest()

def test_is_valid_hash(hasher):
    valid_hash = '00000abcdef1234567890'
    invalid_hash = '12345abcdef1234567890'
    
    assert hasher.is_valid_hash(valid_hash) == True
    assert hasher.is_valid_hash(invalid_hash) == False
    assert hasher.is_valid_hash(valid_hash, leading_zeros=6) == False
    assert hasher.is_valid_hash('000000abcdef1234567890', leading_zeros=6) == True