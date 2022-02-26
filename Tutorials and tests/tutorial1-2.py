from manim import *
class FittingObjects(Scene):
    def construct(self):
        axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], x_length=10, y_length=10)
        axes.to_edge(LEFT, buff=0.5)

        c = Circle(stroke_width=6, stroke_color=WHITE, fill_color=RED_C,fill_opacity=0.8)
        c.set_width(2).to_edge(DR, buff=0)
        t = Triangle(stroke_color=ORANGE, stroke_width=10,fill_color=GREY,fill_opacity=0.8)
        t.set_height(2).shift(DOWN*3+RIGHT*3)

        self.play(Write(axes))
        self.play(DrawBorderThenFill(c))
        self.play(c.animate.set_width(1))
        self.play(Transform(c,t, run_time=3))