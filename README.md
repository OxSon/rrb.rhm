This project is a work in progress (as is this README).

## About
`tbd`

- [references](https://github.com/OxSon/rrb.rhm/discussions/1)
## Build
- [Install Racket](https://racket-lang.org/download/)
- `git clone git@github.com:OxSon/rrb.rhm.git`
- `cd rrb.rhm && raco make cow_array.rhm rbtree.rhm rrbtree.rhm utils.rhm time.rhm`

## Test
- `raco test .`

## Bench
- [Install python](https://www.python.org/downloads/)
- `pip install -r requirements.txt`
- `racket time.rhm`
- `python benchmarks/graph_bench.py`


