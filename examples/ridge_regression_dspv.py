#*******************************************************************************
# Copyright 2014-2018 Intel Corporation
# All Rights Reserved.
#
# This software is licensed under the Apache License, Version 2.0 (the
# "License"), the following terms apply:
#
# You may not use this file except in compliance with the License.  You may
# obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#*******************************************************************************

# daal4py Ridge Regression example for distributed memory systems; distributed Single Process View mode
# run like this:
#    mpirun -genv DIST_CNC=MPI -n 4 python ./ridge_regression_dspv.py

import daal4py as d4p
from numpy import loadtxt, allclose

if __name__ == "__main__":

    # Initialize SPV mode
    d4p.daalinit()
    
    # We need partioned input data, like from multiple files
    infiles = ["./data/distributed/linear_regression_train_" + str(x) + ".csv" for x in range(1,5)]

    # Configure a Ridge regression training object
    train_algo = d4p.ridge_regression_training(distributed=True)
    
    # Read data. Let's have 10 independent, and 2 dependent variables (for each observation)
    indep_data = [loadtxt(x, delimiter=',', usecols=range(10)) for x in infiles]
    dep_data   = [loadtxt(x, delimiter=',', usecols=range(10,12)) for x in infiles]
    # Note, providing a list of files instead also distributes the file read!
    
    # Now train/compute, the result provides the model for prediction
    train_result = train_algo.compute(indep_data, dep_data)

    # Now let's do some prediction (it runs only on a single node)
    predict_algo = d4p.ridge_regression_prediction(distributed=True)
    # read test data (with same #features)
    pdata = loadtxt("./data/distributed/linear_regression_test.csv", delimiter=',', usecols=range(10))
    # now predict using the model from the training above
    predict_result = d4p.ridge_regression_prediction().compute(pdata, train_result.model)
    
    # The prediction result provides prediction
    assert predict_result.prediction.shape == (pdata.shape[0], dep_data[0].shape[1])

    print('All looks good!')
    d4p.daalfini()
