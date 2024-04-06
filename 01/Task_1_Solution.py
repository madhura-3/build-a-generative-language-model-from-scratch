import random
from string import punctuation
from collections import defaultdict


class MarkovChain:
    def __init__(self):
        self.graph = defaultdict(list)

    def _tokenize(self, text):
        return (
            text.translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def train(self, text):
        tokens = self._tokenize(text)
        for i, token in enumerate(tokens):
            if (len(tokens) - 1)  == i:
                break
            self.graph[token].append(tokens[i + 1])
               

    def generate(self, prompt, length=10):
        # get the lask token from the prompt
        current = self._tokenize(prompt)[-1]
        # initialize the output
        output = prompt
        for i in range(length):
            # look up the options in the graph dictionary
            options = self.graph.get(current, [])
            if not options:
                continue
            # use random.choice method to pick a current option
            current = random.choice(options)
            
            # add the random choice to the output string
            output += f" {current}"
    
        return output

text = """
You're on the phone with your girlfriend
She's upset, she's going off about something that you said
'Cause she doesn't get your humor like I do

I'm in the room, it's a typical Tuesday night
I'm listening to the kind of music she doesn't like
And she'll never know your story like I do

But she wears short skirts
I wear T-shirts
She's cheer captain
And I'm on the bleachers
Dreaming about the day when you wake up and find
That what you're looking for has been here the whole time

If you could see
That I'm the one
Who understands you
Been here all along
So, why can't you see
You belong with me
You belong with me

Walk in the streets with you in your worn-out jeans
I can't help thinking this is how it ought to be
Laughing on a park bench thinking to myself
"Hey, isn't this easy?"

And you've got a smile
That could light up this whole town
I haven't seen it in a while
Since she brought you down

You say you're fine I know you better than that
Hey, what you doing with a girl like that?

She wears high heels
I wear sneakers
She's cheer captain
And I'm on the bleachers
Dreaming about the day when you wake up and find
That what you're looking for has been here the whole time

If you could see
That I'm the one
Who understands you
Been here all along
So, why can't you see
You belong with me

Standing by and waiting at your backdoor
All this time how could you not know, baby?
You belong with me
You belong with me

Oh, I remember you driving to my house
In the middle of the night
I'm the one who makes you laugh
When you know you're 'bout to cry
I know your favorite songs
And you tell me about your dreams
Think I know where you belong
Think I know it's with me

Can't you see
That I'm the one
Who understands you?
Been here all along
So, why can't you see
You belong with me

Standing by and waiting at your backdoor
All this time how could you not know, baby?
You belong with me
You belong with me

You belong with me

Have you ever thought just maybe
You belong with me?
You belong with me

I stay out too late
Got nothing in my brain
That's what people say, mmm-mmm
That's what people say, mmm-mmm

I go on too many dates
But I can't make them stay
At least that's what people say, mmm-mmm
That's what people say, mmm-mmm

But I keep cruising
Can't stop, won't stop moving
It's like I got this music
In my mind
Saying, "It's gonna be alright."

'Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off
Heart-breakers gonna break, break, break, break, break
And the fakers gonna fake, fake, fake, fake, fake
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off

I never miss a beat
I'm lightning on my feet
And that's what they don't see, mmm-mmm
That's what they don't see, mmm-mmm

I'm dancing on my own (dancing on my own)
I make the moves up as I go (moves up as I go)
And that's what they don't know, mmm-mmm
That's what they don't know, mmm-mmm

But I keep cruising
Can't stop, won't stop grooving
It's like I got this music
In my mind
Saying, "It's gonna be alright."

'Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off
Heart-breakers gonna break, break, break, break, break
And the fakers gonna fake, fake, fake, fake, fake
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off

Shake it off, I shake it off,
I, I, I shake it off, I shake it off,
I, I, I shake it off, I shake it off,
I, I, I shake it off, I shake it off

Hey, hey, hey
Just think while you've been getting down and out about the liars and the dirty, dirty cheats of the world,
You could've been getting down to this sick beat.

My ex-man brought his new girlfriend
She's like "Oh, my God!" but I'm just gonna shake.
And to the fella over there with the hella good hair
Won't you come on over, baby? We can shake, shake, shake

Yeah ohhh

'Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate (haters gonna hate)
I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off
Heart-breakers gonna break, break, break, break, break (mmmm)
And the fakers gonna fake, fake, fake, fake, fake (and fake, and fake, and fake)
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off

Shake it off, I shake it off,
I, I, I shake it off, I shake it off,
I, I, I shake it off, I shake it off
I, I, I shake it off, I shake it off

Shake it off, I shake it off,
I, I, I shake it off, I shake it off,
I, I, I shake it off, I shake it off,
I, I, I shake it off, I shake it off

Shake it off, I shake it off,
I, I, I shake it off, I shake it off (you've got to),
I, I, I shake it off, I shake it off,
I, I, I shake it off, I shake it off
'Cause, baby, now we got bad blood
You know it used to be mad love
So take a look what you've done
'Cause, baby, now we got bad blood
Hey
Now we got problems
And I don't think we can solve them
You made a really deep cut
And, baby, now we got bad blood
Hey

Did you have to do this? I was thinking that you could be trusted
Did you have to ruin what was shiny? Now it's all rusted
Did you have to hit me where I'm weak? Baby, I couldn't breathe
And rub it in so deep, salt in the wound like you're laughing right at me

Oh, it's so sad to think about the good times, you and I

'Cause, baby, now we got bad blood
You know it used to be mad love
So take a look what you've done
'Cause, baby, now we got bad blood
Hey
Now we got problems
And I don't think we can solve them
You made a really deep cut
And, baby, now we got bad blood
Hey

Did you think we'd be fine? Still got scars on my back from your knife
So don't think it's in the past, these kinda wounds they last and they last
Now did you think it all through? All these things will catch up to you
And time can heal but this won't, so if you're coming my way, just don't

Oh, it's so sad to think about the good times, you and I

'Cause, baby, now we got bad blood
You know it used to be mad love
So take a look what you've done
'Cause, baby, now we got bad blood
Hey
Now we got problems
And I don't think we can solve them
You made a really deep cut
And, baby, now we got bad blood
Hey

Band-aids don't fix bullet holes
You say sorry just for show
If you live like that, you live with ghosts (ghosts)
Band-aids don't fix bullet holes (hey)
You say sorry just for show (hey)
If you live like that, you live with ghosts (hey)
Mhmmm
If you love like that blood runs cold

'Cause, baby, now we got bad blood
You know it used to be mad love (mad love)
So take a look what you've done
'Cause, baby, now we got bad blood
Hey
Now we got problems
And I don't think we can solve them (think we can solve them)
You made a really deep cut
And, baby, now we got bad blood
(Hey)

'Cause, baby, now we got bad blood
You know it used to be mad love
So take a look what you've done (look what you've done)
'Cause, baby, now we got bad blood
Hey
Now we got problems
And I don't think we can solve them
You made a really deep cut
And, baby, now we got bad blood
Hey
"""

chain = Answer.MarkovChain()
chain.train(text)
sample_prompt = "You know"
print(chain.generate(sample_prompt))

result = chain.generate(sample_prompt)
