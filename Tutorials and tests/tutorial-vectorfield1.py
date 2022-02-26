# A vector field represented by a set of change vectors
# Values displayed as grid of vectors. By default color is magnitude.
# Parameters func, color, color_scheme, min_color_scheme_value, max_color_scheme_value,
# colors, x_range, y_range, z_range, three_dimensions, length_func, opacity, vector_config, kwargs

from manim import *

def test_coefficient_matrix(coefficient_matrix):   # This function does not give expected result as matrix is 3x3 yet should be 2x2 for 2D vector field
    A = coefficient_matrix
    A_tr = np.trace(A)
    A_det = np.linalg.det(A)
    # Equation must be less than zero to produce a stable spiral vector field
    return print(A_tr**2 - 4*A_det)

def get_field_func(position, dt):
    delta_x = 1
    delta_y = 1
    coeff_matrix = np.array([[-1, -4, 0],[2,3, 0], [0, 0 ,0]])
    position = position + np.array([dt*delta_x, dt*delta_y, 0])
    position = np.transpose(position)

    field_func = coeff_matrix.dot(position)
    return field_func

class ChangingVectorField(Scene):
    CONFIG = {
        "vector_field_config": {},
        "anim_time": 3,
    }
    def construct(self):
        vector_field = self.get_vector_field(dt=0)

        def update_vector_field(vector_field,dt):
            new_field = self.get_vector_field(dt)
            vector_field.become(new_field)

        # self.add(numberplane)

        # Add updater
        vector_field.add_updater(update_vector_field)
        self.add(vector_field)

        # Animation time:
        self.wait(self.anim_time)

    def get_vector_field(self,dt):
        field_func = get_field_func(dt)
        # field_func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
        vector_field = ArrowVectorField(field_func,length_func = lambda x: 0.25,**self.vector_field_config)
        return vector_field