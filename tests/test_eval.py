from actseg.eval import MoFAccuracy


def test_mof_accuracy():
    pre = [0, 0, 0, 1, 0, 1, 1, 1, 0, 2]
    tar = [0, 0, 1, 1, 2, 1, 1, 0, 0, 1]

    metric = MoFAccuracy()

    metric(tar, pre)

    assert metric.summary() == (6 / 10)
