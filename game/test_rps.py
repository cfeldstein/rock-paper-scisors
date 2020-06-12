#!/usr/bin/env python3
# test_rps.py

import pytest

from .rps import *


def test_rps():
    assert rps() is None


def test_intro(capsys):
    intro()
    out, err = capsys.readouterr()
    assert out == 'Welcome to Rock, Paper, Scissors\n'


# TODO - Resolve issue with: "OSError: pytest: reading from stdin while output is captured! Consider using `-s`."
@pytest.mark.skip
@pytest.mark.parametrize("user, result", [
    ('r', 'Rock'),
    ('s', 'Scissors'),
    ('p', 'Paper'),
])
def test_get_input(user, result):
    get_input.input = lambda: user
    x = get_input()
    assert x == result


@pytest.mark.repeat(12)
def test_get_random():
    assert get_random(game) in game


@pytest.mark.parametrize("user, ai, result", [
    ('Rock', 'Rock', 'Draw'),
    ('Rock', 'Scissors', 'Win'),
    ('Rock', 'Paper', 'Lose'),
    ('Scissors', 'Scissors', 'Draw'),
    ('Scissors', 'Rock', 'Lose'),
    ('Scissors', 'Paper', 'Win'),
    ('Paper', 'Paper', 'Draw'),
    ('Paper', 'Rock', 'Win'),
    ('Paper', 'Scissors', 'Lose'),
])
def test_get_result(user, ai, result):
    assert get_result(user, ai) == result


@pytest.mark.parametrize("result, output", [
    ('Win', 'You WON!\n'),
    ('Lose', 'You Lose.\n'),
    ('Draw', 'Its a Draw.\n'),
    ('else', 'Should not get here\n'),
])
def test_output_result(result, output, capsys):

    output_result(result)
    out, err = capsys.readouterr()
    assert out == output


@pytest.mark.parametrize('user, ai', [
    ('Rock', 'Rock'),
    ('Scissors', 'Scissors'),
    ('Paper', 'Paper'),
])
def test_output_choices(user, ai, capsys):
    output_choices(user, ai)
    out, err = capsys.readouterr()
    assert out == f"You played:  {user} . The computer played:  {ai} .\n"

