"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playing=""
        self.pause=""

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        # show_videos=self._video_library.get_all_videos()
        l=[]
        print("Here's a list of all available videos: ")
        s=""
        for url in self._video_library._videos.keys():
            tag=self._video_library._videos[url]._tags
            title=self._video_library._videos[url]._title
            if len(tag)==0:
                s=title+" ("+url+") "+"[]"
            else:
                s=title+" ("+url+") "+"["
                count=1
                for i in tag:
                    s=s+i
                    if count==1:
                        s=s+" "
                    count+=1
                s=s+"]"
            l.append(s)
            s=""
        l.sort()
        for p in l:
            print(p)
        
        # print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        if video_id in self._video_library._videos:
            if self.playing=="":
                if self.pause=="":
                    play=self._video_library._videos[video_id]._title
                    print("Playing video: {}".format(play))
                    self.playing=video_id
                    self.pause=""
                else:
                    stop=self._video_library._videos[self.pause]._title
                    play=self._video_library._videos[video_id]._title
                    print("Stopping video: {}".format(stop))
                    print("Playing video: {}".format(play))
                    self.playing=video_id
                    self.pause=""

            else:
                stop=self._video_library._videos[self.playing]._title
                play=self._video_library._videos[video_id]._title
                print("Stopping video: {}".format(stop))
                print("Playing video: {}".format(play))
                self.playing=video_id
                self.pause=""
        else:
            print("Cannot play video: Video does not exist")


        # print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""
        if self.playing=="" and self.pause=="":
            print("Cannot stop video: No video is currently playing")
        else:
            if self.pause!="":
                stop=self._video_library._videos[self.pause]._title
                print("Stopping video: {}".format(stop))
                self.playing=""
                self.pause=""
            else:
                stop=self._video_library._videos[self.playing]._title
                print("Stopping video: {}".format(stop))
                self.playing=""
                self.pause=""

        # print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        num=random.randint(1,len(self._video_library.get_all_videos()))
        count=1
        if len(self._video_library.get_all_videos())!=0:
            for i in self._video_library._videos.keys():
                if count==num:
                    self.play_video(i)
                    break
                count+=1
        else:
            print("No videos available")
        # print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if self.playing=="" and self.pause=="":
            print("Cannot pause video: No video is currently playing")
        else:
            if self.pause=="":
                pause=self._video_library._videos[self.playing]._title
                print("Pausing video: {}".format(pause))
                self.pause=self.playing
                self.playing=""
            else:
                pause=self._video_library._videos[self.pause]._title
                print("Video already paused: {}".format(pause))

        # print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.playing=="" and self.pause=="":
            print("Cannot continue video: No video is currently playing")
        else:
            if self.pause=="":
                    print("Cannot continue video: Video is not paused")
            else:
                contin=self._video_library._videos[self.pause]._title
                print("Continuing video: {}".format(contin))
                self.playing=self.pause
                self.pause=""

        # print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        if self.playing=="" and self.pause=="":
            print("No video is currently playing")
        else:
            if self.pause=="":
                tag=self._video_library._videos[self.playing]._tags
                if len(tag)!=0:
                    print("Currently playing: {} ({}) [{} {}]{}".format(self._video_library._videos[self.playing]._title,self.playing,tag[0],tag[1],""))
                else:
                    print("Currently playing: {} ({}) [{} {}]{}".format(self._video_library._videos[self.playing]._title,self.playing,"","",""))
            else:
                tag=self._video_library._videos[self.pause]._tags
                if len(tag)!=0:
                    print("Currently playing: {} ({}) [{} {}]{}".format(self._video_library._videos[self.pause]._title,self.pause,tag[0],tag[1]," - PAUSED"))
                else:
                    print("Currently playing: {} ({}) [{} {}]{}".format(self._video_library._videos[self.pause]._title,self.pause,"",""," - PAUSED"))

        # print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
