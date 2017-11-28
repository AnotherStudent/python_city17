# python -m pytest tests.py -v

from summ import *
import pytest

@pytest.mark.parametrize("count,expected", [
  (2, [14, 28, 29, 35, 41, 53, 67, 76, 82, 92]),
  (3, [104, 117, 140, 155, 171, 208, 209, 223, 232, 277, 280,
  290, 305, 322, 334, 343, 350, 401, 410, 433, 446, 464,
  503, 515, 530, 551, 588, 589, 598, 599, 607, 644, 668,
  669, 670, 686, 696, 706, 711, 727, 760, 772, 802, 820,
  858, 859, 866, 885, 895, 902, 920, 958, 959, 966, 985, 995])])
def test_summ(count,expected):
	assert(summ(count) == expected)