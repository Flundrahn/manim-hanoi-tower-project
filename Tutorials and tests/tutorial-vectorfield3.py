from manim import *

from manim_ce.manim.grpc.impl.frame_server_impl import get

class ChangingVectorField(Scene):
    def construct(self):

        def field_func(position):
            delta_x = 1
            delta_y = 1
            coeff_matrix = np.array([[-1, -4, 0],[2,3, 0], [0, 0 ,0]])
            position = position + np.array([dt*delta_x, dt*delta_y, 0])
            position = np.transpose(position)

            field_func = coeff_matrix.dot(position)
            return field_func

        vector_field = ArrowVectorField(field_func, length_func=lambda x: 0.25)

        def vector_field_updater(vector_field, dt):
            new_field_func = get_field_func(dt)
            new_vector_field = ArrowVectorField(new_field_func, length_func=lambda x: 0.25)
            return vector_field.become(new_vector_field)

        vector_field.add_updater(vecto_field_updater)
        self.add(vector_field)
        self.wait(2)


