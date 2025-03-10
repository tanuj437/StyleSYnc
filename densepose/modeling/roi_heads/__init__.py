# Modified by Tanuj Saxena
# Copyright (c) Facebook, Inc. and its affiliates.

from .v1convx import DensePoseV1ConvXHead
from .deeplab import DensePoseDeepLabHead
from .registry import ROI_DENSEPOSE_HEAD_REGISTRY
from .roi_head import Decoder, DensePoseROIHeads
