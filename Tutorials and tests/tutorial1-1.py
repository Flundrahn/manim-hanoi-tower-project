from manim import *  #import manim library
class Animation1(Scene):
    def construct(self):
        box = Rectangle(height=1, width=1)

        self.add(box)
        self.play(box.animate.shift(RIGHT*2), run_time=2)
        self.play(box.animate.shift(UP*3), run_time=2)
        self.play(box.animate.shift(DOWN*5+LEFT*5), run_time=2)
        self.play(box.animate.shift(UP*1.5+RIGHT*1), run_time=2)