import streamlit as st

st.title("🎧 Daelicent Playlist")
st.caption("A soundtrack for Daelicent")

songs = {
    "Lover, You Should’ve Come Over - Jeff Buckley": {
        "url": "https://youtu.be/HxfE6PJmGS8",
        "lyrics": """
Looking out the door I see the rain  
Fall upon the funeral mourners  
Parading in a wake of sad relations  
As their shoes fill up with water  

Maybe I'm too young  
To keep good love from going wrong  
But tonight you're on my mind  
So... you'll never know  

Broken down and hungry for your love  
With no way to feed it  
Where are you tonight?  
Child, ya know how much I need it  

Too young to hold on  
And too old to just break free and run  

Sometimes a man gets carried away  
When he feels like should be having his fun  
Much too blind to see the damage he's done  
Sometimes a man must awake to find that  
Really he has no one  

So I'll wait for you, love  
And I'll burn  
Will I ever see your sweet return?  
Oh, will I ever learn?  
Oh-oh, lover, you should've come over  
'Cause it's not too late  

Lonely is the room, the bed is made  
The open window lets the rain in  
Burning in the corner is the only one who dreams  
He had you with him  

My body turns  
And yearns for a sleep that won't ever come  
It's never over  
My kingdom for a kiss upon her shoulder  
It's never over  
All my riches for her smiles  
When I've slept so soft against her  

It's never over  
All my blood for the sweetness of her laughter  
It's never over  
She is the tear that hangs inside my soul forever  

Oh, but maybe I'm just too young  
To keep good love from going wrong  

Oh-oh-oh, lover  
You should've come over, yeah, yes  
Yes, I feel too young to hold on  
And much too old to break free and run  
Too deaf, dumb and blind to see the damage I've done  
Sweet lover, you should've come over  

Oh, love, well I've waited for you  
Lover, lover, lover  
Lover, love, love, love, love, love, love!  
Lover, you should've come over  
'Cause it's not too late  
"""
    },
    "Undress - Sombr": {
        "url": "https://youtu.be/fOQ_-gZsnYQ",
        "lyrics": """
You had a dream, you wanted better  
You were sick of all the holes in your sweater  
You looked to me and wondered whether  
I was the lamppost to which you were tethered  

I'm lookin' at you and you're lookin' at me  
But the glimmer in your eyes is sayin' you wanna leave  
You're sayin' to me what you're sayin' to me  
But the glimmer in your eyes is tellin' me other things  

I don't wanna get undressed  
For a new person all over again  
I don't wanna kiss someone else's neck  
And have to pretend it's yours instead  

I took the train to see my mother  
I look across the tracks to see you with another  
There's nothin' worse than seein' your lover  
Moving on while you still suffer  

I'm lookin' at you and you're lookin' at me  
But the glimmer in your eyes is sayin' you wanna leave  
You're sayin' to me what you're sayin' to me  
But the glimmer in your eyes is tellin' me other things  

I don't wanna get undressed  
For a new person all over again    
I don't wanna kiss someone else's neck  
And have to pretend it's yours instead  

And I don't wanna learn another scent  
I don't want the children of another man  
To have the eyes of the girl I won't forget  
I won't forget  

I don't wanna get undressed  
For a new person all over again  
I don't wanna kiss someone else's neck  
And have to pretend it's yours instead  

I don't wanna get undressed  
For a new person all over again  
"""
    },
    "The 1 - Taylor Swift": {
        "url": "https://youtu.be/KsZ6tROaVOQ",
        "lyrics": """
And if my wishes came true, it would've been you.  
In my defense, I have none.  
For never leaving well enough alone.  
But it would've been fun, if you would've been the one.  
"""
    },
    "Mystery of Love - Sufjan Steven": {
        "url": "https://youtu.be/gVVhHjyC04k?si=snSYVoznmq9i_xbo",
        "lyrics": """
Like Hephaestion, who died  
Alexander's lover.  
Now my riverbed has dried.  
Shall I find no other?  
"""
    },
    "Ghost - Halsey": {
        "url": "https://youtu.be/-r7WTPeCh-I?si=ohEYcgPOyxEwEbCa",
        "lyrics": """
I'm searching for something that I can't reach  

I don't like them innocent  
I don't want no face fresh  
Want them wearing leather  
Begging, let me be your taste test  
I like the sad eyes, bad guys  
Mouth full of white lies  
Kiss me in the corridor  
But quick to tell me goodbye  

You say that you're no good for me  
'Cause I'm always tugging at your sleeve  
And I swear I hate you when you leave  
I like it anyway  

My ghost  
Where'd you go?  
I can't find you in the body sleeping next to me  
My ghost  
Where'd you go?  
What happened to the soul you used to be?  

You're a Rolling Stone boy  
Never sleep alone boy  
Got a million numbers  
And they're filling up your phone, boy  
I'm off the deep end, sleeping  
All night through the weekend  
Saying that I love him but  
I know I'm gonna leave him  

You say that you're no good for me  
'Cause I'm always tugging at your sleeve  
And I swear I hate you when you leave  
I like it anyway  

My ghost  
Where'd you go?  
I can't find you in the body sleeping next to me  
My ghost  
Where'd you go?  
What happened to the soul that you used to be  

I'm searching for something that I can't reach  

My ghost  
Where'd you go?  
I can't find you in the body sleeping next to me  
My ghost  
Where'd you go?  
What happened to the soul that you used to be  
"""
    },
    "Dark Paradise - Lana Del Rey": {
        "url": "https://youtu.be/dvSZQ4oMHGM",
        "lyrics": """
And there's no remedy for memory, your face is like a melody.  
It won't leave my head.  
Your soul is haunting me and telling me that everything is fine.  
But I wish I was dead (dead, like you)  
"""
    },
    "The Night We Met - Lord Huron": {
        "url": "https://youtu.be/KtlgYxa6BMU",
        "lyrics": """
I had all and then most of you  
Some and now none of you.  
Take me back to the night we met.  
I don't know what I'm supposed to do,  
Haunted by the ghost of you.  
Oh, take me back to the night we met.
"""
    }
}

selected_song = st.radio("Choose a song", list(songs.keys()))

st.subheader(selected_song)
st.video(songs[selected_song]['url'])

if "lyrics" in songs[selected_song]:
    st.markdown("**Lyrics:**")
    st.markdown(songs[selected_song]["lyrics"])
