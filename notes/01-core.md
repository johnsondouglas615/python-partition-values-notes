# Partition values by a threshold: implementation

## What the example does

Both output lists retain input order. The threshold belongs to the high partition because the comparison is greater-than-or-equal.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "items": [
    3,
    1,
    5,
    3
  ],
  "threshold": 3
}
```

Expected result:

```json
{
  "low": [
    1
  ],
  "high": [
    3,
    5,
    3
  ]
}
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
