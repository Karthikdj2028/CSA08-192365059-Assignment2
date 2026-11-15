# Q6 – Call tree for n = 5

The recurrence is `ways(n) = ways(n-1) + ways(n-2)` with `ways(0)=1` and `ways(1)=1`.

```text
ways(5)
├── ways(4)
│   ├── ways(3)
│   │   ├── ways(2)
│   │   │   ├── ways(1)
│   │   │   └── ways(0)
│   │   └── ways(1)
│   └── ways(2)
│       ├── ways(1)
│       └── ways(0)
└── ways(3)
    ├── ways(2)
    │   ├── ways(1)
    │   └── ways(0)
    └── ways(1)
```

Repeated subproblems include `ways(3)` and `ways(2)`. Plain recursion calculates them more than once. Memoisation stores each result the first time and returns it on later requests.
