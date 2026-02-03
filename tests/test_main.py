import builtins
import pytest
from calculator import main  # imports your main.py file


def run_main_with_inputs(monkeypatch, capsys, inputs):
    """
    Helper to run main.main() with mocked user input.
    inputs: list of strings, each returned by input() in order.
    """
    it = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda _: next(it))
    main.main()
    return capsys.readouterr().out


def test_calculator_addition(monkeypatch, capsys):
    output = run_main_with_inputs(monkeypatch, capsys, ["1", "2", "3"])
    assert "Result:" in output
    assert "Result: 5.0" in output


def test_calculator_subtraction(monkeypatch, capsys):
    output = run_main_with_inputs(monkeypatch, capsys, ["2", "10", "4"])
    assert "Result:" in output
    assert "Result: 6.0" in output


def test_calculator_multiplication(monkeypatch, capsys):
    output = run_main_with_inputs(monkeypatch, capsys, ["3", "3", "4"])
    assert "Result:" in output
    assert "Result: 12.0" in output


def test_calculator_division(monkeypatch, capsys):
    output = run_main_with_inputs(monkeypatch, capsys, ["4", "10", "2"])
    assert "Result:" in output
    assert "Result: 5.0" in output


def test_invalid_choice(monkeypatch, capsys):
    output = run_main_with_inputs(monkeypatch, capsys, ["9", "1", "2"])
    assert "Invalid choice" in output


def test_divide_by_zero(monkeypatch, capsys):
    output = run_main_with_inputs(monkeypatch, capsys, ["4", "10", "0"])
    assert "Error: Cannot divide by zero" in output
