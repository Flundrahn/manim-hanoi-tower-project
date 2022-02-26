from manim import *
class Updaters(Scene):
    def construct(self):
        
        r = RoundedRectangle(stroke_width=4, stroke_color=WHITE, fill_color=BLUE_B, width=4.5, height=2)
        r.shift(UP*3+LEFT*4)

        mathtext = MathTex("\\frac{3}{4} = 0.75")
        mathtext.set_color_by_gradient(GREEN, YELLOW).set_height(1.5)
        # mathtext.move_to(r.get_center())
        mathtext.add_updater(lambda x : x.move_to(r.get_center()))

        self.play(FadeIn(r))
        self.play(Write(mathtext))
        self.play(r.animate.shift(RIGHT*1.5+DOWN*5), run_time=3)
        self.wait()
        mathtext.clear_updaters()
        self.play(r.animate.shift(LEFT*2+UP*1), run_time=3)
        self.play(r.animate.move_to(mathtext.get_center()))