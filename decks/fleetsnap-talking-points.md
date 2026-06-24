# FleetSnap Review · What to Say

---

## Slide 1 · Title

"I pulled your live Search Console data and your PostHog analytics, and put the two together. A few things jumped out that I think are genuinely useful whether you work with us or not."

"This is about what's already working and where the biggest open lane is."

---

## Slide 2 · Traffic more than doubled

"First, the headline: your traffic roughly doubled last quarter. Visitors up 114%, page views up 200%, sessions up 141%."

"What really stands out is a 16-minute average session and a 26% bounce rate. That's exceptional. People who land are sticking around and digging in."

"So this isn't a fix-what's-broken conversation. It's an amplify-what-works conversation."

"The question is where the growth comes from next. Let's look at how people find you today."

---

## Slide 3 · How people find you

"Right now, your traffic is community-driven. Direct is biggest at 652, then Organic Social at 357. That's your Facebook host groups working exactly like you described."

"Organic Search is only 326 visitors. That feels low. And on the next slide I'll show you why that's actually the most exciting number in here."

If asked why Direct is so high: "Some of that is your logged-in customers using the app, plus untagged links shared in groups. It's real, but it's not a channel you can scale on demand. Search is."

"Here's the search opportunity."

---

## Slide 4 · The 17,000 vs 71 slide

"Google shows your earnings tool to people 17,000 times in 90 days. Out of all those, 71 clicked through."

"That's a 0.4% click-through rate at an average position of 8."

"Here's why that's good news. The demand is clearly there. Seventeen thousand searches. You're just not capturing the clicks. And the page itself converts fine once people arrive. So this is a titles-and-positioning fix, not a rebuild."

"Closing even a slice of that gap is the single highest-return thing you can do on the site. The audience is already raising their hand."

"And the data even tells us which topics to chase."

---

## Slide 5 · What to write next

"On the call you guessed 'Turo Calculator' was lower-quality traffic. The data backs you up. 932 impressions, 6 clicks. Those are mostly people just curious what they'd earn, not buyers."

"Your brand term converts beautifully, 28% click-through. And co-hosting is where it gets interesting: 752 impressions on the co-hosting calculator but only 3 clicks. Higher intent, badly captured."

"So the content roadmap is to pull away from the 'calculator' crowd and lean into co-hosting and fleet-automation topics, the language your actual buyers use."

"Now, you mentioned AEO and people finding you through ChatGPT. Let's talk about that."

---

## Slide 6 · AEO baseline

"You said a couple folks found you through ChatGPT. I confirmed it. ChatGPT 2 visitors, Gemini 2, Reddit 9, last quarter."

"Small numbers, and I'm showing you on purpose, because this is your zero line. The whole point of AEO work is moving that number, and the magic here is your tracking already catches it."

"The play is seeding Reddit through independent voices on threads that already get traffic, because the LLMs lean on Reddit as a source. Then we watch those referral numbers climb in PostHog quarter over quarter."

"Most agencies can't prove AEO is working. You'll be able to, because the instrumentation is already there."

"Speaking of instrumentation, let's talk about whether all this traffic actually converts."

---

## Slide 7 · Conversion funnels

"GSC stops at the Google click. PostHog picks up what happens next. You've got strong tracking at the top of the funnel, and one gap at the bottom I want to flag, because it's actually an easy win."

"Of 505 people who opened the earnings tool, 85, about 17%, uploaded their data, and 25, about 5%, generated a full report. That report-generated number is your real activation metric."

"The single biggest drop is right at the start, the upload step. 83% leave before uploading their CSV. Make that first step easier and everything downstream grows."

"On the concierge side, of 209 viewers, 45, about 22%, selected a tier. Good intent for an $800-to-$2K offer."

"Now, the lead-capture and payment steps show zero, but that's not real, you obviously have paying customers. Those events aren't firing yet: your v2 paywall just relaunched June 11, and payments go through Stripe, which sits outside PostHog. So the fix is wiring up those events. Once we do, you'll be able to see true cost per customer."

"That's a fast, concrete win we can knock out early, and it makes every future decision data-backed."

"Based on all of this, here's where we'd actually be able to help."

---

## Slide 8 · How EmberTribe fits

"Your needs line up with three things we do. I'll keep this quick."

"On-page and technical SEO is priority one: that's the titles-and-meta work to capture the seventeen thousand impressions. Fastest return."

"SEO content and strategy is priority two: the co-hosting and fleet-automation roadmap so you're pulling in buyers, not calculator tire-kickers."

"AEO and Reddit seeding is priority three: growing that ChatGPT and Gemini baseline, with the lift tracked in your PostHog."

"It's modular. You don't have to take all three. Start with the highest-leverage piece and scope to where you are. We work with bootstrapped teams all the time."

"So if you did want to move, here's the order I'd put them in."

---

## Slide 9 · Three moves / next steps

"Three priorities, in order."

"One, capture the seventeen thousand. Rewrite titles and meta on the tool pages to lift that click-through. Fastest win, the audience is already there."

"Two, build co-hosting content that matches your real buyers."

"Three, start seeding AEO on Reddit and track the lift."

"All three of these you could run in-house. I've given you the data either way. If you'd rather we run it so you can focus on the product, that's where EmberTribe comes in. No pressure on this call."

"Of those three, which feels most urgent to you?"

---

## Slide 10 · Appendix (only if he asks for specifics)

"First, credit where it's due: the on-page work you shipped in June is strong. I audited your live HTML across a dozen crawlers, and your pages serve Google, Bing, ChatGPT, Perplexity, and the social scrapers full content with unique titles, meta descriptions, canonicals, clean headings, and rich structured data. That's a real foundation, so this isn't a rebuild."

"I did find two gaps worth fixing. First, your homepage, your strongest brand page, isn't prerendered like the others. It still serves the generic shell with no unique title or schema, so it's punching below its weight."

"Second, OAI-SearchBot, the crawler behind ChatGPT Search, is getting an empty page. GPTBot and ChatGPT are allowed, but that one search bot slips through, which directly affects the AEO you care about."

"Beyond those, two medium-term items: move from the current bot-by-bot rendering to a setup where every visitor gets the full HTML, and double-check the star-rating schema on a couple pages so it's backed by real reviews. All quick fixes on a good base."
