# freeseer - vga/presentation capture software
#
#  Copyright (C) 2010  Free and Open Source Software Learning Centre
#  http://fosslc.org
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# For support, questions, suggestions or any other inquiries, visit:
# the #fosslc channel on IRC (freenode.net)

from freeseer import *
import os

class FreeseerCore:
    freeseer = FreeSeeR()

    def get_video_devices(self):
        i = 0
        vid_devices = []
        dev='/dev/video' + str(i)
        while os.path.exists(dev):
            i=i+1
            vid_devices.append(dev)
            dev='/dev/video'+str(i)
        vid_devices.append('/dev/fw1')
        return vid_devices
        
    def get_video_sources(self):
        vid_sources = ['v4l2src', 'v4lsrc', 'dv1394src', 'ximagesrc']
        return vid_sources

    def get_audio_sources(self):
        snd_sources = ['alsasrc', 'pulsesrc']
        return snd_sources

    def get_talk_titles(self):
        talk_titles = []
        f = open('talks.txt', 'r')
        lines = f.readlines()
        f.close()

        for line in lines:
            talk_titles.append(line.rstrip())
        return talk_titles

    # Returns the filename to use when recording
    # This function checks to see if a file exists and increments index
    # until a filename that does not exist is found
    def get_record_name(self, filename):
        i = 0
        recordname = self.make_record_name(filename, i)
        while os.path.exists(recordname):
            i=i+1
            recordname = self.make_record_name(filename, i)
        return recordname

    def make_record_name(self, filename, index):
        return filename + str(index) + '.ogg'

    def change_videosrc(self, vid_source, vid_device):
        self.freeseer.change_videosrc(vid_source, vid_device)

    def change_soundsrc(self, snd_source):
        self.freeseer.change_soundsrc(source)

    def record(self, filename='default.ogg'):
        self.freeseer.record(filename)

    def stop(self):
        self.freeseer.stop()

    def preview(self, enable=False, window_id=None):
        if enable == True:
            self.freeseer.enable_preview(window_id)
            print 'Preview Activated'
        else:
            print 'Preview Deactivated'
