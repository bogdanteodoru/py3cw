import pytest
from .request import Py3CW


def test_error_missing_key():
    with pytest.raises(ValueError) as excinfo:
        assert Py3CW(
            key='',
            secret='secret'
        )
    excinfo.match(r'Missing key')


def test_error_missing_secret():
    with pytest.raises(ValueError) as excinfo:
        assert Py3CW(
            key='key',
            secret=''
        )
    excinfo.match(r'Missing secret')


def test_error_missing_entity():
    p3cw = Py3CW(
        key='key',
        secret='secret'
    )
    with pytest.raises(ValueError) as excinfo:
        assert p3cw.request('', '')
    excinfo.match(r'Missing entity')


def test_error_invalid_entity():
    p3cw = Py3CW(
        key='key',
        secret='secret'
    )
    with pytest.raises(ValueError) as excinfo:
        assert p3cw.request('test', '')
    excinfo.match(r'Invalid entity')


def test_error_invalid_action():
    p3cw = Py3CW(
        key='key',
        secret='secret'
    )
    with pytest.raises(ValueError) as excinfo:
        assert p3cw.request('smart_trades', 'test')
    excinfo.match(r'Invalid action')


def test_error_missing_id():
    p3cw = Py3CW(
        key='key',
        secret='secret'
    )
    with pytest.raises(ValueError) as excinfo:
        assert p3cw.request('smart_trades', 'step_panic_sell')
    excinfo.match(r'Missing id')
    with pytest.raises(ValueError) as excinfo:
        assert p3cw.request('smart_trades', 'step_panic_sell', '')
    excinfo.match(r'Missing id')