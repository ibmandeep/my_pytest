# pytest.param in a nutshell:
# pytest.param is a special helper provided by pytest to add metadata (like id, marks, etc.) 
# to individual parameter sets when using @pytest.mark.parametrize.


# pytest.param(arg1, arg2, ..., id="custom_id", marks=pytest.mark.xfail)

# Use pytest.param when:

# You want to customize test case IDs.
# You want to mark individual parameters (e.g. xfail, skip).
# You want to attach metadata to specific parameter values.


import pytest

@pytest.mark.parametrize(
    "x, y",
    [
        pytest.param(1, 2, id="one-two"),
        pytest.param(3, 4, id="three-four"),
    ]
)
def test_add(x, y):
    assert x + y > 0



#Mark One Param as Expected to Fail
@pytest.mark.parametrize(
    "x",
    [
        pytest.param(1, id="pass"),
        pytest.param(0, marks=pytest.mark.xfail(reason="zero always fails"), id="xfail-zero"),
    ]
)
def test_nonzero(x):
    assert x != 0


#Example 3: Combine id and marks
# pytest.param(42, id="meaning_of_life", marks=pytest.mark.skip(reason="Too obvious"))


@pytest.mark.parametrize(
    "input_value",
    [
        pytest.param(10, id="valid-input"),
        pytest.param(0, id="xfail-zero", marks=pytest.mark.xfail(reason="Zero is invalid")),
        pytest.param(-1, id="skip-negative", marks=pytest.mark.skip(reason="Negative input not supported")),
    ]
)
def test_positive_input(input_value):
    assert input_value > 0




# Let's say this is your test data list
print_last_lines = [
    pytest.param("print('hello')", 1, (1, 1), id="single-print"),
    pytest.param("print('one')\nprint('two')", 2, (1, 2), id="double-print"),
    pytest.param("def f():\n    print('inside')\nprint('outside')", 
    2, 
    (3, 3), 
    id="nested-and-top-level"
    ),
    pytest.param("print('skip this')", 1, (1, 1), id="skip-case", marks=pytest.mark.skip(reason="Example skip")),
]

# Now parametrize using that list and extract ids
@pytest.mark.parametrize(
    "source_code, expected_count, expected_range",
    print_last_lines,
    ids=[param.id for param in print_last_lines]
)
def test_print_analysis(source_code, expected_count, expected_range):
    result = analyze_print_statements(source_code)
    assert result.count == expected_count
    assert result.line_range == expected_range

# Dummy implementation for example to run
def analyze_print_statements(code: str):
    lines = code.splitlines()
    count = 0
    line_nums = []
    for idx, line in enumerate(lines, start=1):
        if "print(" in line and not line.startswith(" "):  # Skip indented
            count += 1
            line_nums.append(idx)
    if not line_nums:
        return type("Result", (), {"count": 0, "line_range": (0, 0)})
    return type("Result", (), {"count": count, "line_range": (line_nums[0], line_nums[-1])})
