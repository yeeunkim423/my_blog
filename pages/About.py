import streamlit as st
import streamlit.components.v1 as components


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
    "Daddy Issues - The Neighbourhood": {
        "url": "https://youtu.be/gzA53VsWCr8?si=_PchT1c53bR-wjis",
        "lyrics": """
Take you like a drug  
I taste you on my tongue  

You ask me what I'm thinking about  
I tell you that I'm thinking about  
Whatever you're thinking about (ah)  
Tell me something, then I'll forget  
And you might have to tell me again  
It's crazy what you do for a friend  

Go ahead and cry, little girl  
Nobody does it like you do  
I know how much it matters to you  
I know that you got daddy issues  
And if you were my little girl  
I'd do whatever I could do  
I'd run away and hide with you  
I know that you got daddy issues  
And I do too  

I tried to write your name in the rain  
But the rain never came, so I made with the Sun  
The shade always comes at the worst times (ah)  

You ask me what I'm thinking about  
I tell you that I'm thinking about  
Whatever you're thinking about  
Tell me something, then I'll forget  
And you might have to tell me again  
It's crazy what you do for a friend  

Go ahead and cry, little girl  
Nobody does it like you do  
I know how much it matters to you  
I know that you got daddy issues  
And if you were my little girl  
I'd do whatever I could do  
I'd run away and hide with you  
I know that you got daddy issues  

I keep on trying to let you go  
I'm dying to let you know  
How I'm getting on  
I didn't cry when you left at first  
But now that you're dead it hurts  
This time I gotta know  
Where did my daddy go?  

I'm not entirely here  
Half of me has disappeared  

Go ahead and cry, little boy  
You know that your daddy did too  
You know what your mama went through  
You gotta let it out soon, just let it out  

Go ahead and cry, little girl  
Nobody does it like you do  
I know how much it matters to you  
I know that you got daddy issues  
And if you were my little girl  
I'd do whatever I could do  
I'd run away and hide with you  
I know that you got daddy issues  
And I do too  

If you were my little girl  
I'd do whatever I could do  
I'd run away and hide with you  
I know that you got daddy issues  
And I do too    
"""
    },
    "I Wanna Be Yours - Arctic Monkeys": {
        "url": "https://youtu.be/nyuo9-OjNNg?si=p0ts6uEBsJ110QSX",
        "lyrics": """
I wanna be your vacuum cleaner  
Breathing in your dust  
I wanna be your Ford Cortina  
I will never rust  

If you like your coffee hot  
Let me be your coffee pot  
You call the shots, babe  
I just wanna be yours  

Secrets I have held in my heart  
Are harder to hide than I thought  
Maybe I just wanna be yours  
I wanna be yours, I wanna be yours  

Wanna be yours  
Wanna be yours  
Wanna be yours  

Let me be your 'leccy meter  
And I'll never run out  
Let me be the portable heater  
That you'll get cold without  

I wanna be your setting lotion (wanna be)  
Hold your hair in deep devotion (how deep?)  
At least as deep as the Pacific Ocean  
I wanna be yours  

Secrets I have held in my heart  
Are harder to hide than I thought  
Maybe I just wanna be yours  
I wanna be yours, I wanna be yours  

Wanna be yours  
Wanna be yours  
Wanna be yours  
Wanna be yours  

Wanna be yours  
Wanna be yours  
Wanna be yours  
Wanna be yours  

I wanna be your vacuum cleaner (wanna be yours)  
Breathing in your dust (wanna be yours)   
I wanna be your Ford Cortina (wanna be yours)  
I will never rust (wanna be yours)  

I just wanna be yours (wanna be yours)  
I just wanna be yours (wanna be yours)  
I just wanna be yours (wanna be yours)      
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
I'm doing good, I'm on some new shit  
Been saying yes instead of no  
I thought I saw you at the bus stop, I didn't though  
I hit the ground running each night  
I hit the Sunday matinée  
You know, the greatest films of all time were never made  

I guess you never know, never know  
And if you wanted me, you really should've showed  
And if you never bleed, you're never gonna grow  
And it's alright now    

But we were something, don't you think so?  
Roaring twenties, tossing pennies in the pool  
And if my wishes came true  
It would've been you  
In my defense, I have none  
For never leaving well enough alone  
But it would've been fun  
If you would've been the one  
(Ooh)  

I had this dream you're doing cool shit  
Having adventures on your own  
You meet some woman on the internet and take her home  
We never painted by the numbers, baby  
But we were making it count  
You know, the greatest loves of all time are over now  

I guess you never know, never know  
And it's another day waking up alone  

But we were something, don't you think so?  
Roaring twenties, tossing pennies in the pool  
And if my wishes came true  
It would've been you  
In my defense, I have none  
For never leaving well enough alone  
But it would've been fun  
If you would've been the one  

I, I, I persist and resist the temptation to ask you  
If one thing had been different  
Would everything be different today?  

We were something, don't you think so?  
Rosé flowing with your chosen family  
And it would've been sweet  
If it could've been me  
In my defense, I have none  
For digging up the grave another time  
But it would've been fun  
If you would've been the one  
(Ooh)  
"""
    },
    "Mystery of Love - Sufjan Stevens": {
        "url": "https://youtu.be/gVVhHjyC04k?si=snSYVoznmq9i_xbo",
        "lyrics": """
Oh, to see without my eyes  
The first time that you kissed me  
Boundless by the time I cried  
I built your walls around me  

White noise, what an awful sound  
Fumbling by Rogue River  
Feel my feet above the ground  
Hand of God, deliver me  

Oh, oh woe-oh-woah is me  
The first time that you touched me  
Oh, will wonders ever cease?  
Blessed be the mystery of love  

Lord, I no longer believe  
Drowned in living waters  
Cursed by the love that I received  
From my brother's daughter  

Like Hephaestion, who died  
Alexander's lover  
Now my riverbed has dried  
Shall I find no other?  

Oh, oh woe-oh-woah is me  
I'm running like a plover  
Now I'm prone to misery  
The birthmark on your shoulder reminds me  

How much sorrow can I take?  
Blackbird on my shoulder  
And what difference does it make  
When this love is over?  

Shall I sleep within your bed?  
River of unhappiness  
Hold your hands upon my head  
'Til I breathe my last breath  

Oh, oh woe-oh-woah is me  
The last time that you touched me  
Oh, will wonders ever cease?  
Blessed be the mystery of love   
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
All my friends tell me I should move on  
I'm lying in the ocean, singing your song  
Ah, ah, ah, ah  
That's how you sang it  

Loving you forever can't be wrong  
Even though you're not here, won't move on  
Ah, ah, ah, ah  
That's how we played it  

And there's no remedy for memory  
Your face is like a melody  
It won't leave my head  
Your soul is haunting me and telling me  
That everything is fine  
But I wish I was dead (dead, like you)  

Every time I close my eyes  
It's like a dark paradise  
No one compares to you  
I'm scared that you  
Won't be waiting on the other side  

Every time I close my eyes  
It's like a dark paradise  
No one compares to you  
I'm scared that you  
Won't be waiting on the other side  

All my friends ask me why I stay strong  
Tell 'em when you find true love, it lives on  
Ah, ah, ah, ah  
That's why I stay here  

And there's no remedy for memory  
Your face is like a melody  
It won't leave my head  
Your soul is haunting me and telling me  
That everything is fine  
But I wish I was dead (dead, like you)  

Every time I close my eyes  
It's like a dark paradise  
No one compares to you  
I'm scared that you  
Won't be waiting on the other side  

Every time I close my eyes  
It's like a dark paradise  
No one compares to you  
But there's no you  
Except in my dreams tonight  

Oh, oh, oh, oh, ha, ha, ha, ha  
I don't wanna wake up from this tonight  
Oh, oh, oh, oh, ha, ha, ha, ha  
I don't wanna wake up from this tonight  

There's no relief  
I see you in my sleep  
And everybody's rushing me  
But I can feel you touching me  

There's no release  
I feel you in my dreams  
Telling me I'm fine  
 
Every time I close my eyes  
It's like a dark paradise  
No one compares to you  
I'm scared that you  
Won't be waiting on the other side (so tell me)  

Every time I close my eyes  
It's like a dark paradise  
No one compares to you  
But there's no you  
Except in my dreams tonight  

Oh, oh, oh, oh, ha, ha, ha, ha  
I don't wanna wake up from this tonight  
Oh, oh, oh, oh, ha, ha, ha, ha  
I don't wanna wake up from this tonight  
"""
    },
    "The Night We Met - Lord Huron": {
        "url": "https://youtu.be/KtlgYxa6BMU",
        "lyrics": """
I am not the only traveler  
Who has not repaid his debt  
I've been searching for a trail to follow again  
Take me back to the night we met  

And then I can tell myself  
What the hell I'm supposed to do  
And then I can tell myself  
Not to ride along with you  

I had all and then most of you  
Some and now none of you  
Take me back to the night we met  

I don't know what I'm supposed to do  
Haunted by the ghost of you  
Oh, take me back to the night we met  

When the night was full of terrors  
And your eyes were filled with tears  
When you had not touched me yet  
Take me back to the night we met  
 
I had all and then most of you  
Some and now none of you  
Take me back to the night we met  
 
I don't know what I'm supposed to do  
Haunted by the ghost of you  
Take me back to the night we met  
"""
    }
}

selected_song = st.radio("Choose a song", list(songs.keys()))

st.subheader(selected_song)
st.video(songs[selected_song]['url'])

if "lyrics" in songs[selected_song]:
    st.markdown("**Lyrics:**")
    st.markdown(songs[selected_song]["lyrics"])
components.html(
    """
    <style>
      #topButton {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 12px 18px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 16px;
        z-index: 9999;
      }
      #topButton:hover {
        background-color: #45a049;
      }
    </style>

    <button id="topButton">맨 위로 가기 ⬆️</button>

    <script>
      document.getElementById('topButton').addEventListener('click', function() {
        window.scrollTo({top: 0, behavior: 'smooth'});
      });
    </script>
    """,
    height=60
)

