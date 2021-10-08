# Reference Action Segmentation Evaluation Code

This repository contains the reference code for action segmentation evaluation.

If you have a bug-fix/improvement or if you want to add a new features please send a pull request or open an issue.

## Installation

The `actseg` library is available on PyPI.

```shell
pip install actseg
```

## Development

```shell
make init
make test
```

## Example Usage

All the metrics have the same api.

```python
from actseg.eval import MoFAccuracy, Edit

pred1 = [0, 0, 0, 1, 0, 1, 1, 1, 0]
pred2 = [1, 2, 3, 0, 0, 1, 2, 3, 0, 0, 0, 1, 2, 3, 0, 0, 0, 0]

target1 = [0, 0, 1, 1, 2, 1, 1, 0, 0]
target2 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]

metrics = [MoFAccuracy(), Edit()]
for p, t in zip([pred1, pred2], [target1, target2]):
    for m in metrics:
        m(targets=t, predictions=p)

for m in metrics:
    print(m)

# MoF: 0.3333333333333333
# Edit: 52.5
```

## Metrics

### Frame-wise Metrics
1. MoF (Accuracy)
2. F1Score
3. IoD
4. IoU

### Segment-wise Metrics
1. Edit (Edit distance or matching score)

### Specifying Ignore Class

For some Metrics it is possible to specify the indices of classes to ignore (e.g. Background) by 
passing `ignore_ids` parameter to the constructor.


## Acknowledgement

Please see `src/actseg/external` for external sources used in this project.
