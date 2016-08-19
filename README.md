# spotify-puzzles
Python solutions to the Spotify puzzles found here -> https://labs.spotify.com/puzzles/

This is My First Python. I originally wrote solutions to these puzzles in PHP and thought porting them over would be trivial. Oh I was wrong, I had to adapt my way of thinking in ways I wasn't quite expecting, the for loops are a bit different, there's this thing called splicing that was new to me and if I didn't explicitly define variable types I will get stupid answers (I mean `1/2 = 0.5` right? ...wrong! You must tell python you want a float: `1/float(2) = 0.5`).

## Reverse Binary (Confirmed)
Surprisingly this one worked first time. I could have used built-in functions to convert from decimal to binary in one line but then where's the fun in that? So I reinvented the wheel and implemented my own functions to do this. Not much more to say about this.

## Zipf's Song (Confirmed)
I found this one quicker to implement but failed to get the correct solution from spotify after a few attempts. Initially I just read all the songs from the input in because that seamed like the sensible thing to do, I mean why would they not want me to analyse all the input they sent me? And in the examples provided, reading all the input yielded the correct solutions. 
After much head scratching, I resorted back to closer inspection of the question (Note: always read the question). So the observing, unlike me, would have noticed the subtle instructions provided in bold:
>The first line of input contains two integers n and m (1 ≤ n ≤ 50000, 1 ≤ m ≤ n), the number of songs on the album, and the number of songs to select. **Then follow n lines.** The i’th of these lines contains an integer fi and string si, where 0 ≤ fi ≤ 10^12 is the number of times the i’th song was listened to, and si is the name of the song. 

So the issue was that the number of songs to be read into my program had to match the first number provided in the first line of the input - don't just accept the whole lot! By implementing a simple break clause to escape the superfulous lines, the program passed the test - decent.

## Cats vs Dogs (in progress)
Don't get me started on this one...
