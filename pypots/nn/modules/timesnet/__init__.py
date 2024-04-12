"""
The package including the modules of TimesNet.

Refer to the paper
`Haixu Wu, Tengge Hu, Yong Liu, Hang Zhou, Jianmin Wang, and Mingsheng Long.
TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis.
In ICLR, 2023.
<https://openreview.net/pdf?id=ju_Uqw384Oq>`_

"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: BSD-3-Clause


from .backbone import BackboneTimesNet
from .layers import InceptionBlockV1, TimesBlock

__all__ = [
    "BackboneTimesNet",
    "InceptionBlockV1",
    "TimesBlock",
]
