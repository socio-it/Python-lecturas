import re

class Tokens:
    __match_args__ = ('input', 'output')
    typecode = "d"

    def __init__(self, input: int, output: int):
        self.input = input
        self.output = output

    @property
    def input(self) -> int:
        return self._input

    @input.setter
    def input(self, value: int):
        self._input = int(value)

    @property
    def output(self) -> int:
        return self._output

    @output.setter
    def output(self, value: int):
        self._output = int(value)

    def __iter__(self):
        return iter((self.input, self.output))

    def __repr__(self):
        return f"Tokens(input={self.input}, output={self.output})"

    __str__ = __repr__

    def __eq__(self, value):
        if not isinstance(value, Tokens):
            return NotImplemented
        return self.input == value.input and self.output == value.output

    def __hash__(self):
        return hash((self.input, self.output))

    def __format__(self, format_spec):
        if format_spec == "total":
            return f"Total Tokens: {self.input + self.output}"
        if format_spec == "i":
            return f"Input Tokens: {self.input}"
        if format_spec == "o":
            return f"Output Tokens: {self.output}"
        return f"Tokens(input={self.input:{format_spec}}, output={self.output:{format_spec}})"

    @classmethod
    def frombytes(cls, octects: bytes) -> "Tokens":
        s = octects.decode("ascii", "ignore")
        # opcionalmente descartar prefijo de typecode
        if s and s[0].isalpha():
            s = s[1:]
        m = re.fullmatch(r"input=(\d+)output=(\d+)", s)
        if not m:
            raise ValueError(f"Formato inválido: {octects!r}")
        i, o = map(int, m.groups())
        return cls(i, o)


# Pruebas
d = Tokens(5, 10)
print(d)                                  # Tokens(input=5, output=10)
print(Tokens.frombytes(b'dinput=5output=10'))  # Tokens(input=5, output=10)
