# Welcome!
This is my repository on how I manage to scrape [/health/diseases] specifically as for a reason being a prerequisite on my whole project (check my profile for more info)

# Run through
myClevelandClinic's website design made webscrappers hard to surf to the website recursively and wget-level's function. The issue is that the importante links/href of the main target wont be at reach for the fact that it will be only shown when an ::after/::before will be occured to effect that class of a <code>&lt;div&gt;</code>. Long story short, it acquired be to insert more effort to achieve the surfing phenomenon of wget and href level entries. 
So I had to check if there is another way to achieve what I want to achieve (to get the specific pages of what I want, easily. A script way), and that is I found that I can enter a page fully (literally a page with no changes or whatsoever) without knowing its futhur URL (I guess a part of their GET api only acquires an I.D of the page). So i.e /health/diseases/12345 and it will either return a 'not found' page as a return of myClevelandClinic or its full URL /health/diseases/12345-title_name-of-the-page.
By that being discovered, I will have a list of real I.D(s) that I can used for the next script to be lastly iterate the list of I.Ds. 
## Why not combine the two scripts? 
1 request can have an average return of 1-2seconds and I am iterating 30,000 potential ID(s) that is so much time. 
The other reason is that I am concern with my remote's 3-4GB storage left and not having an idea of how many pages or ID(s) that is available.
The latter reason is my real reason by the way. I also considered the other reason but the second reason is just a play safe for me and saving my time for the other problems that I will be encountering.
