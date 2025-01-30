import os
import sys

import numpy as np
import scipy

TEST_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TEST_DIR_PATH + "/../../")

import torch_math_tools as tmt

# ----------------------------------------------------------------------------# 
# --------------------             Constants              --------------------# 
# ----------------------------------------------------------------------------# 

SAMPLE_DATA_DIR = os.path.join(TEST_DIR_PATH, "sample_data")
SAMPLE_DTSERIES_PATH = os.path.join(SAMPLE_DATA_DIR, "dtseries.npy")
SAMPLE_PARTITION_PATH = os.path.join(SAMPLE_DATA_DIR, "partition.npy")


DIST_DIR = "/data/data7/network_control/projects/network_control/resources/brain_distances"
SUBCORTEX_MASK_PATH = os.path.join(DIST_DIR, "subcortex_mask.npy")
GEODESIC_MASK_PATH = os.path.join(DIST_DIR, f"geodesic_mask_10.npz")

# ----------------------------------------------------------------------------# 
# --------------------                Main                --------------------# 
# ----------------------------------------------------------------------------# 


def main():
    """ """

    USE_SYNTHETIC = True

    if os.path.exists(SAMPLE_DTSERIES_PATH) and not USE_SYNTHETIC:
        voxel_data = np.load(SAMPLE_DTSERIES_PATH)
        subcortex_index = np.load(SUBCORTEX_MASK_PATH)
        geodesic_mask = scipy.sparse.load_npz(GEODESIC_MASK_PATH)

    else:
        voxel_data = np.random.randn(900, 91_282)
    
    subcortex_index, geodesic_mask = None, None

    block_size = 5_000
    print(f"BLOCK SIZE :: {block_size}")
    print(voxel_data.shape)

    backend = "torch"
    # backend = "numpy"

    # sc = tmt.block_aggregators.Runner.run(voxel_data[:, :], mask=geodesic_mask, exclude_index=subcortex_index,
    #                                      block_size=block_size, symmetric=True, backend=backend)

    # sc = tmt.SparseCorrelator.run(voxel_data[:, :], mask=geodesic_mask, exclude_index=subcortex_index,
    #                               block_size=block_size, symmetric=True, backend=backend)

    sc = tmt.ThresholdCorrelator.run(voxel_data[:, :], threshold=0.1, mask=geodesic_mask, exclude_index=subcortex_index,
                                  block_size=block_size, symmetric=True, backend=backend)


if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------# 
# --------------------                End                 --------------------# 
# ----------------------------------------------------------------------------#
