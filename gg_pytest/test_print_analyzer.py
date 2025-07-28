# test_print_analyzer.py

from dataclasses import dataclass
import ast
import pytest

@dataclass
class PrintAnalysisResult:
    count: int
    line_range: tuple[int, int]

def analyze_print_statements(source_code: str) -> PrintAnalysisResult:
    tree = ast.parse(source_code)
    print_nodes = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and hasattr(node.func, 'id')
        and node.func.id == 'print'
    ]

    if not print_nodes:
        return PrintAnalysisResult(count=0, line_range=(0, 0))


    print_nodes.sort(key=lambda n: n.lineno)
    last_print = print_nodes[-1]
    start_line = last_print.lineno
    end_line = getattr(last_print, 'end_lineno', start_line)

    return PrintAnalysisResult(count=len(print_nodes), line_range=(start_line, end_line))



print_last_lines = [
    pytest.param(
        "print('Hello')",
        1,
        (1, 1),
        id="single line print"
    ),
    pytest.param(
        "print(\n    'multi-line'\n)",
        1,
        (1, 3),
        id="multi-line print"
    ),
    pytest.param(
        "x = 10\n# comment\nprint('end')",
        1,
        (3, 3),
        id="print after code and comment"
    ),
    pytest.param(
        "def f():\n    print('inside')\nprint('outside')",
        2,
        (3, 3),
        id="multiple prints, last outside"
    ),
]

@pytest.mark.parametrize(
    "source_code, expected_count, expected_range",
    print_last_lines,
    ids=[param.id for param in print_last_lines],
)
def test_print_analysis(source_code, expected_count, expected_range):
    result = analyze_print_statements(source_code)
    assert result.count == expected_count
    assert result.line_range == expected_range
