def test_fibonacci__check_if_fibonacci_function_exists__when_the_program_runs(mocker, calculator):
    fibonacci = mocker.spy(calculator, 'fibonacci')
    calculator.fibonacci()
    fibonacci.assert_called()
