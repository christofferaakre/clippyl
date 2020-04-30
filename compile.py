from moviepy.editor import *
from moviepy.video.fx.all import fadein

folder = 'clips/Counter-Strike_Global_Offensive/2020-04-30'

clip1 = VideoFileClip("1.mp4")
clip2 = VideoFileClip("2.mp4")
clip3 = VideoFileClip("3.mp4")

fade_duration = 1

final_clip = concatenate_videoclips(
    [
        fadein(clip1, 1),
        fadein(clip2, 1),
        fadein(clip3, 1),
    ], padding=-fade_duration
)
final_clip.write_videofile("videos/test.mp4", threads=8)