
def visbrain_plot(mesh, tex=None):
    """
    Visualize a trimesh object using visbrain core plotting tool
    :param mesh: trimesh object
    :param tex: numpy array of a texture to be visualized on the mesh
    :return:
    """
    from visbrain.objects import BrainObj

    # invert_normals = True -> Light outside
    # invert_normals = False -> Light inside
    b_obj = BrainObj('gui', vertices=mesh.vertices, faces=mesh.faces,
                     translucent=False, invert_normals=True)
    if tex is not None:
        b_obj.add_activation(data=tex, cmap='viridis')
    b_obj.preview(bgcolor='white')


def pyglet_plot(mesh, curv_ref=None):
    """
    Visualize a trimesh object using pyglet as proposed in trimesh
    the added value is for texture visualization
    :param mesh: trimesh object
    :param curv_ref: numpy array of a texture to be visualized on the mesh
    :return:
    """
    import numpy as np
    if curv_ref is not None:
        # scale the map between 0 and 1
        scaled_curv = curv_ref - curv_ref.min()
        scaled_curv = scaled_curv / scaled_curv.max()
        # convert into uint8 in [0 255]
        vect_col = np.stack([255 * np.ones(scaled_curv.shape),
                             np.round(scaled_curv * 255),
                             np.round(scaled_curv * 255),
                             255 * np.ones(scaled_curv.shape)],
                            axis=1).astype(np.uint8)
        if vect_col.shape[0] == mesh.vertices.shape[0]:
            mesh.visual.vertex_colors = vect_col  # color.to_rgba(vect_col)
        elif vect_col.shape[0] == mesh.faces.shape[0]:
            mesh.visual.face_colors = vect_col
    # call the default trimesh visualization tool using pyglet
    mesh.show()
