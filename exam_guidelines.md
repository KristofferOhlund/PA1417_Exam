### Evaluating test code quality

1. Follow principes of test design
    - avoid random values, use BVA / EP insted
    - Avoid multiple asserts in a unit test
    - patch harcoded dependencys or random values
    - Mock injectable dependencies

2. When evaluating code quality
    - Name the violation (e.g 'random test values' / 'multiple asserts', 'incorrectly patched namespace')
    - Show the location (name the rows)
    - Describe the problem
    - Describe the improvement

### Evaluating test design technique

The 4-step technique
1. Identify Actions and Conditions
2. Construct Combinations
3. Denote Expected Outcomes
4. Collapse to the Relevant Test Cases

#### Non-functional tests

Software Quality Attribute - Definitions
[ISO25010](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010)