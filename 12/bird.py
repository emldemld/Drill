import game_framework
from pico2d import *
from random import randint

import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 40.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event

# Boy States

class RunState:

    def enter(bird, event):
        if bird.dir > 0  and bird.velocity >= 0:
            bird.velocity += RUN_SPEED_PPS
        elif  bird.dir <= 0 and bird.velocity <= 0:
            bird.velocity -= RUN_SPEED_PPS
        bird.dir = clamp(-1, bird.velocity, 1)

    def exit(bird, event):
        pass

    def do(bird):
        #boy.frame = (boy.frame + 1) % 8
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)

    def draw(bird):
        bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)

class Bird:

    def __init__(self):
        self.x, self.y = randint(100, 1500), randint(100, 600)
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('bird100x100x14.png')
        self.dir = randint(0, 1)
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)

    def get_bb(self):
        # fill here
        return 0, 0, 0, 0


    def add_event(self, event):
        pass

    def update(self):
        self.cur_state.do(self)
        if self.x > 1500 or self.x < 100:
            self.dir = -self.dir
            self.velocity = -self.velocity


    def draw(self):
        self.cur_state.draw(self)
        #fill here

    def handle_event(self, event):
        pass
