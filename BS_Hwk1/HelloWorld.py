def say_hello(name: str, repeat: int = 1, goodbye: bool = False) -> None:
    """
    Print a greeting or farewell message with the given name.

    Parameters:
    - name (str): The name to include in the greeting or farewell message.
    - repeat (int, optional): The number of times to repeat the message. Default is 1.
    - goodbye (bool, optional): If True, print a farewell message; otherwise, print a greeting. Default is False.

    Returns:
    None

    Examples:
    >>> say_hello('World')
    Hello World!

    >>> say_hello('World', 3, True)
    Goodbye World!
    Goodbye World!
    Goodbye World!
    """

  if goodbye:
      message = 'Goodbye'

  else:
      message = 'Hello'

  for _ in range(repeat):
      print(f'{message} {name}!')

say_hello('World')
say_hello('World', 3, True)