from manim import *
import numpy as np

class TowerOfHanoi(ZoomedScene):
    def __init__(self):
        self.n_discs = 6
        self.disc_height = 1        
        self.rod_spacing = self.disc_height + self.n_discs + 1
        self.rod_height = self.disc_height * self.n_discs + 0.5
        self.anim_speed = 0.3
        self.font_size = DEFAULT_FONT_SIZE*1.4
        self.disc_buff = 0.05
        super().__init__()

    def move_disc(self, from_group, target_group):
        disc = from_group[-1]
        from_group.remove(disc)
        disc_x_coord = disc.get_center()[0]
        self.play(
            disc.animate.move_to(np.array([disc_x_coord, self.rod_height + self.disc_height*2, 0])),
            run_time = self.anim_speed
        )
        self.play(
            disc.animate.shift(RIGHT * (target_group.get_center() - disc.get_center())),
            run_time = self.anim_speed
        )
        self.play(
            disc.animate.next_to(target_group, UP, buff = self.disc_buff),
            self.moves_counter_var.tracker.animate.increment_value(1),
            run_time = self.anim_speed)
        target_group.add(disc)
        
    
    def hanoi_solver(self, n_discs, start_group, help_group, target_group):
        if n_discs > 0:
            self.hanoi_solver(n_discs - 1, start_group, target_group, help_group)
            self.move_disc(start_group, target_group)
            self.hanoi_solver(n_discs - 1, help_group, start_group, target_group)
        
    def construct(self):

        # Define rods
        a = VectorizedPoint(location = LEFT * self.rod_spacing)
        b = VectorizedPoint(location = ORIGIN)
        c = VectorizedPoint(location = RIGHT * self.rod_spacing)
        
        rod_a = Line(start = a.get_center(), end = a.get_center() + UP * self.rod_height)
        rod_b = Line(start = b.get_center(), end = b.get_center() + UP * self.rod_height)
        rod_c = Line(start = c.get_center(), end = c.get_center() + UP * self.rod_height)
        rods = VGroup(rod_a, rod_b, rod_c)

        # Labels
        a_label = Tex("A", font_size = self.font_size)
        b_label = Tex("B", font_size = self.font_size)
        c_label = Tex("C", font_size = self.font_size)
        a_label.next_to(rod_a, DOWN)
        b_label.next_to(rod_b, DOWN)
        c_label.next_to(rod_c, DOWN)
        labels = VGroup(a_label, b_label, c_label)

        # Define discs
        r_discs = range(self.n_discs)
        discs = VGroup()
        for r in r_discs:
            d_width = self.disc_height + self.n_discs - (r+1)
            d = Rectangle(
                height = self.disc_height,
                width = d_width,
                color = BLUE,
                fill_opacity = 1,
                sheen_factor = 0.3,
                sheen_direction = np.array([- 1, 1, 0])
            )
            discs.add(d)

        # Groups for discs at each rod with points a, b and c at bottom
        a_group = VGroup(a)
        b_group = VGroup(b)
        c_group = VGroup(c)

        # Configure camera
        all_mobs = VGroup(discs,rods)
        camera_y_pos = np.array([0, self.rod_height*0.6, 0])
        self.camera.frame.move_to(camera_y_pos).set(height = self.rod_height*2.8)

        # Create move counter
        self.moves_counter_var = Variable(0, Text("Moves", font_size = self.font_size), var_type = Integer).align_to(self.camera.frame, UR).shift(np.array([-2, -1, 0]))
        self.moves_counter_var.label.set_color(RED)
        self.moves_counter_var.value.set(font_size = self.font_size*1.4).set_color(RED)

        intro_text = Text(
            "This is a visualization of the Tower of Hanoi Puzzle.\n" +
            "Invented by French mathematician Édouard Lucas in the 19th century.",
            font_size = self.font_size,
            should_center = True,
            line_spacing=1.3
        )

        objective_text = Text(
            "The objective of the puzzle is to move an entire stack\n" +
            "of discs to the last rod, obeying the following rules:\n\n" +
            "1. Only one disk may be moved at a time.\n" +
            "2. Only the disk at the top of a stack may be moved.\n" +
            "3. No disk may be placed on top of a smaller disc.\n\n" +
            "The puzzle can be solved using an elegant recursive algorithm:",
            font_size = self.font_size,
            should_center = True,
            line_spacing=1.3
        )
        
        solver_text = Text(
            "def hanoi_algorithm(n_discs, A, B, C):\n" +
            "     if n_discs > 0:\n" +
            "          hanoi_algorithm(n_discs-1, A, C, B)\n" +
            "          move_disc(from = A, to = C)\n" +
            "          hanoi_algorithm(n_discs-1, B, A, C)",
            font_size = self.font_size,
            should_center = False,
            font="Consolas",
            line_spacing=1.3
        )
        intro_text.move_to(camera_y_pos)
        objective_text.move_to(camera_y_pos)
        solver_text.move_to(camera_y_pos)

        self.wait(1.5)
        self.play(Write(intro_text), run_time = 2)
        self.wait(3)
        self.play(FadeOut(intro_text))
        self.play(Write(objective_text), run_time = 2)
        self.wait(8)
        self.play(FadeOut(objective_text))
        self.play(Write(solver_text), run_time = 2)
        self.wait(8)
        self.play(FadeOut(solver_text))

        self.play(*[
            Create(rod)
            for rod in rods
        ])

        for label in labels:
            self.play(FadeIn(label))
            self.wait(0.1)

        discs.move_to(a).shift(UP * 3 * self.rod_height)
        self.add(discs)
    
        for disc, k in zip(discs, range(len(discs))):
            self.play(
                disc.animate.next_to(a_group, UP, buff = self.disc_buff),
                run_time = 0.5
            )
            a_group.add(disc)

        self.play(Create(self.moves_counter_var))
        self.wait(1)

        self.hanoi_solver(self.n_discs, a_group, b_group, c_group)  
        self.wait(2)