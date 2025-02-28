# bpm-to-showcontroller-live-converter

This is a small aplication that can convert BPM to the value you have to set the speedmaster in Showcontroller/Dynamics Live to get the specific BPM you want.

I made this since the speedmaster in Live doesn't correspond to any BPM in a "logical" way. So this means when the fader is at 255 the actual BPM is way higher. I made this calculator by making some "probe points" with another script I used for detecting the actual BPM and then noting the BPM and the corresponding fader value.

Why did I even make this application?
I control Showcontroller Live via ArtNet and therefor I use the speedmaster to set the speed of the song for Live. This application does not send a MidiClock signal or something like that. It just calculates the fader value that you can then use in your lighting control software. 