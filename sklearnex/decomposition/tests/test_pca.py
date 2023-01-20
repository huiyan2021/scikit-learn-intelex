#!/usr/bin/env python
#===============================================================================
# Copyright 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#===============================================================================

import numpy as np
from numpy.testing import assert_allclose


def test_sklearnex_import():
    from sklearnex.decomposition import PCA
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    pca = PCA(n_components=2, svd_solver='full').fit(X)
    assert 'sklearnex' in pca.__module__
    assert_allclose(pca.singular_values_, [[6.30061236 0.54980354]])
    assert_allclose(pca.components_, [[ 0.83849223  0.54491356][-0.54491356  0.83849223]])
    assert_allclose(pca.explained_variance_ratio_, [[0.9924429 0.0075571]])
