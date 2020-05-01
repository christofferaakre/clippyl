from moviepy.editor import *
from moviepy.video.fx.all import fadein

folder = 'clips/Counter-Strike_Global_Offensive/2020-04-30'

clip1 = fadein(VideoFileClip("1.mp4").subclip(0, 2), 1)
clip2 = fadein(VideoFileClip("2.mp4").subclip(0, 2), 1)
clip3 = fadein(VideoFileClip("3.mp4").subclip(0, 2), 1)

text_width = 720
text_height = 120

center_x = 1920 / 2  - text_width / 2
speed = 3

def text_position(t):
    if t >= (center_x + text_width) / (speed *center_x):
        return (center_x, 0)
    else:
        return (speed * t * center_x - text_width, 0)

text = slide_in(fadein(TextClip(txt="zizaran", font="Roobert", bg_color="purple", color="white", size=[text_width, text_height]).set_pos((center_x, 0).set_duration(3).set_start(1), 2)))
clip1 = CompositeVideoClip([clip1, text])

TextClip.list("font")
TextClip.list("color")

fade_duration = 1

final_clip = clip1

final_clip.write_videofile("videos/test.mp4", threads=8)