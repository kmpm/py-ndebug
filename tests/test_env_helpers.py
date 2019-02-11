from ndebug import env_helpers


def test_inspect_ops(mocker):
    mocker.patch.dict('os.environ', {'DEBUG_COLORS': 'no',
                                     'DEBUG_DEPTH': '10',
                                     'DEBUG_SHOW_HIDDEN': 'enabled',
                                     'DEBUG_SOMETHING': 'null'})
    actual = env_helpers.options()
    assert actual == {'colors': False, 'depth': 10, 'show_hidden': True, 'something': None}


def test_load_and_save():
    actual = env_helpers.load()
    assert actual == ''

    env_helpers.save('test:data')
    actual = env_helpers.load()
    assert actual == 'test:data'
