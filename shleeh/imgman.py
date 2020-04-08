import numpy as np
from scipy.ndimage import affine_transform


def reorient_to_ras(data, affine, vox_resol):
    """ Reorient and re-sample the input data into RAS space
    to ensure consistent orientation regardless of which axis
    was sliced during data acquisition.
    """
    org_shape = data.shape
    fov_size = np.asarray(org_shape) * vox_resol
    rotate_mat = (affine[:3, :3] / vox_resol).astype(np.int8)
    origin = rotate_mat.dot(fov_size/2)

    org_affine = affine.copy()
    org_affine[:3, 3] = -origin

    ras_shape = abs(rotate_mat.dot(org_shape))
    ras_affine = np.eye(4)
    ras_affine[:3, :3] = np.diag(vox_resol)
    ras_affine[:3, 3] = -fov_size/2

    org_mm2vox = np.linalg.inv(org_affine)
    ras_mm2vox = org_mm2vox.dot(ras_affine)

    rotate = ras_mm2vox[:3, :3]
    shift = ras_mm2vox[:3, 3]
    return affine_transform(data, rotate, shift, output_shape=ras_shape)
