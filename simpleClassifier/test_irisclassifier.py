from typing import Set
import irisclassifier
import pytest


def test_evaluation():
    i = irisclassifier.IrisClassifie()
    i.ingestion()
    i.segregation()
    i.train()
    res = i.evaluation()
    assert res > 0.75

