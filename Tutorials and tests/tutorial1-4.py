from manim import *
class Redrawers(Scene):
    def construct(self):
        
        r = ValueTracker(0.5) # Tracks value of radius

        circle = always_redraw(lambda :
        Circle(radius=r.get_value(), stroke_color=YELLOW, stroke_width=5)
        )

        line_radius = always_redraw(lambda :
        Line(start=circle.get_center(), end=circle.get_bottom(), stroke_color = RED_B, stroke_width = 10)
        )

        line_circumference = always_redraw(lambda :
        Line(stroke_color=YELLOW, stroke_width=5).set_length(2*r.get_value() *PI).next_to(circle, DOWN, buff=0.2)
        )

        triangle = always_redraw(lambda : 
        Polygon(circle.get_top(), circle.get_left(), circle.get_right(), fill_color=GREEN_C, fill_opacity=0.8)
        )

        all_mobs = VGroup(circle,triangle)

        self.play(LaggedStart(
            Create(circle), DrawBorderThenFill(line_radius), DrawBorderThenFill(triangle), run_time=4, lag_ratio=0.75
            ))
        self.play(ReplacementTransform(circle.copy(),line_circumference), run_time=2)
        self.play(r.animate.set_value(2), run_time=5)

        self.play(
            self.camera.frame.set_height(all_mobs.height()*1.2),
            self.camera.frame.move_to(all_mobs.get_center())
        )